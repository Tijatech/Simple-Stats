import math
import os
import random
import re
import sys

def diagonalDifference(arr):
	ltotal = 0;
	rtotal = 0;
	for i in range(len(arr)):
		for e in range(len(arr[i])):
			if i == e:
				ltotal+= arr[i][e];
		for r in range(-len(arr[i]),0):
			if -(i+1) == r:
				rtotal += arr[i][r];
	total = abs(ltotal - rtotal);
	return total;
			
if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	
	n = int(input().strip());
	arr = [];
	for i in range(n):
		arr.append(list(map(int, input().rstrip().split())));

	result= diagonalDifference(arr);
	fptr.write(str(result) + '\n')
	fptr.close();