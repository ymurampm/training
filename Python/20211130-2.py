# linear search

import random

def create_random_array(x):
  tmp=[]
  a=0
  for i in range(x):
    a=a+random.randint(0,10)
    tmp.append(a)
  return tmp

def searchchar(x,y):
  start=0
  end=len(x)
  mid=(start+end)//2
  flg=False
  while (start<end-1):
    print(start,mid,end)
    if x[mid]==y:
      print("true")
      flg=True
      break
    if (x[mid]>y):
      end=mid
    else:
      start=mid
    mid=(start+end)//2
  if (flg==False):
    print("false")

list=(create_random_array(10))
print(list)
num=random.randint(0,50)
print(num)
searchchar(list,num)

