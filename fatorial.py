#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
