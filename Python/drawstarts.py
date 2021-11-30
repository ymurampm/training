# for i in range(5):
#     string=""
#     for j in range(i):
#         string=string+"*"
#     print(string)

# for i in range(5):
#     string=""
#     for j in range(5-i):
#         string=string+"*"
#     print(string)

height=6
for i in range(height):
    i=i+1
    string=""
    for j in range(height*2-1):
        j=j+1
        if j<=height-i or j-height>=i:
            string=string+" "
        else:
            string=string+"*"
    print(string)

height=6
for i in range(height):
    i=i+1
    string=""
    for j in range(height):
        j=j+1
        if height-i >= j:
            string=string+" "
        else:
            string=string+"*"
    print(string)
