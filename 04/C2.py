#C2

#Min function
def mymin(lst):
	the_smallest_number= None
	for num in lst:
		if the_smallest_number is None:
			the_smallest_number=num
		else:
			if the_smallest_number> num:
				the_smallest_number= num
	return(the_smallest_number)

#Max function
def mymax(lst):
	the_max_number=None
	for number_2 in lst:
		if the_max_number is None:
			the_max_number=number_2
		elif the_max_number<number_2:
			the_max_number=number_2
	return(the_max_number)

#Average function
def myaverage(lst):
	count1=0
	sum1=0
	for number_3 in lst:
		count1=count1+1
		sum1=sum1+number_3
	average1=sum1/count1
	return(average1)


#Median function
def mymedian(lst):
	lst.sort()	
	r=int(len(lst)/2)
	if (len(lst) % 2) == 0:
		median1=((lst[r-1])+(lst[r]))/2
	else:
		median1=lst[r]	
	return(median1)


#Range Function
def myrange(lst):
	return(mymax(lst)-mymin(lst))

lst=[9, 41, 12, 3, 74, 15]
print('The list is:',lst)
print('The minimum number of this dataset is ',mymin(lst))
print('The maximum number of this dataset is ',mymax(lst))
print('The average number of this dataset is ',myaverage(lst))
print('The median number of this dataset is ',mymedian(lst))
print('The range of this dataset is ',myrange(lst))


