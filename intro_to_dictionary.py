'''

Given a list of string containing names of students and another list containing marks
of corresponding students.
The task is to create a dictionary to store marks of students with their name
(name will be unique).

Input Format:
First line of input contains number of testcases T. For each testcase, first line of input contains N, number of students, and next two line contains N names and N marks respectively.

Output Format:
For each testcase, create a dictionary and print each key and corresponding value of dictionary in sorted order.

Constraints:
1 <= T <= 100
1 <= N <= 104
1 <= marks <= 104

User Task:
The task is to complete the function create_dict() which creates a dictionary and returns it.

Example:
Input:
1
5
john ala ilia sudan mercy
100 200 150 80 300

Output:
ala 200
ilia 150
john 100
mercy 300
sudan 80

'''


def create_dict(arr):
    #dict = {}

    di = dict(arr)
    return di

    # Your code here
    # Hint: use loop to iterate through arr
    # and assign key value to the dict


    #return dict


testcases = int(input())

# Looping through testcases
while (testcases > 0):
    size_arr = int(input())

    name = input().split()
    marks = input().split()
    arr = list()
    for i in range(0, size_arr, 1):
        arr.append((name[i], marks[i]))

    print(arr)
    dict = create_dict(arr)

    for key in sorted(dict.keys()):
        print(key, dict[key])

    testcases -= 1




