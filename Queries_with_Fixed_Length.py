#!/usr/bin/env python3

if __name__ == "__main__":
    n, q = [int(x) for x in input().strip().split()]
    arr = [int(x) for x in input().strip().split()]
    
    for _ in range(q):
        d = int(input().strip())
        maxes = []
        was_first = False
        
        for i in range(n - d + 1):
            if i == 0 or was_first == True:
                #print(arr[i:i+d])
                maxes.append(max(arr[i:i+d]))
            else:
                #print("max({}, {})".format(maxes[-1], arr[i+d-1]))
                maxes.append(max(maxes[-1], arr[i+d-1]))
                
            if maxes[-1] == arr[i]:
                was_first = True
            else:
                was_first = False
            
        print(min(maxes))
            
### upto this, code passed the all test cases ###

### remaining commented code is not required which is defaultly given by hackerrank ###

# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'solve' function below.
# #
# # The function is expected to return an INTEGER_ARRAY.
# # The function accepts following parameters:
# #  1. INTEGER_ARRAY arr
# #  2. INTEGER_ARRAY queries
# #

# def solve(arr, queries):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     q = int(first_multiple_input[1])

#     arr = list(map(int, input().rstrip().split()))

#     queries = []

#     for _ in range(q):
#         queries_item = int(input().strip())
#         queries.append(queries_item)

#     result = solve(arr, queries)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()

########################### EXPLANATION #########################################
if __name__ == "__main__":
    # Read the values for n (length of the array) and q (number of queries)
    n, q = [int(x) for x in input().strip().split()]
    
    # Read the array elements
    arr = [int(x) for x in input().strip().split()]
    
    # Iterate through each query
    for _ in range(q):
        # Read the query parameter 'd' (window size)
        d = int(input().strip())
        
        # Initialize a list to store maximum values in each window
        maxes = []
        
        # Flag to track if the first element in the window was the maximum
        was_first = False
        
        # Iterate through the array to find maximum values in each window of size 'd'
        for i in range(n - d + 1):
            if i == 0 or was_first == True:
                # If it's the first iteration or the first element in the previous window was the maximum,
                # append the maximum value in the current window to the 'maxes' list
                maxes.append(max(arr[i:i+d]))
            else:
                # If not the first iteration, calculate the maximum by comparing the previous maximum
                # with the last element in the current window
                maxes.append(max(maxes[-1], arr[i+d-1]))
                
            # Update the 'was_first' flag based on whether the maximum in the current window
            # is the first element in the window
            if maxes[-1] == arr[i]:
                was_first = True
            else:
                was_first = False
            
        # Print the minimum value from the list of maximum values in each window
        print(min(maxes))
###########################################################################################

------------------------------------------------------------------------------------------------------
'''The code takes an array and a window size as input and finds, for each window of the given size,
the minimum among the maximum values within the window. The primary functionality involves iterating
through the array, maintaining a list of maximum values in each window, and then finding the minimum
among these maximum values for each query.'''
-----------------------------------------------------------------------------------------------------
