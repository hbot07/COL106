#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    openingBrackets = {'(', '{', '['}
    closingBrackets = {')', '}', "]"}
    brackets_pair = {'(': ')', '{': '}', '[': ']'}
    bracketStack = []

    for i in s:
        if i in openingBrackets:
            bracketStack.append(i)

        if i in closingBrackets:
            if len(bracketStack) == 0:
                return 'NO'
            bracket = bracketStack.pop()  # bhenchod ye toh dekhle empty toh nahi
            if brackets_pair[bracket] != i:
                return 'NO'

    if len(bracketStack) != 0:
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
