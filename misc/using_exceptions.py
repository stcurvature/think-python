# Sample program to try exceptions

try:
	top = int(input("Enter numerator:"))
except ValueError: # Catches ValueError exceptions
	print("Not an integer")
	exit(0)

try:
	bottom = int(input("Enter denominator:"))
except:	# Catches any exceptions
	print("Not an integer")
	exit(0)

try:
	if ((top % bottom) == 0):
		print("The numerator is evenly divided by the " + "denominator")
	else:
		print("The fraction is not a whole number")
except	ZeroDivisionError:
	print("The denominator cannot be zero")

