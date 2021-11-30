#3x3の表の足し算関数

def add_table(x,y):
  tmp=[[0,0,0],[0,0,0],[0,0,0]]
  for i in range(3):
    for j in range(3):
      tmp[i][j]=x[i][j]+y[i][j]
  return tmp

table1=[[1,1,1],[2,2,2],[3,3,3]]
table2=[[1,1,3],[2,2,4],[3,3,6]]

print(table1)
print(table2)
print(add_table(table1,table2))

