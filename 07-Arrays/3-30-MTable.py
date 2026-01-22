x=[[0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0]]

for i in range(len(x)):
    for j in range(len(x[i])):
        x[i][j]=(i+1)*(j+1)
        
for row in x:
    print(row)