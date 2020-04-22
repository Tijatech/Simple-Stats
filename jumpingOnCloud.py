import math
import os
import random
import re
import sys

def jumpingOnClouds(n,c):
	jumps = 0;
	i = 0;
	for i in range(n-1):
		if c[i-1] == 0:
			print(c[i]);
			if c[i-1] == c[i+1] and i < n -1:
				jumps+=1;
				i +=1;
			else:
				jumps+=1;
		else:
				jumps+=0;

	return jumps;
			




if __name__ == '__main__':
#	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	n = int(input())
	c = list(map(int, input().rstrip().split()))
	result = jumpingOnClouds(n, c)
#	fptr.write(str(result) + '\n')
#	fptr.close();