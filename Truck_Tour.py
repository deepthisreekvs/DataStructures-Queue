#!/usr/bin/env python3

import queue

if __name__ == "__main__":
    n = int(input().strip())
    res = 0
    tank = 0
    q = queue.Queue()
 
    for ind in range(n):
        petr, dist = [int(arg) for arg in input().strip().split()]
        tank += petr
        
        if dist <= tank:
            tank -= dist
        else:
            tank = 0
            res = ind+1
            
        q.put((petr, dist))
            
    print(res)

####### upto this, code is executed for the all test cases ############
--------------------------------------------------------------------------------------------
####### remaining commented code which is defaultly provided by hackerrank is not required ##############
# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'truckTour' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
# #

# def truckTour(petrolpumps):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     petrolpumps = []

#     for _ in range(n):
#         petrolpumps.append(list(map(int, input().rstrip().split())))

#     result = truckTour(petrolpumps)

#     fptr.write(str(result) + '\n')

#     fptr.close()

--------------------------------------------------------------------------
######## EXPLANATION #############
#!/usr/bin/env python3

import queue

# Main function
if __name__ == "__main__":
    # Read the number of elements
    n = int(input().strip())
    
    # Initialize variables for result, tank capacity, and a queue
    res = 0
    tank = 0
    q = queue.Queue()

    # Loop through each element
    for ind in range(n):
        # Read the petrol and distance values for the current element
        petr, dist = [int(arg) for arg in input().strip().split()]
        
        # Update the tank capacity by adding petrol
        tank += petr
        
        # Check if the current distance is reachable with the current tank capacity
        if dist <= tank:
            tank -= dist
        else:
            # If the distance is not reachable, reset the tank and update the result index
            tank = 0
            res = ind + 1
            
        # Put the petrol and distance values into the queue
        q.put((petr, dist))

    # Print the final result index
    print(res)
#########################################

'''The code simulates a journey with a given number of stops, where at each stop, it refuels the tank based on petrol availability and
consumes fuel to reach the next stop. The main functionality is to find the starting point (stop index) from which the journey can be
completed without running out of fuel. It uses a queue to store petrol and distance values at each stop and updates the result index accordingly.'''
