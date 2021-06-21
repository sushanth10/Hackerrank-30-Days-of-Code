#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max_sum = arr[1][1]+ sum(arr[0][0:3]) + sum(arr[2][0:3])
    for i in range(1, 5):
        for j in range(1,5):
            glass_sum = arr[i][j]+ sum(arr[i-1][j-1:j+2]) + sum(arr[i+1][j-1:j+2])
            if glass_sum > max_sum:
                max_sum = glass_sum
    
    print(max_sum)