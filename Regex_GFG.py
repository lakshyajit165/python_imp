# Initial Template for Python 3
import re  ##import re module to use regex
''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# User function Template for python3


def numberMatcher(str):
    pat = re.compile(r'\d+')  ##write the pattern here
    match = re.findall(pat, str)  ##find all finds all the matched texts and returns a list
    if (match):
        for i in match:
            print(i, end=" ")
    else:
        print(-1, end="")

def main():
    testcases = int(input())  # testcases
    while (testcases > 0):
        mystr = input()
        numberMatcher(mystr)
        print()
        testcases -= 1


if __name__ == '__main__':
    main()



