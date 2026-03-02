def f(arr):
    x=1
    for i in range(len(arr)):
        if arr[i]==arr[i] and x==1:
            x+=1
        elif arr[i] != arr[i-1]:
            return arr[i]  