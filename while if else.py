# -*- coding: utf-8 -*-
"""Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b8nDNRcrIPB53c7PJrPlqcwnVOOBhxZb

*COMMENT*
"""

#THIS IS COMMENT
#PLS IGNORE 
print("hello world")

""" this is comment
pls ignore
thanks"""
print("hello world")

a = 34
b = 45
if b < a:
  print("smaller")
elif b == a:
  print("euqal")
else:
  print("bigger")

a = 45
b = 50
c = 55
if b>a and c==a:
  print("ok")
else:
  print("not")

x = 1
while x in range(6):
 print(x)
 x+=1

x = 1
while x < 10:
 print(x)
 x+=1
 if x == 5:
  break

x = 1
while x < 10:
 print(x)
 x+=1
 if x == 5:
  continue