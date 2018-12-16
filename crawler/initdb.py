# -*- coding: utf-8 -*-

import sqlite3
import os
import shutil
import shutil
import pickle

from config import db_file
from config import word_file
from config import init_words
from config import word_file
from config import searched_word_file
from config import init_file
from config import pagerank_file
from config import inverted_index_file
from config import cache_dir


def initdb():

    if os.path.exists(db_file):
        os.remove(db_file)

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute(
        '''
        create table webpage (
            url text primary key,
            title text not null
        )
        '''
    )
    cursor.execute(
        '''
        create table ref (
            s_url text not null,
            d_url text not null,
            primary key (s_url, d_url)
        )
        '''
    )
    cursor.execute(
        '''
        create table webpage_word (
            url integer not null references webpage(url),
            word varchar(12) not null,
            primary key (url, word)
        )
        '''
    )

    #cursor.execute('create table invindex (id int primary key, cont varchar(160))')

    cursor.close()
    conn.commit()

    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
    os.mkdir(cache_dir)

    with open(word_file, "wb") as f:
        pickle.dump(init_words, f)

    with open(searched_word_file, "wb") as f:
        pickle.dump(set(), f)

    with open(pagerank_file, "wb") as f:
        pickle.dump([], f)

    with open(inverted_index_file, "wb") as f:
        pickle.dump([], f)

    with open(init_file, "wb") as f:
        pass