#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean_val = sum(arr)/len(arr)
    sum_dev_squares = 0
    for i in arr:
        sum_dev_squares += (i-mean_val)**2
    variance = sum_dev_squares/len(arr)
    print("%.1f"%(variance**0.5))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
