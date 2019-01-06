'''
    Find nCr for given n and r.

    Input:
    First line contains number of test cases T. T testcases follow. Each testcase contains 1 line of input containing 2 integers n and r separated by a space.

    Output:
    For each testcase, in a new line, find the nCr. Modulus your output to 10power9+7.

    Constraints:
    1 <= T <= 50
    1<= n <= 1000
    1<= r <=800

    Example:
    Input:
    1
    3 2
    Output:
    3
'''


for t in range(int(input())):
    n, r = map(int, input().split())
    c = n - r

    f = 1
    while (r > 0):
        f = f * r;
        r -= 1
    fact = 1;
    while (n > c):
        fact *= n
        n -= 1
    res = fact // f
    print(res % (1000000000 + 7))