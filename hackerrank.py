# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:47:07 2019

@author: user
"""

str1=input('enter 1st')
str2=input('enter 1st')
try:
    n=str1.find(str2,0,len(str1))
except ValueError:
    print('str2 is not found')
else:
    print('sub string at',n+1)    
    
    
str1=input('enter 1st:  ')
lst=['hackerrank']
l=[]
n=len(str1)
n1=len(lst)
 


def sum(n):
    if n==0:
        return 0
    else:
        return (n%10+sum(int(n/10)))
    print()
    sum(24753)