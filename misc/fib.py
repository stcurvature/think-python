#  Generate fibonnaci series

def gen_fib_series(n):
	a, b = 0, 1
	while b < n:
		print(b, end=' ')
		a, b = b, a + b
	print()

n = int(input("enter n: "))

gen_fib_series(n)
