#Median function to solve for median of a give list
def getMedian(array):
	n = len(array);
	median = 0;
	avg = n//2;
	if n % 2 == 0:
		median = (array[avg] + array[avg-1])//2;
	else:
		median = array[avg];
	return round(median,1)



#Use to get input and turn them to int
N = int(input());
numbers = input();
array = numbers.split(" ");
arrays = [];
for i in array:
	i = int(i);
	arrays.append(i)
arrays.sort();


# use to find list of numbers that fall between the upper quartile and lower quartile3.
aL = len(arrays)//2;
if N % 2 == 0:
	lowerQ = arrays[:aL]
	upperQ = arrays[aL:]
else:
	lowerQ = arrays[:aL]
	upperQ = arrays[aL +1:]


quartile1 = getMedian(lowerQ)
quartile2 = getMedian(arrays);
quartile3 = getMedian(upperQ)

print(quartile1)
print(quartile2)
print(quartile3)