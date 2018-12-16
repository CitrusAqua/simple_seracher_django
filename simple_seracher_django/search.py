# -*- coding: utf-8 -*-


import sys
import sqlite3
import jieba
import pickle
from time import time
import os



from .config import db_file
from .config import inverted_index_file
from .config import pagerank_file
from .config import entities_per_page


def intersection(a, b):
    return [e for e in a if e in b]


def take_second(e):
    return e[1]


# return result, result count, elpased time(ms)
def get_search_result(keywords, page=1):

    start = time()

    query = []

    #for arg in sys.argv[1:]:
    #    seg_list = jieba.cut_for_search(arg)
    #    for w in seg_list:
    #        query.append(w)

    for k in keywords.split(' '):
        seg_list = jieba.cut_for_search(k)
        for w in seg_list:
            query.append(w)

    invindex = dict()
    with open(inverted_index_file, "rb") as f:
        invindex = pickle.load(f)

    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("SELECT url FROM webpage")
    result = c.fetchall()

    filtered = []
    for row in result:
        filtered.append(row[0])

    for w in query:
        if w not in invindex:
            filtered = []
            break
        filtered = intersection(filtered, invindex[w])

    rank = {}
    with open(pagerank_file, "rb") as f:
        rank = pickle.load(f)


    with_rank = []
    for u in filtered:
        if u not in rank:
            rnk = 0
        else:
            rnk = rank[u]
        with_rank.append((u, rnk))
    with_rank.sort(reverse=True, key=take_second)


    end = time()
    elp = end - start
    elp_ms = elp * 1000

    res = []

    e_st = entities_per_page * (page-1)
    e_ed = entities_per_page * page
    for u in with_rank[e_st : e_ed]:
        c.execute("SELECT title FROM webpage WHERE url = ?", (u[0],))
        t = c.fetchall()[0][0]
        res.append((u[0], t))

    conn.close()

    return res, len(filtered), elp_ms
