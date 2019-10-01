def p01():
	print("Hello, world!")
def p02_1():
	name = input("Who are you?")
	print("Hello,",name,"!")
def p02_2():
	input1= input("What is your temperature in degress Celsius?")
	cinput= float(input1)
	print("The temperature of",cinput, "in Fahrenheit temperature is",cinput*1.8+32)

while True:
	print("List of functions you may like to choose: ")
	print("Function 1: Print hello world ")
	print("Function 2: Print Hello with your name ")
	print("Function 3: Transfer Celsius temperature from Celsius to Fahrenheit ")
	
	input2=input('Which function do you like to execute? 1, 2 or 3 You may also enter no to exit this program.')
	if input2== '1':
	 p01()
	elif input2== '2':
	 p02_1()
	elif input2== '3':
	 p02_2()
	elif input2== 'no':
	 break
	else: 
	  print('You may enter a wrong number,please choose again,thank you!')
print('Thanks for using this program!')
