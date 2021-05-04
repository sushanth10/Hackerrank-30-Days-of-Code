#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary_n = bin(n)
    max_count = 0
    count = 0
    for i in binary_n[2:]:
        if i=='1':
            count+=1
        else:
            count=0
        if count>max_count:
            max_count = count
    print(max_count)
