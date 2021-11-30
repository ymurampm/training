# Create a function that takes an integer n and returns the factorial of factorials. See below examples for a better understanding:

# Examples
# fact_of_fact(4) ➞ 288
# # 4! * 3! * 2! * 1! = 288

# fact_of_fact(5) ➞ 34560

# fact_of_fact(6) ➞ 24883200


def fact(x):
  factnum=1
  for i in range(x):
    factnum=factnum*(i+1)
  return factnum

def fact_of_fact(y):
  fof=1
  for i in range(y):
    fof=fof*(fact(i+1))
  return fof

print(fact_of_fact(5))


