# This program converts input characters to ASCII values
# Uses built in function ord for string to ascii conversion

user_string = input("Enter string\n");
str_len = len(user_string)


for i in range (str_len):
	v = ord(user_string[i])
	print ("%c ASCII value is  %d" % (user_string[i], v))
