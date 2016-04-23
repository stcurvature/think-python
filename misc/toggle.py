# Toggles caps to small and vice versa
# Uses built in function ord and chr

# toggle 
def toggle(str):
	""" Toggles Caps to Small and Vice versa"""
	if ((str >= 97) and (str <= 122)):
		if (str != 32):
			str = str - 32
	elif ((str >= 65) and (str <= 90)):
		if (str != 32):
			str = str + 32
	return str

# get user string
user_string = input("Enter string \n")

# converted string will be held here
generated_string = ""

# temp variable to store intermediate result
tval = 0

# get string length
str_len = len(user_string)

# Loop through and toggle
for i in range (str_len):
	tval = toggle(ord(user_string[i]))
	generated_string = generated_string +  chr(tval)

# Once complete, print
print (generated_string)

