# -*- coding: utf-8 -*-

import sqlite3

from .config import db_file


def get_cache(url):
    print("getting", url)
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("SELECT html FROM webpage WHERE url=?", (url,))
    result = c.fetchall()[0][0]
    conn.close()
    return result