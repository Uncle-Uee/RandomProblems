"""
Explanation of Fibonacci Recursion Can Be Found Here:
https://medium.com/launch-school/recursive-fibonnaci-method-explained-d82215c5498e
"""

# Use Dictionary for Key Value Pair.
# Key = Nth Term
# Value = Fibonacci Value
fibonacci_cache = {}

def fibonacci(n = 3):
	# Error Check
	if type(n) != int:
		raise TypeError("n Must be an Integer")
	if n < 1:
		raise ValueError("n Must be a Positive Value")

	# If we have cached the value, then return it
	if n in fibonacci_cache:
		return fibonacci_cache[n]

	# Computer Fibonacci Nth Term
	if n == 1:
		value = 0
	elif n == 2:
		value = 1
	elif n > 2:
		value = fibonacci(n - 1) + fibonacci(n - 2)

	# Cache the Value and Return it
	fibonacci_cache[n] = value
	return value

for i in range(1, int(input("Enter a Value: ")) + 1):
	print(i, ":", fibonacci(i))

def Fibonacci(n):
	if (n == 0):
		return 0
	elif (n == 1):
		return 1
	else:
		return Fibonacci(n - 1) + Fibonacci(n - 2)

print(Fibonacci(2))
