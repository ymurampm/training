# # A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

# # Create a function that determines whether a number is a Disarium or not.

# # Examples
# # is_disarium(75) ➞ False
# # # 7^1 + 5^2 = 7 + 25 = 32

# # is_disarium(135) ➞ True
# # # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

# # is_disarium(544) ➞ False

# # is_disarium(518) ➞ True

# # is_disarium(466) ➞ False

# # is_disarium(8) ➞ True

# #3x3の表の足し算関数

# def get_digit(x):
#   return len(str(x))

# def get_nth_digit(x,y):
#   return (x // (10**(y-1))) % 10

# def disarium(x):
#   disarium_num=0
#   digit=get_digit(x)
#   for i in range(get_digit(x)):
#     base=get_nth_digit(x,i+1)
#     # print(base)
#     for j in range(digit-i-1):
#       base=base*get_nth_digit(x,i+1)
#     # print(base)
#     disarium_num=disarium_num+base

#   return disarium_num

# def is_disarium(y):
#   if y==disarium(y):
#     return True
#   else:
#     return False

# print(is_disarium(135))


num=int(input("Enter a number: "))
copynum=num
total=0
l=len(str(num))

while(num>0):
    remainder=num%10
    print(remainder)
    num=num//10
    total+=remainder**l 
    l-=1
    
if(total==copynum):
    print("True")
else:
    print("False")