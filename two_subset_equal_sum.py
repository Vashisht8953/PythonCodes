def isSubsetsum (arr,n,sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    if arr[n-1] > sum:
        return isSubsetsum (arr, n-1, sum)

    
    return isSubsetsum (arr, n-1, sum) or isSubsetsum (arr, n-1, sum-arr[n-1])

def findPartion (arr, n):
    sum = 0
    for i in range(0, n):
        sum += arr[i]

    if sum%2 != 0:
        return False

    return isSubsetsum (arr, n, sum//2)

arr = [15,5,20,10,35,15,10]
n = len(arr)
if findPartion (arr, n) == True:
    print("Can be devided into two subsetsof equal sum")
    
else:
    print("Can't be devided into two subsetsof equal sum")
