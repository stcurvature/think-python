# Converts input characters (caps) to small characters
# This example uses built in function ord and char

user_string = input("Enter string (smaller case, no validation will be done)\n");
generated_string = ""

# Find the length of the input string
str_len = len(user_string)

# Loop through and convert
for i in range (str_len):
	v = ord(user_string[i])
	if ((v >= 65) and (v <= 90)):
		if (v != 32 ):
			v = v + 32
	generated_string = generated_string + chr(v)

# Once complete, print
print (generated_string)
