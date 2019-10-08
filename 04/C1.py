#C1

#Write a program that finds the smallest number in a list[9, 41, 12, 3, 74, 15]

the_smallest_number= None
for num in [9, 41, 12, 3, 74, 15]:
	if the_smallest_number is None:
		the_smallest_number=num
	else:
		if the_smallest_number> num:
			the_smallest_number= num

print('The list is:',[9, 41, 12, 3, 74, 15])
print(the_smallest_number)
