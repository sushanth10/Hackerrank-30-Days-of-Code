#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    q2 = arr[n//2]
    if len(arr)%2==0:
        q2 = (arr[n//2-1]+arr[n//2])/2
    arr1 = [x for x in arr if x<q2]
    arr2 = [y for y in arr if y>q2]
    
    # print(q2, arr1, arr2)
    n = len(arr1)
    q1 = arr1[n//2]
    if len(arr1)%2==0:
        q1 = (arr1[n//2-1]+arr1[n//2])/2
        
    n =  len(arr2)
    q3 = arr2[n//2]
    if len(arr2)%2==0:
        q3 = (arr2[n//2-1]+arr2[n//2])/2
        
    ans = map(int, [q1,q2,q3])
    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
