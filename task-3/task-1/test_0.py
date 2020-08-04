"""Tests the string module through user input check"""

import string_0

def input_string():
	"""Inputs the lists of strings and prints the list of strings."""

	num_of_lists = int(input('Input number of lists: '))
	if num_of_lists < 2:
		raise Exception('Min number of lists = 2')

	# Container list for other lists of strings
	container_list = list()

	# Store strings for each list here
	strings_list = list()

	for each_list in range(num_of_lists):
		num_of_strings_in_list = int(input(f'\nInput number of strings for {each_list + 1}: '))
		if num_of_strings_in_list < 2:
			raise Exception('Min number of strings in a list = 2')
		
		for each_string in range(num_of_strings_in_list):
			string = input(f'Input String for list {each_list + 1}: ')
			strings_list.append(string)
		# After a list of strings is input, add it to the container list, and clear the
		# list variable for further input
		else:
			container_list.append(strings_list[:])
			strings_list.clear()

	print('\nOutput list:')
	print(f'{string_0.string_builder(container_list)}')


"""If this module executed, call input_string()"""
input_string()