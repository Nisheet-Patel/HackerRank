#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minn = 0 
    maxx = 0
    
    for i in range(len(arr)):
        summ = 0
        for j in range(len(arr)):
            if j!=i:
                summ += arr[j]
        if summ <= minn or minn == 0:
            minn = summ
        if summ >= maxx or maxx == 0:
            maxx = summ
    
    print("{} {}".format(minn,maxx))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
