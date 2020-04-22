dice = [1,2,3,4,5,6];

sample = len(dice);
cases = 0;
for i in dice:
	if i % 2 != 0:
		cases+=1;
		
Pr = cases/sample;
print(Pr)

	
		
