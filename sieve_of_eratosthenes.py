def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for i in range(2, n + 1):
        if (prime[i]):
            print(i, end=' ')


t = int(input())
while (t != 0):
    n = int(input())
    SieveOfEratosthenes(n)
    print('\n')
    t -= 1
