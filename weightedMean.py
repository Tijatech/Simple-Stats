N = int(input());

numbers1 = input();
numbers2 = input();

array1 = numbers1.split(" ");
array2 = numbers2.split(" ");

def unPackArray(array):
	X = [];
	for i in array:
		i = int(i);
		X.append(i);
	return X;
	
	
X = unPackArray(array1);
W = unPackArray(array2);




def getWeightedMean(X, W, N):
	products = [];
	for i in range(N):
		product = X[i] * W[i];
		products.append(product);
	weightedMean = sum(products)/sum(W);
	return round(weightedMean,1);
		
		
		
weightedMean = getWeightedMean(X, W, N);
print(weightedMean);