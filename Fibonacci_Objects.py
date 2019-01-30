# Fibonacci Objects

'''

You are given two objects. Each object has data members x,y, and z.
You need to find the nth fibonacci object. The nth fibonacci object is given by F(n)=F(n-1)+F(n-2); n>2
You need to sum the corresponding values of obj1 and obj2 to get obj3.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains three lines of input. The first line contains x,y,z values of obj1. The second line contains x,y,z values of obj2. The third lines  contains n.

Output Format:
For each testcase, in a new line, print the x,y,z values of nth fibonacci object

Your Task:
This is a function problem, you don't need to output anything. Just complete the function nthFibO and return the object.

Constraints:
1 <= T <= 100

Examples:
Input:
1
1 2 3
4 5 6
3
Output:
5 7 9



'''

# Initial Template for Python 3
class FibO:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def fiboSum(self, obj):
        self.x += obj.x
        self.y += obj.y
        self.z += obj.z

    def getCoord(self):
        print(self.x, self.y, self.z)

    def deepCopy(self, obj):
        self.x, self.y, self.z = obj.x, obj.y, obj.z



# Completed the code below
def nthFibO(n, a, b):
    ##Your code here
    if(n == 1):
        return a
    elif(n == 2):
        return b
    else:
        for i in range(3,n+1):
            obj = FibO(a.x, a.y, a.z)
            obj.fiboSum(b)
            a = b
            b = obj
        return obj



# Given
def main():
    testcases = int(input())  # testcases
    while (testcases > 0):
        xyz1 = [int(i) for i in input().split()]
        x1 = xyz1[0]
        y1 = xyz1[1]
        z1 = xyz1[2]

        xyz2 = [int(i) for i in input().split()]
        x2 = xyz2[0]
        y2 = xyz2[1]
        z2 = xyz2[2]

        n = int(input())
        obj1 = FibO(x1, y1, z1)
        obj2 = FibO(x2, y2, z2)
        (nthFibO(n, obj1, obj2).getCoord())

        testcases -= 1


if __name__ == '__main__':
    main()


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# User function Template for python3



