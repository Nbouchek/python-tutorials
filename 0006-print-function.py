# Read an integer .
#
# Without using any string methods, try to print the following:
#
#
# Note that "" represents the values in between.
#
# Input Format
#
# The first line contains an integer .
#
# Output Format
#
# Output the answer as explained in the task.
#
# Sample Input 0
#
# 3
# Sample Output 0
#
# 123

if __name__ == '__main__':
    # use print(*values, sep=' ', end='\n', file=sys.stdout)
    print(*range(1, int(input()) + 1), sep='')
