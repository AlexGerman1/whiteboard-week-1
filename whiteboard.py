# -*- coding: utf-8 -*-
"""Docstring"""

import io


def open():
    f = io.open('corpora.txt', encoding='utf-8')
    corpora_data = f.read()
    f.close()
    print(f)
    return
