def no_duplicate_letters(x):
	words = x.split()
	o = []
	for i in range(len(y)):
		o.append('F') if len(set(y[i])) < len(y[i]) else o.append("T") 
	return False if "F" in o else True

print(no_duplicate_letters("Fortune favors the bold"))
