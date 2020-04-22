import math
import os
import random
import re
import sys

def compareTriplets(a, b):
	aRate = 0;
	bRate = 0;
	for  i in range(len(a)):
			if a[i] > b[i]:
				aRate +=1;
			if a[i] < b[i]:
				bRate +=1;
			rate = str(aRate) +" " + str(bRate)
	return rate;
	


if __name__ == '__main__':
#	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	
	a = list(map(int, input().rstrip().split()))
	b = list(map(int, input().rstrip().split()))
	result = compareTriplets(a,b)
#	fptr.write(str(result) + '\n')
#	fptr.close();
	print(result)