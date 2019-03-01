def reverse_array(array = []):
	if len(array) == 0:
		return array

	else:
		return array[::-1]

integers = [1, 1, 2, 3, 5, 5, 7, 9, 9, 9]
print(reverse_array(integers))

strings = ["f", "e", "d", "c", "b", "a"]
print(reverse_array(strings))
