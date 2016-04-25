# This program right justifies the given string for 80 coloumn:w

coloumn_widtn = 80

user_string = input("enter the string : ")
strlen = len(user_string)
offset = coloumn_widtn - strlen;

if (strlen > 80):
	print("string length exceeds 80 coloumn width\n")
else:
	print(" " * offset, user_string)

