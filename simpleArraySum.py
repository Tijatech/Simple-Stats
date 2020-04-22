import math
import os
import random
import re
import sys

def simpleArraySum(ar):
	total = sum(ar);
	return total;


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	ar_count = int(input())
	ar = list(map(int, input().rstrip().split()))
	result = simpleArraySum(ar)
	fptr.write(str(result) + '\n')
	fptr.close();
	print(result)