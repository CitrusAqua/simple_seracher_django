# -*- coding: utf-8 -*-


import requests
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
import re
import time
import sqlite3
import jieba
import threadpool
import brotli
import pickle
from math import ceil
import urllib

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from config import db_file
from config import search_sites
from config import accept_domains
from config import init_words
from config import word_file
from config import searched_word_file
from config import key_batch_size
from config import skip_prefix
from config import cache_dir
from config import chromedriver_path

from log import log

from index import index
from pagerank import pagerank

from data_getters import prefix_getter



webpage_cmds = set()
ref_cmds = set()
word_cmds = set()

searched = set()
keywords = set()
new_key = set()



def new_driver():
    chrome_options = Options()
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-referrers')
    #chrome_options.add_argument("user-data-dir=N:\\PyProjects\\simple_seracher_django\\crawler\\profile\\");
    chrome_options.add_experimental_option( "prefs", {'profile.default_content_settings.images': 2})
    driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=chrome_options)
    return driver


def parse_url(url, domain):

    url = url.split('?', 1)[0]
    url = url.split('#', 1)[0]

    for p in skip_prefix:
        if url.startswith(p):
            return None

    if url.startswith("https://") or url.startswith("http://") or url.startswith("//"):
        e = url.split('/')[2]
        #print(e)
        flag = False
        for n in e.split('.'):
            if n in accept_domains:
                flag = True
        if not flag:
            return None
        if url.startswith("//"):
            return "https:" + url
        return url
    return domain + url


def proc_search(domain, url, headers, key):

    print("searching", url+key)

    href_list = []
    tit_list = []

    special_getter = False

    for k in prefix_getter:
        if url.startswith(k):
            href_list, tit_list = prefix_getter[k](key)
            special_getter = True
            break

    if not special_getter:
        res = requests.Response()
        try:
            s = requests.Session()
            s.mount('https://', HTTPAdapter(max_retries=10))
            res = s.get(url+key, headers=headers)
            s.close()
        except:
            log('Failed fetching:\n\t' + url+key)
            return

        content = res.content
        if res.headers.get('Content-Encoding') == 'br':
            content = brotli.decompress(content)
        content = content.decode("utf-8")
        html = content

        soup = BeautifulSoup(html, "lxml")

        for a in soup.find_all('a', href=True):
            if a.has_attr('title'):
                tit_list.append(a['title'])
            else:
                tit_list.append(a.text)
            href_list.append(a['href'])

    if tit_list is None and href is None:
        log('Failed fetching:\n\t' + url+key)
        return

    for a in tit_list:
        seg_list = jieba.cut_for_search(a)
        for w in seg_list:
            if w not in searched:
                new_key.add(w)

    for href in href_list:
        url = parse_url(href, domain)
        if url is not None:
            get_webpage(domain, url, headers)

    #driver.quit()



def get_webpage(domain, url, headers, retries=0):
    #print(url)
    url = urllib.parse.unquote(url)

    res = requests.Response()
    try:
        s = requests.Session()
        s.mount('https://', HTTPAdapter(max_retries=10))
        res = s.get(url, headers=headers)
        s.close()
    except:
        log('Failed fetching:\n\t' + url)
        return

    content = res.content
    if res.headers.get('Content-Encoding') == 'br':
        content = brotli.decompress(content)
    content = content.decode("utf-8", errors="ignore")
    html = content


    soup = BeautifulSoup(html, "lxml")

    tit = ''

    special_getter = False

    for k in prefix_getter:
        if url.startswith(k):
            tit = prefix_getter[k](url)
            special_getter = True
            break

    if tit is None:
        if retries < 5:
            get_webpage(domain, url, headers, retries+1)
        else:
            log("No title: "+url)
        return

    if not special_getter:
        tit = soup.find('title')
        if tit is None or tit.text == "":
            tit = soup.find('h1')
            if tit is None or tit.text == "":
                tit = soup.find('h2')
                if tit is None or tit.text == "":
                    tit = soup.find('h3')
                    if tit is None or tit.text == "":
                        tit = soup.find('h4')
                        if tit is None or tit.text == "":
                            tit = soup.find('h5')
                            if tit is None or tit.text == "":
                                tit = soup.find('h6')
        if tit is None or tit.text == "":
            if retries < 5:
                get_webpage(domain, url, headers, retries+1)
            else:
                log("No title: "+url)
            return
        tit = tit.text

    # Save cache
    filename = urllib.parse.quote(url, safe="")
    with open(cache_dir+filename+'.cache', "w", encoding="utf-8") as f:
        f.write(html)


    webpage_cmds.add(("insert into webpage (url, title) values (?, ?)", (url, tit)))

    seg_list = jieba.cut_for_search(tit)
    for w in seg_list:
        word_cmds.add(("insert into webpage_word (url, word) values (?, ?)", (url, w)))

    content = ''
    for a in soup.find_all('h1'):
        if a.has_attr('title'):
            content = a['title']
        else:
            content = a.text
        seg_list = jieba.cut_for_search(content)
        for w in seg_list:
            word_cmds.add(("insert into webpage_word (url, word) values (?, ?)", (url, w)))

    #for a in soup.find_all('a', href=True, title=True):
    for a in soup.find_all('a', href=True):
        pg = a['href']
        pg = parse_url(pg, domain)
        if pg is not None:
            ref_cmds.add(("insert into ref (s_url, d_url) values (?, ?)", (url, pg)))





def crawler():
    try:
        conn = sqlite3.connect(db_file)
        conn.text_factory = str
        pool = threadpool.ThreadPool(8)

        # Init keywords
        with open(word_file, "rb") as f:
            keywords = pickle.load(f)
        with open(searched_word_file, "rb") as f:
            searched = pickle.load(f)

        while True:
            keywords_list = list(keywords)
            while len(keywords_list) != 0:
                init_vals = []
                for k in keywords_list[:key_batch_size]:
                    for site in search_sites:
                        for search_page in site['search_page']:
                            init_vals.append(([site['domain'], search_page, site['header'], k], None))

                threqs = threadpool.makeRequests(proc_search, init_vals)
                [pool.putRequest(req) for req in threqs]
                pool.wait()

                print("Commiting...")

                cursor = conn.cursor()

                for cmd in webpage_cmds:
                    try:
                        cursor.execute(cmd[0], cmd[1])
                    except:
                        pass

                for cmd in word_cmds:
                    try:
                        cursor.execute(cmd[0], cmd[1])
                    except:
                        pass

                for cmd in ref_cmds:
                    try:
                        cursor.execute(cmd[0], cmd[1])
                    except:
                        pass

                cursor.close()
                conn.commit()

                webpage_cmds.clear()
                ref_cmds.clear()
                word_cmds.clear()

                print("Ranking and indexing...")
                pagerank()
                index()

                print("Saving keywords...")

                for k in keywords_list[:key_batch_size]:
                    searched.add(k)

                keywords_list = keywords_list[key_batch_size:]

                with open(word_file, "wb") as f:
                    pickle.dump(set(keywords_list), f)

                with open(searched_word_file, "wb") as f:
                    pickle.dump(searched, f)

                print("Done.")


            keywords = new_key.copy()
            new_key.clear()

            print("Iterator Done.")



    except Exception as e:
        print(e)
    finally:
        conn.close()

