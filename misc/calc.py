# Calculator

x = float(input("Enter a number:"))
y = float(input("Enter a second number:"))

print("1) Add the two numbers")
print("2) Subtract the two numbers")
print("3) Multiply the two numbers")
print("4) Divide the two numbers")

choice = int(input("Please enter your choice: "))

print("The answer is: ", end="")

if (choice == 1):
	print(x + y)
else:
	if (choice == 2):
		print(x - y)
	else:
		if (choice == 3):
			print(x * y)
		else:
			if (choice == 4):
				print(x/y)
			else:
				print("Invalid choice.")
