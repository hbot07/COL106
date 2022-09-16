#!/bin/python3

import math
import os
import random
import re
import sys


class Stack:
    def __init__(self):
        self.data = []
        self.height = 0

    def push(self, element):
        self.data.append(element)
        self.height += element

    def pop(self):
        self.height -= self.data.pop()


#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    s1, s2, s3 = Stack(), Stack(), Stack()
    for i in range(len(h1)-1, -1, -1):
        s1.push(h1[i])
    for i in range(len(h2)-1, -1, -1):
        s2.push(h2[i])
    for i in range(len(h3)-1, -1, -1):
        s3.push(h3[i])




# Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
