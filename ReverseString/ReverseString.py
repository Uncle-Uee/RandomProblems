def reverse_string(word = ""):
	return word[::-1]

def reverse_string_recursion(word = ""):
	if len(word) == 0:
		return word
	return reverse_string_recursion(word[1:]) + word[0]

print(reverse_string(input("Enter a Word: ")))
print(reverse_string_recursion(input("Enter a Word: ")))
