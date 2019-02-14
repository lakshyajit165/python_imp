# Initial Template for Python 3
# User function Template for python3
# insert into dictionary
def insert_dict(query, dict):
    # Your code here
    dict[query[1]] = query[2]


# deleting from dictionary
def del_dict(query, dict):
    # Your code here
    if (query[1] in dict.keys()):
        del dict[query[1]]


# print marks of required name
def print_dict(key, dict):
    # Your code here
    #print(dict)
    if key in dict.keys():
        print("Marks of " + key + "is " + dict[key])
    else:
        return False


testcase = int(input())

# looping through testcases
while (testcase > 0):

    n = int(input())

    i = 0
    dict = {}
    while i < n:
        flag = False
        delete = False
        query = input().split()
        if (query[0] == 'i'):
            insert_dict(query, dict)
            print("Inserted")

        if (query[0] == 'd'):
            if del_dict(query, dict) is False:
                print("-1")
            else:
                print("Deleted")

        if (query[0] == 'p'):
            if (print_dict(query[1], dict) is False):
                print("-1")

        i += 1

    testcase -= 1