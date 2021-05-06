def deleteColumns(A):
    l = len(A[0])
    dp = [1]*l
    for i in range(l -2, -1, -1):
        for j in range(i+1, l):
            if all(row[i] <= row[j] for row in A):
                dp[i] = max(dp[i], 1 +dp[j])

    return l- max(dp)

arr = ["zyx", "wvu", "tsr"]
print(deleteColumns(arr))
