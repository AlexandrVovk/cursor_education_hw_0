#!/usr/bin/python
import os
import sys

digit_one = raw_input("please type first roman digit: ")

print (digit_one)

digit_two = raw_input("please type first roman digit: ")

print (digit_two)

newgrades = {'M': '1', 'D': '2', 'C': '3', 'L': '4', 'X': '5', 'V': '6', 'I': '7'}

result = sorted(digit_one, key=newgrades.__getitem__)

print (''.join(result))

