#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    numSwaps=0
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j+1]<a[j]:
                a[j+1],a[j] = a[j], a[j+1]
                numSwaps+=1
    print("Array is sorted in {0} swaps.".format(numSwaps))
    print("First Element: {0}".format(a[0]))
    print("Last Element: {0}".format(a[len(a)-1]))
