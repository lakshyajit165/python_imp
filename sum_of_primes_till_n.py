def SieveOfEratosthenes(n):
    sum = 0
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for i in range(2, n + 1):
        if (prime[i]):
            sum += i
    return sum

t = int(input())
while (t != 0):
    n = int(input())
    print(SieveOfEratosthenes(n))
    t -= 1