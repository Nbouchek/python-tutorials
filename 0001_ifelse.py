#!/bin/python3

# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird
# Input Format
#
# A single line containing a positive integer, .
#
# Constraints
#
# Output Format
#
# Print Weird if the number is weird; otherwise, print Not Weird.
#
# Sample Input 0

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("Enter a number >>> ").strip())
    if n % 2 == 1:
        print("Weird")
    if n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    if n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    if n % 2 == 0 and n > 20:
        print("Not Weird")
