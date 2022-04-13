r = int(input("Enter the order of square matrix : "))
column = []
for i in range(r):
   row=[]
   for j in range(r):
      row.append(int(input()))
   column.append(row)
for i in range(r):
   for j in range(r):
      if(i==j):
         print(column[i][j], end=' ')