R = 4
C = 4

def counterClockspiralPrint(m, n, arr):
    k = 0
    l = 0
    count = 0

    total = m*n

    while(k<m and l<n):
        if(count == total):
            break
        for i in range(k, m):
            print(arr[i][l], end = " ")
            count =+ 1
        l += 1

        if(count == total):
            break

        for i in range(l, n):
            print( arr[m-1][i], end = " ")

            count += 1
        m -= 1

        if(count == total):
            break

        if(k< m):
            for i in range(m-1, k-1, -1):
                print(arr[i][n-1], end = " ")
                count += 1
            n -= 1

        if (count == total):
            break

        if (l<n):
            for i in range(n-1, l-1, -1):
                print(arr[k][i], end = " ")
                count += 1

            k += 1

arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]
counterClockspiralPrint( R, C, arr)







             
        
