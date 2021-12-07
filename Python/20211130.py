# linear search

import random

def create_random_array(x):
  tmp=[]
  for i in range(x):
    tmp.append(random.randint(0,10))
  return tmp

def searchchar(x,y):
  flg=False
  for i in range(len(x)):
    if (x[i]==y):
      print("true")
      flg=True
      break
  if (flg==False):
    print("false")

list=(create_random_array(10))
print(list)
searchchar(list,0)

