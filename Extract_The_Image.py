'''
Extract the image

You are given a string str that contains some html text. In this html text is an image url that is in the tag . You need to extract the url. The image url is of the format .jpg

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains a string str.

Output Format:
For each testcase, in a new line, print the image url. If not present print -1.

Your Task:
This is a function problem. Do not take any input. Just complete the function imgExtracter and print the output.

Constraints:
1 <= T <= 100

Example:
Input:
2
<html><head></head><body><img src='www.geeksforgeeks.org/sample/62.jpg'</body></html>
<html><head></head><body><img src='www.geeksforgeeks.org/sample/99.jpg'</body></html>

'''

# Initial Template for Python 3
import re

#User function Template for python3
def imgExtracter(str):
    ##Your code here
    A = str.split('src=\'')
    print(A[1].split('\'')[0])

def main():
    testcases = int(input())  # testcases
    while (testcases > 0):
        str = input()
        imgExtracter(str)
        testcases -= 1


if __name__ == '__main__':
    main()