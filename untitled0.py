# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:23:53 2019

@author: user
"""

print('hhh')
lt=[]
for i in range(1,7):
    lt.append(i)
s=input('enter rthe string')
lt=s.split()
print(lt)
print(s[::-1])

s1='hello world how are you'
l1=s1.count('h')
print(l)



from collections import Counter 
test_str = "GeeksforGeeks"
  
# using collections.Counter() to get  
# count of each element in string  
res = Counter(test_str) 

  
# printing result  
print (res) 

n = int(input())
arr1=[]
for i in range(0,n):
    arr1.append(i)
    sort(arr1)
    
    
def ar(r):
    a=3.14*r*r
    return a
ar(4)
        



n1=int(input())
n2=int(input())
lt=[]
for i in range(0,n2):
    lt=lt.append(i)
    
    
    
import calendar
print (calendar.TextCalendar(firstweekday=6).formatyear(2015))

import calendar
#calendar.Calendar(calendar.SUNDAY)
user_input = input().split()
month = int(user_input[0])
day = int(user_input[1])
year = int(user_input[2])
c = calendar.weekday(year, month, day)

if c == 0:
    print("MONDAY")
elif c == 1:
    print("TUESDAY")
elif c == 2:
    print("WEDNESDAY")
elif c==3:
    print("THURSDAY")
elif c==4:
    print("FRIDAY")
elif c== 5:
    print("SATURDAY")
elif c==6:
    print("SUNDAY")
    
def solve(s):
    for i in s:
    if i==" ":
      i=i+1
      i=i.capatilise()
  return i    
  
s='shyam ysadav'
s1=s.split(' ')
s2=s1.strip()
print(s2)




from collections import OrderedDict
foo = "mppmt"
result = "".join(OrderedDict.fromkeys(foo))

print('enter the string')
s=input().split()
s1=set(s)
print(s1)





def dupe(str1):
    s=set(str1)
    s1="".join(s)
    return "".join(s)
str1='geeksforgeeks'
a=dupe(str1)
print(a)













