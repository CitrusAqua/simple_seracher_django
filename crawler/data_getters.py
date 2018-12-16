# -*- coding: utf-8 -*-

import urllib
import requests
from requests.adapters import HTTPAdapter
import brotli
import json

from config import chromedriver_path
from config import log_file
from config import bili_header
from config import acfun_header

from log import log


def h_bilibili(url):
	id = url.split('/')[-1]
	res = requests.Response()
	try:
		s = requests.Session()
		s.mount('https://', HTTPAdapter(max_retries=3))
		res = s.get('https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id='+id, headers=bili_header)
		s.close()
	except:
		log('Failed fetching:\n\t' + 'https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id='+id)
		return None

	content = res.content
	if res.headers.get('Content-Encoding') == 'br':
		content = brotli.decompress(content)
	content = content.decode("utf-8")

	dat = json.loads(content)
	tit = dat['data']['item']['title'] + ' _ ' + dat['data']['user']['name'] + ' _ 哔哩哔哩相簿'
	return tit


acfun_channelid_name = {
	0: 'a',
	1: 'v',
	60: 'v',
	63: 'a',
	58: 'v',
	1: 'v',
	59: 'z',
}


def search_acfun(key):
	res = requests.Response()
	try:
		s = requests.Session()
		s.mount('https://', HTTPAdapter(max_retries=3))
		res = s.get('http://search.aixifan.com/search?q='+key, headers=acfun_header)
		s.close()
	except:
		log('Failed fetching:\n\t' + 'http://search.aixifan.com/search?q='+key)
		return None, None

	content = res.content
	if res.headers.get('Content-Encoding') == 'br':
		content = brotli.decompress(content)
	content = content.decode("utf-8")

	dat = json.loads(content)

	href_list = []
	tit_list = []

	dat = dat['data']['page']
	for d in dat['sp']:
		contentId = d['contentId']
		title = d['title']
		href = "http://www.acfun.cn/a/"+contentId
		tit_list.append(title)
		href_list.append(href)

	for d in dat['ai']:
		contentId = d['contentId']
		title = d['title']
		href = "http://www.acfun.cn/bangumi/aa"+contentId
		tit_list.append(title)
		href_list.append(href)

	for d in dat['list']:
		contentId = d['contentId']
		title = d['title']
		parentChannelId = d['parentChannelId']
		name = ''
		if parentChannelId in acfun_channelid_name:
			name = acfun_channelid_name[parentChannelId]
		else:
			name = 'v'
		href = "http://www.acfun.cn/"+name+'/'+contentId
		tit_list.append(title)
		href_list.append(href)

	return href_list, tit_list




prefix_getter = {
	'https://h.bilibili.com/': h_bilibili,
	'http://www.acfun.cn/search/': search_acfun,

	}