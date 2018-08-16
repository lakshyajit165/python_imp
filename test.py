n = int(input())
A = list(map(int,input().split()))
q = int(input())
while(q!=0):
    sum = 0
    flag = 0
    t = int(input())
    for i in range(len(A)):
        sum+=A[i]
        if(sum >= t):
            print(i+1)
            flag = 1
            break
    if(flag == 0):
        print("-1")
    q-=1