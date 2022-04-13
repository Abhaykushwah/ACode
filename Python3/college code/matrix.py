r = int(input("Enter the order of square matrix : "))
column = []
for i in range(r):
   row=[]
   for j in range(r):
      row.append(int(input()))
   column.append(row)
#print(lst)
for i in range(r):
   for j in range(r):
      print(column[i][j], end=' ')
   print()
