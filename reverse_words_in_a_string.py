t = int(input())
while(t!=0):
    A = input().split('.')
    for i in range(len(A)-1,-1,-1):
        if(i == 0):
            print(A[i],end='')
        else:
            print(A[i],end='.')
    print()
    t-=1