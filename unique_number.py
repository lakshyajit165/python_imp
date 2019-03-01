# Initial Template for Python 3



# Driver Code
def main():
    testcase = int(input())

    while testcase > 0:
        numbers = input().split()
        l = sorted_elements(numbers)

        for x in l:
            print(x, end=' ')

        print()
        testcase -= 1


if __name__ == '__main__':
    main()

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''


# User function Template for python3
# Function to print elements in sorted order
def sorted_elements(numbers):
    # Your code here
    # return the list which contains
    # elements in sorted order
    A = []
    for i in numbers:
        A.append(int(i))
    A.sort()
    B = []
    for i in A:
        if i not in B:
            B.append(i)
    return B