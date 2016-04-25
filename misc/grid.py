# Program to print grid as shown below
# 
# +----+----+
# |    |    |
# |    |    |
# +----+----+
# |    |    |
# |    |    |
# +----+----+


element_seperator = 4

def	print_border_line():
	print("+", "-" * element_seperator, "+", "-" * element_seperator, "+")

def	print_inline():
	print("|", " " * element_seperator, "|", " " * element_seperator, "|")

def print_block():
	print_border_line()
	print_inline()
	print_inline()
	print_inline()
	print_border_line()

def	print_lower_block():
	print_inline()
	print_inline()
	print_inline()
	print_border_line()


def	print_grid():
	print_block()
	print_lower_block()
	print_lower_block()

print_grid()
