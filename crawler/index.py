# -*- coding: utf-8 -*-


import sqlite3
import jieba
import pickle

from config import db_file
from config import inverted_index_file


from log import log


def index():

    conn = sqlite3.connect(db_file)

    invindex = dict()

    c = conn.cursor()
    c.execute("SELECT url, word FROM webpage_word")
    result = c.fetchall()

    for row in result:
        if row[1] not in invindex:
            invindex[row[1]] = [row[0]]
        else:
            invindex[row[1]].append(row[0])


    with open(inverted_index_file, 'wb') as f:
        pickle.dump(invindex, f)


    conn.close()