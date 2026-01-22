def f(a):
    print(len(a), len(a[0]))
    return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]

print((f([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]])))

print(f([[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 0]]))

print(f([[4, 5, 6, 7, 8]]))