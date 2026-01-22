M=[[0,0,0],
   [0,0,0],
   [0,0,0]]

def print_matrix(M):
    for row in M:
        print(row)
print_matrix(M)

def Identity_matrix(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if i == j:
                M[i][j] = 1
            else:
                M[i][j] = 0
    print_matrix(M)
Identity_matrix(M)