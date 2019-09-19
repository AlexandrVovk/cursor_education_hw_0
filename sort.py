#!/usr/bin/python
import os
import sys

#students = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

digit = 'VII'

newgrades = {'I': 'A', 'V': 'B', 'X': 'C', 'L': 'D', 'C': 'E', 'D': 'F', 'M': 'G'}

print sorted(digit, key=newgrades.__getitem__)