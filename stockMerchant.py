import math
import os
import random
import re
import sys

def jumpingOnClouds(n,c):
	jumps = 0;
	for i in range(n-1):
		if c[i] == 0:
			if c[i-1] == c[i+2]:
				jumps+=1;
			else:
				jumps+=1;
		else:
				jumps+=0;
	return jumps;
			




if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	n = int(input())
	c = list(map(int, input().rstrip().split()))
	result = jumpingOnClouds(n, c)
	fptr.write(str(result) + '\n')
	fptr.close();
	print(result);