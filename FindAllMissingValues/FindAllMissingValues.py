def find_missing_values(array = []):
	N = len(array)
	register = [0 for i in range(N)]

	for i in array:
		register[i] = 1

	for i in range(1, N):
		if register[i] == 0:
			print(i)

find_missing_values([1, 1, 2, 3, 5, 5, 7, 9, 9, 9])
