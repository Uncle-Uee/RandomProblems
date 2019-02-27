fizz = "Fizz"
buzz = "Buzz"


def mod_calculation(i = 1, modby = 1):
	"""
	Calculate the Modulus of the Value i.
	:param i: Value to calculate the Modulus of.
	:param modby: The Modulus Value.
	:return:
	"""
	return i % modby


def fizzbuzz_iterative(array = list()):
	for i in array:
		mod3 = mod_calculation(i, 3) == 0
		mod5 = mod_calculation(i, 5) == 0

		if mod3 and mod5:
			print(fizz + " " + buzz)
		elif mod3:
			print(fizz)
		elif mod5:
			print(buzz)
		else:
			print(i)


def fizzbuzz_recursion(array = list()):
	if len(array) == 0:
		return

	mod3 = mod_calculation(array[0], 3) == 0
	mod5 = mod_calculation(array[0], 5) == 0

	if mod3 and mod5:
		print(fizz + " " + buzz)
	elif mod3:
		print(fizz)
	elif mod5:
		print(buzz)
	else:
		print(array[0])

	fizzbuzz_recursion(array[1:])


numbers = list((i for i in range(1, abs(int(input("Enter a Value: "))) + 1)))
print("Fizz Buzz Iterative Example")
fizzbuzz_iterative(numbers)
print("\nFizz Buzz Recursive Example")
fizzbuzz_recursion(numbers)
