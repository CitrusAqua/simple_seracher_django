# -*- coding: utf-8 -*-



from time import time


from config import log_file


def log(info):
    with open(log_file, "a", encoding='utf-8') as f:
        f.write(info + '\n')