from random import randint

def FindMissingNumber(n = 0, array = list()):
	"""
	Find the Missing Number in a List.
	:param n: The Range of the Numbers in the List.
	:param array: The List of Numbers.
	:return: The Missing Number of the List.
	"""
	total = sum(array)
	series = 0
	for i in range(1, n + 1):
		series += i
	return "Missing Value : " + str(series - total)

n = abs(int(input("Enter a Value: ")))
array = list((i for i in range(1, n + 1)))
array.pop(randint(0, n - 1))

print(array)
print(FindMissingNumber(n, array))
