def missing(A,n):
    l = 0
    r = n-1
    while(l <= r):
        mid = (l+r)//2
        if(mid == 0 or (A[mid]!=mid+1 and A[mid-1] == mid)):
            return(mid+1)
        elif(A[mid]!=mid+1):
            r = mid - 1
        else:
            l = mid + 1
    return(-1)
n = int(input())
A = list(map(int,input().split()))
print(missing(A,n))