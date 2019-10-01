while True:
	print("List of functions you may like to choose: ")
	print("Function 1: Print hello world ")
	print("Function 2: Print Hello with your name ")
	print("Function 3: Transfer Celsius temperature from Celsius to Fahrenheit ")
	
	input2=input('Which function do you like to execute? 1, 2 or 3')
	if input2== '1':
	 print('Hello, world!')
	elif input2== '2':
	 nam=input('Who are you?')
	 print("Hello,",nam,"!")
	elif input2== '3':
	  cinput= float(input("What is your temperature in degress Celsius?"))    
	  print('The temperature of',cinput, 'in Fahrenheit temperature is',cinput*1.8+32)
	else: 
	  print('You may enter a wrong number,please choose again,thank you!')
