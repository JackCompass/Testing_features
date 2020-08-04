"""This module provides functionality to check whether
given string is intger or not
"""

def is_integer(string):
	"""Returns true if param string is integer.

	Also handles '+' and '-' prefixes
	"""
	if string[0] == '+' or string[0] == '-':
		string = string.lstrip('+-')

	for digit in string:
		if ord(digit) >= 48 and ord(digit) <= 57:
			continue
		else:
			return False
	else:
		return True


"""If this module executed, raise error"""
if __name__ == '__main__':
	raise Exception('Not Standalone Module')
