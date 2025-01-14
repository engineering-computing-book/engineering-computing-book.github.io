#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 12:38:03 2024

@author: ricopicone
"""

def print_nonempty(s):
    if s:
        print(s)
    else:
        print("Empty string")

print_nonempty("This should print")
print_nonempty("")      # This should print "Empty string"