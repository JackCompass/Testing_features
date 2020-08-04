"""Module provides functionality related to string building and compaction"""

def string_builder(string_lists):
	"""Receives a list of lists, each of which contain several strings. Returns a list, which contains strings
	built from each list
	"""
	# Store built strings here
	strings = list()

	# Make strings and append by using join on each list
	for string_list in string_lists:
		built_string = ' '.join(string_list)
		strings.append(built_string)

	return strings


"""If this module executed, error out"""
if __name__ == '__main__':
	raise Exception('Not a standalone module')