# Find the Different Pairs of Values when Added together they Equal the Value K.
def find_pairs(k = 0, array = []):
	if len(array) == 0:
		return "Empty Array"

	for i in range(len(array)):
		first = array[i]
		for j in range(i + 1, len(array)):
			second = array[j]
			if first + second == k:
				print("Pair Found : {" + str(first) + ", " + str(second) + "}")

find_pairs(7, [2, 4, 3, 5, 6, -2, 4, 7, 8, 9])
