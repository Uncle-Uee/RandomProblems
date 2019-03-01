def merge_strings(a, b):
	size = len(a) if len(a) < len(b) else len(b)

	merge_string = ""
	for i in range(size):
		merge_string += a[i] + b[i]

	if size < len(b):
		merge_string += b[size:]

	elif size < len(a):
		merge_string += a[size:]

	return merge_string

print(merge_strings("abcjklmnop", "defghi"))
