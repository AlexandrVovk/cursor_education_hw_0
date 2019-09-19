#!/usr/bin/python
import os
import sys

digit_one = raw_input("please type first roman digit: ")

#print (digit_one)

digit_two = raw_input("please type first roman digit: ")

#print (digit_two)

sum = digit_one+digit_two

#print(sum)

list = {'M': '1', 'D': '2', 'C': '3', 'L': '4', 'X': '5', 'V': '6', 'I': '7'}

result_list = sorted(sum, key=list.__getitem__)

result_str = ''.join(result_list)

print(result_str)

result = result_str.replace('IIIII','V').replace('VV','X').replace('XXXXX','L').replace('LL','C').replace('CCCCC','D').replace('DD','M')

print (result)

print 'The result is: ', result