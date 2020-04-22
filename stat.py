N = int(input());
numbers = input();
array = numbers.split(" ");
arrays = [];
for i in array:
	i = int(i);
	arrays.append(i)
	
def getMean(n, array):
	total = sum(array);
	mean = total/n;
	return round(mean, 1);
	
def getMedian(n, array):
	array.sort();
	median = 0;
	if n % 2 == 0:
		median = (array[(n//2)-1] + array[(n//2)])/2;
	else:
		median = array[(n//2)];
	return round(float(median),1)
				
def getMode(array):
	dictionary = {};
	for element in array:
		if element in dictionary.keys():
			dictionary[element] += 1;
		else:
			dictionary[element] = 1;
	max_value = max(dictionary.values());
	if max_value == 1:
		return min(array);
		
	else:
		dictItem = list(dictionary.items());
		maxData = [];
		for i, e in dictItem:
			if e == max_value:
				maxData.append(i);
		return min(maxData);
		
		
def main():
	mean = getMean(N,arrays);
	median = getMedian(N,arrays);
	mode = getMode(arrays);
	print(f"{mean}");
	print(f"{median}");
	print(f"{mode}");
	
main();
