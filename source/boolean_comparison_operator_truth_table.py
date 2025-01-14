#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:51:37 2024

@author: ricopicone
"""

import operator as op

def print_tabular_data(data):
    for row in data:
        print('\t'.join(map(str, row)))

xl = [
    [False, False], 
    [False, True], 
    [True, False], 
    [True, True], 
    [0, 0], 
    [0, 1], 
    [1, 0], 
    [1, 1]
]
opl = [op.truth, op.not_, op.and_, op.or_, op.eq, op.ne, op.lt, op.gt, op.le, op.ge]

tbl = []
for i, x in enumerate(xl):
    tbl.append([])
    for k, op_ in enumerate(opl):
        if op_ == op.truth:
            tbl[i].append(bool(x[0]))
        elif op_ == op.not_:
            tbl[i].append(not x[0])
        else:
            tbl[i].append(op_(x[0],x[1]))

print_tabular_data(tbl)