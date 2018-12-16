# -*- coding: utf-8 -*-

import sqlite3
import numpy as np
import pandas as pd
import pickle
from scipy import sparse
from scipy.sparse import lil_matrix
import threadpool
from time import time

from config import db_file
from config import pagerank_file


G = dict()
index2node = dict()
node2index = dict()


def proc_PageRank(M, alpha):

    n = M.shape[0]
    v = np.zeros(n)
    def_val = 1/n
    for i in range(n):
        v[i] = def_val
    _v = alpha*M.dot(v) + (1-alpha)*v
    while (abs(v - _v)).sum() > 0.0001:
        v = _v
        _v = alpha*M.dot(v) + (1-alpha)*v

    result = {}
    for ind, prob in enumerate(v):
        if prob != 0:
            result[index2node[ind]] = prob

    return result



def initMat(node1, node2, M):
    M[node2index[node2],node2index[node1]] = 1/len(G[node1])

def Generate_Transfer_Matrix(G):

    for index,node in enumerate(G.keys()):
        node2index[node] = index
        index2node[index] = node
    n = len(node2index)
    M = lil_matrix((n, n), dtype=np.float32)

    for node1 in G.keys():
        G[node1] = {e for e in G[node1] if e in node2index}

    pool = threadpool.ThreadPool(16)
    init_vals = []
    for node1 in G.keys():
        for node2 in G[node1]:
            init_vals.append(([node1,node2,M], None))

    threqs = threadpool.makeRequests(initMat, init_vals)
    for req in threqs:
        pool.putRequest(req)
    pool.wait()

    return M



def pagerank():

    G.clear()
    index2node.clear()
    node2index.clear()

    alpha = 0.85

    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    cursor = c.execute("SELECT s_url, d_url FROM ref")
    for row in cursor:
        if row[0] not in G:
            G[row[0]] = dict()
        G[row[0]][row[1]] = 1

    c.close()
    conn.close()

    M = Generate_Transfer_Matrix(G)

    result = proc_PageRank(M, alpha)

    with open(pagerank_file, "wb") as f:
        pickle.dump(result, f)
