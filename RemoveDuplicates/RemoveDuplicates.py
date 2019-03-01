def remove_duplicates_set(array = []):
	return set(array)


def remove_duplicates_manual(array = []):
	if len(array) == 0:
		return "Empty Array"

	no_duplicates = []
	no_duplicates.append(array[0])

	for i in array:
		if i not in no_duplicates:
			no_duplicates.append(i)

	return no_duplicates

duplicates = [1, 1, 2, 2, 3, 4, 5]

print(remove_duplicates_manual(duplicates))