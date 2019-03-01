def find_all_common_elements(array_1 = [], array_2 = [], array_3 = []):
	if len(array_1) == 0 or len(array_2) == 0 or len(array_3) == 0:
		return "Invalid Array Present, Each Array Must have Atleast 1 Element"

	common_elements = []
	for i in array_1:
		if i in array_2 and i in array_3:
			common_elements.append(i)

	print(common_elements)

find_all_common_elements([3, 4, 15, 20, 30, 70, 80, 120], [1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100])
