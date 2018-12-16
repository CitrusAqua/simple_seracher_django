# -*- coding: utf-8 -*-

import os
import sys

from config import init_file

from crawler import crawler
from initdb import initdb

if __name__ == '__main__':
    if not os.path.exists(init_file):
        print('Initializing database...')
        initdb()
    if len(sys.argv) > 1 and sys.argv[1] == '--clean':
        print('Initializing database...')
        initdb()
    while True:
        #try:
        crawler()
        #except Exception as e:
        #    print(e)