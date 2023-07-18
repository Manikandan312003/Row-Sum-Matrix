def rowSum(arr):
    length=len(arr)
    RowSum=[0 for i in range(length)]
    for i in range(length):
        s=0
        for j in range(len(arr[0])):
            s+=arr[i][j]
        RowSum[i]=s
    return RowSum

print(rowSum([[1,2,3,4],[5,6,7,8],[9,2,3,4]]))