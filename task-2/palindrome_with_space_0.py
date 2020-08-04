"""Module has function to check palindromic string"""

def is_palindrome(check_string):
	"""Returns true if param is palindrome, after removing all spaces. Case-independent"""
	# Eliminate spaces
	check_string = check_string.replace(' ', '')
	# Ignore case
	check_string = check_string.casefold()
	# [::-1] yields reverse
	if check_string == check_string[::-1]:
		return True
	else:
		return False


if __name__ == '__main__':
	"""If this module executed, provide testing functionality"""
	user_input = input('Input string: ')

	if is_palindrome(user_input):
		print('Palindrome')
	else:
		print('Not Palindrome')