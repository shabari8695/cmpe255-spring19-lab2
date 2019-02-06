
def mean_num_friends(x):
	sum = 0
	for i in x:
		sum += i

	return sum/len(x)

def median_num_friends(x):
	x.sort()
	if len(x)%2 == 0:
		return (x[len(x)/2 - 1] + x[(len(x)/2)])/2.0
	else:
		return x[int(len(x)/2)]


num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20,60]
print("mean={}".format(mean_num_friends(num_friends)))
print("median={}".format(median_num_friends(num_friends)))