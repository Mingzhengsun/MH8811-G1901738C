def genPassword(n):
	import random
	pass_1=''
	global lower_letter,upper_letter,numbers,symbols
	lower_letter='abcdefghijklmnopqrstuvwxyz'
	upper_letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	numbers='1234567890'
	symbols='!"#$%&\'()*+,-./:;<=>?@][^_`{|}~'
	pass_1=pass_1+random.choice(lower_letter)
	pass_1=pass_1+random.choice(upper_letter)
	pass_1=pass_1+random.choice(numbers)
	pass_1=pass_1+random.choice(symbols)
	group1=lower_letter + upper_letter + numbers + symbols
	for i in group1:
		if n-4>0:
			pass_1=pass_1+random.choice(group1)
			n=n-1
	random.shuffle([pass_1])
	return pass_1

if __name__ == " __main__":
	print(genPassword(12))	
	
	
