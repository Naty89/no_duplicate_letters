def no_duplicate_letters(x):
	# words = 
	# o = []
	# for i in range(len(y)):
	# 	o.append('F') if len(set(y[i])) < len(y[i]) else o.append("T") 
	# return False if "F" in o else True

	return all([ aWord.count(let)==1 for aWord in x.split() for let in aWord ])


print(no_duplicate_letters("Fortune favors the bold"))