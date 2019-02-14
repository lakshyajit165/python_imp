'''

Sometimes you might need to convert a tuple to dict object to make it more readable.
 In this article, we will try to learn how to convert a list of tuples into a dictionary.
 Here we will find two methods of doing this. Examples:

Input : [("akash", 10), ("gaurav", 12), ("anand", 14),
         ("suraj", 20), ("akhil", 25), ("ashish", 30)]
Output : {'akash': [10], 'gaurav': [12], 'anand': [14],
          'ashish': [30], 'akhil': [25], 'suraj': [20]}

Input : [('A', 1), ('B', 2), ('C', 3)]
Output : {'B': [2], 'A': [1], 'C': [3]}

'''


# Python code to convert into dictionary
def Convert(tup, di):
    di = dict(tup)
    return di


# Driver Code
tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print(Convert(tups, dictionary))