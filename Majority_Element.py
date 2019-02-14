
'''

A majority element in an array A[] of size n is an element that appears
more than n/2 times (and hence there is at most one such element). Write a function which
takes an array and emits the majority element (if it exists),
otherwise prints NONE as follows: Examples:

Input : 3 3 4 2 4 4 2 4 4
Output : 4

Input : 3 3 4 2 4 4 2 4
Output : NONE

'''


# Function to find majority element
from collections import Counter

def majority(arr):

    # convert array into dictionary
    freqDict = Counter(arr)

    # traverse dictionary and check majority element
    size = len(arr)
    for (key,val) in freqDict.items():
         if (val > (size/2)):
             print(key)
             return
    print('None')

# Driver program
if __name__ == "__main__":
    arr = [3,3,4,2,4,4,2,4,4]
    majority(arr)