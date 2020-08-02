def is_integer(str):
	'''
	This function compares every character of the string with the integer list.
	return True when all character are number else return False.
	'''
	integer = [0,1,2,3,4,5,6,7,8,9,"+","-"]
	for x in range(0, len(str)):
		if str[x] not in integer:
			return False
	return True

	
if __name__ == "__main__":
	raise Exception("This is not a standalone module. Please import to use.")