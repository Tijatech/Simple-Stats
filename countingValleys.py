import math
import os
import random
import re
import sys

def countingValleys(n,s):
	seaLevel = 0;
	valley = 0;
	for i in s:
		if i == "D":
			seaLevel-=1;
		else:
			seaLevel+=1;
			if seaLevel == 0:
				valley+=1;
	return valley;

if __name__ == '__main__':
	#fptr = open(os.environ['OUTPUT_PATH'], 'w')
	n = int(input())
	s = input()
	result = countingValleys(n, s)
	#fptr.write(str(result) + '\n')
	#fptr.close();
print(result);