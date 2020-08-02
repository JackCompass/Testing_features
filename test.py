import integer

if __name__ == "__main__":
	user_text = input("Enter text : ")
	if integer.is_integer(user_text):
		print("Integer")
	else:
		print("Not Integer")