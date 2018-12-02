A = list(map(int,input().split()))

max = max(set(A),key = A.count)

print("The maximum occuring element is "+ str(max))