A = list(map(int, input().split()))
for i in range(len(A)):
    if(i == 0 and A[i] == 7):
        pass
    elif(i == 0 and A[i] != 7):
        print(A[i], end=' ')
    elif(A[i] == 7 or A[i-1] == 7):
        pass
    else:
        print(A[i],end=' ')