def no_duplicate_letters(x):
	return all([ aWord.count(let)==1 for aWord in x.split() for let in aWord ])


print(no_duplicate_letters("Fortune favors the bold"))