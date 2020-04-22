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
x = input();
f = input();
xs = x.split(" ");
fs = f.split(" ");



dataA = [];

for i in range(N):
		fs[i] = int(fs[i]);
		d = (xs[i]+",")* fs[i];
		dataA.append(d.split(","));

data = []
for e in range(len(dataA)):
	for i in dataA[e]:
		data.append(i);
		
finalData = [];
for i in data:
	try:
		i = int(i);
		finalData.append(i);
	except:
		del(i)
		
finalData.sort();
 #use to find list of numbers that fall between the upper quartile and lower quartile3.
aL = len(finalData)//2;
dataLength = len(finalData);

if dataLength % 2 == 0:
	lowerQ = finalData[:aL]
	upperQ = finalData[aL:]
else:
	lowerQ = finalData[:aL]
	upperQ = finalData[aL +1:]


quartile1 = getMedian(lowerQ)
quartile3 = getMedian(upperQ)

interQuartile = float(quartile3 - quartile1);

print(interQuartile);



