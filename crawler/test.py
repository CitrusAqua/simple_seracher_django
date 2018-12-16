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
from config import bangumi_header

from log import log



if __name__ == '__main__':
    url = "http://bgm.tv/subject_search/%E5%8A%A8"
    res = requests.Response()
    try:
        s = requests.Session()
        s.mount('https://', HTTPAdapter(max_retries=10))
        res = s.get(url, headers=bangumi_header)
        s.close()
    except:
        log('Failed fetching:\n\t' + url)

    content = res.content
    if res.headers.get('Content-Encoding') == 'br':
        content = brotli.decompress(content)
    content = content.decode("utf-8")
    html = content
    print(html)