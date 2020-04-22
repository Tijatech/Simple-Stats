N = int(input());
numbers = input();
array = numbers.split(" ");
arrays = [];
for i in array:
	i = int(i);
	arrays.append(i)
	
def getMean(array):
	n = len(array);
	total = sum(array);
	mean = total/n;
	return mean;
	
	
	
mean = getMean(arrays);
	
total = 0;
for e in arrays:
	total += (e-mean)**2;
	
	
sD = (total/N) ** 0.5;
sD = round(sD,1);
print(sD);
