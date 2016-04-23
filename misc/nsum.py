# This program calculates the sum of n positive integers computed by the formula
# sum(1...100) = 1 + 2 + ...+ n = (n)(n+1)/2

n = int(input("Enter the range n\n"))
sum = ((n) * (n + 1))/2

print("Sum (1...%d) is %d\n" % (n,sum))
