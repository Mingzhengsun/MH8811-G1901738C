import json

def serialization(data_structure):
    data_type = type(data_structure)
    
    #dictionary
    if data_type is dict:
        res = "dictionaries|"
        for i in data_structure:
	#key values type   remember data_structure[i] to get values		
            res = res + str(i)
            res = res + ":"
            res = res + str(data_structure[i])
            res = res + ","
            res = res + str(type(data_structure[i]))
            res = res + "|"
        return res[:-1]
        
    # list
    elif data_type is list:
        res = "list|"
        for i in data_structure:
	#values type
            res = res + str(i)
            res = res + ","
            res = res + str(type(i))
            res = res + "|"
        return res[:-1]
        

def deserialization(i):
	# step 1 type
	list_of_str = i.split("|")
	data_type = list_of_str[0]
	list_of_str = list_of_str[1:]
    # step 2 dictionaries
	if data_type == 'dictionaries':
		res = dict()
		for i in list_of_str:
			split1 = i.split(":")
			key = split1[0]
			other= split1[1]
			other1 = other.split(",")
			value = other1[0]
			value_type = other1[1]
            # key : value, type
			if value_type == "<class 'str'>":
				res[key] = str(value)
			elif value_type == "<class 'int'>":
				res[key] = int(value)
			else:
				res[key] = float(value)
		return res
 
     # step 3 list
	elif data_type == 'list':
		res = list()
		for i in list_of_str:
			split2 = i.split(",")
			value = split2[0]
			value_type = split2[1]
            # value, type
			if value_type == "<class 'str'>":
				res.append(str(value))
			elif value_type == "<class 'int'>":
				res.append(int(value))
			else: 
				res.append(float(value))
		return res

def my_compare(ds1, ds2):
	if type(ds1) is not type(ds2):
		return "Wrong"
	else: 
		if isinstance(ds1, list):
			if ds1 == ds2:
				return "True"
			else:
				return "Wrong"
		if isinstance(ds1, dict):
			if ds1 == ds2:
				return "True"
			else:
				return "Wrong"



# ask user for a path to the json file
path1 = input("Please enter the path of the json file ")

# load the data structure from the json file

data_file = open(path1)
data1 = json.load(data_file)
data_file.close()


# convert the original data structure into a string using serializer
string1 = serialization(data1)

# write the string to a file
# w for write,Don't forget to close the file
file_name = input("Please input the file name to store the data structure: ")
file1 = open(file_name, 'w')
file1.write(string1)
file1.close()

# Read the string back from the file. Close the file afterwards
file2 = open(file_name, 'r')
string2 = file2.read()
file2.close()

# Pass it to your deserialization function, which would return a restored data structure
deserialization_data= deserialization(string2)

# Compare the two data structures
print(my_compare(deserialization_data, data1))
print(deserialization_data)
print(data1)
