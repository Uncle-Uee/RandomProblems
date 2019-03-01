class QuickSort:
	array = []
	size = 0

	def sort(self, array = []):
		if array is None:
			return "Array is Empty"

		self.array = array
		self.size = len(array)
		self.quick_sort(0, self.size - 1)

	def quick_sort(self, low = 0, high = 1):
		"""
		Swap values around based on whether or not they are smaller than the pivot or greater than the pivot
		:param low: Left Most Value.
		:param high: Right Most Value
		"""

		i = low
		j = high

		# Middle Value
		pivot = self.array[low + (high - low) // 2]

		# Divide into 2 Arrays
		while i <= j:
			# All values less than the pivot are placed before it.
			while self.array[i] < pivot:
				i += 1
			# All values greater than the pivot are placed after it.
			while self.array[j] > pivot:
				j -= 1

			if i <= j:
				self.swap(i, j)
				i += 1
				j -= 1

		if low < j:
			self.quick_sort(low, j)

		if i < high:
			self.quick_sort(i, high)

	def swap(self, i = 0, j = 0):
		"""
		Swap Element at Index i with Element at Index j
		:param i: ith Element
		:param j: jth Element
		"""
		temp = self.array[i]
		self.array[i] = self.array[j]
		self.array[j] = temp

array = [6, 5, 3, 1, 8, 7, 2, 4]
quick_sort = QuickSort()
quick_sort.sort(array)
print(array)
