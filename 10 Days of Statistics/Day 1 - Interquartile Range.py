#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    arr = list()
    for i in range(len(values)):
        arr += [values[i]]*freqs[i]
    arr.sort()
    
    n = len(arr)
    q2 = arr[n//2]
    arr1 = arr2 = list() 
    
    if len(arr)%2==0:
        q2 = (arr[n//2-1]+arr[n//2])/2
        arr1 = arr[:n//2]
        arr2 = arr[n//2+1:]
    else:
        arr1 = arr[:n//2]
        arr2 = arr[n//2+1:]
        
    n = len(arr1)
    q1 = arr1[n//2]
    if len(arr1)%2==0:
        q1 = (arr1[n//2-1]+arr1[n//2])/2
        
    n =  len(arr2)
    q3 = arr2[n//2]
    if len(arr2)%2==0:
        q3 = (arr2[n//2-1]+arr2[n//2])/2
        
    # print(arr1, arr2, q1, q2, q3, n)
    print("%.1f"%(q3-q1))
    
if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
