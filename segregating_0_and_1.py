A = list(map(int,input().split()))
c0 = A.count(0)
n = len(A)
B = []
for i in range(c0):
    B.append(0)
for j in range(n-c0):
    B.append(1)
print(B)
