# Created by : Nikita Tiwari

# Python program to check if
# given number is prime or not
def is_prime(num = 0):
	# If given number is greater than 1
	if num > 1:

		# Iterate from 2 to n / 2
		for i in range(2, num // 2):

			# If num is divisible by any number between
			# 2 and n / 2, it is not prime
			if (num % i) == 0:
				print(num, "is not a prime number")
				break
		else:
			print(num, "is a prime number")

	else:
		print(num, "is not a prime number")

def is_prime_optimized(num = 0):
	# Corner cases
	if num <= 1:
		return False
	if num <= 3:
		return True

	# This is checked so that we can skip
	# middle five numbers in below loop
	if num % 2 == 0 or num % 3 == 0:
		return False

	i = 5
	while i * i <= num:
		if num % i == 0 or num % (i + 2) == 0:
			return False
		i = i + 6

	return True
