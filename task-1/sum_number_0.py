"""Module provides code for printing sum of all integers of a list without using sum()"""

if  __name__ == "__main__":

	list_size = int(input('Input list size: '))

	# Is it really necessary to use a list here?

	sum_elements = 0

	for i in range(list_size):
		try:
			element = int(input('Input element: '))
			sum_elements += element
		except:
			raise Exception('An Error occured!')

	print(f'Sum: {sum_elements}')