'''
You have been familiar with Lists in Python and it's various inbuilt functions including sort. Could you think of sorting a list of tuple according to your requirement. This can be made possible through custom sort in Python.

Syntax:
sorted(list, key = compareSort), list is the list you want to sort, and compareSort is the function in which you need to write your comparator.

Example,
list = [('a', 1), ('b', 2), ('c', 3), ('d', 4), (''e', 4)] and we want to sort this list according to second value of tuple and if second value is same, then sort according to first value, then just mention the comparator as key in sort function and define that function with return value as the key according to which you want to sort the list.

Let's implement this out through a question. Given a list of tuples consisting of name and marks of students. The task is to sort the students according to the marks, but wherever same marks is encountered, sort the two according to the name.

Input Format:
First line of input contains number of testcases T. For each testcase, first line of input contains size of list. Next two lines contains N names and N marks respectively.

Output Format:
For each testcase, print the sorted list of tuples according to our requirement.

Constraints:
1 <= T <= 100
1 <= N <= 104
1 <= marks <= 104

User Task:
The task is to complete the comparator function which compares as required.

Example:
Input:
1
5
a b c aad abc
100 100 300 100 100

Output:
a 100 aad 100 abc 100 b 100 c 300

Explanation:
Testcase 1: First, list is sorted according to marks, and when marks are equal, then sorted according to the name.


'''


# Driver Code
def main():
    # Testcase input
    testcases = int(input())

    # Looping through testcases
    while (testcases > 0):
        size_arr = int(input())

        name = input().split()
        marks = input().split()
        arr = list()
        for i in range(0, size_arr, 1):
            arr.append((name[i], marks[i]))

        arr.sort(key=customSort)

        for i in arr:
            print(i[0], i[1], end=" ")

        print()
        testcases -= 1


if __name__ == '__main__':
    main()


# User function Template for python3
# Function to sort using comparator
def customSort(arr):
    # Your code here
    # Hint : Should be a return statement
    return (arr[1], arr[0])