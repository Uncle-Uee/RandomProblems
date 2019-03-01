def isAnagram(word_1 = "", word_2 = ""):
	if len(word_1) != len(word_2):
		return False

	word_1_list = list(word_1)
	word_2_list = list(word_2)

	word_1_list.sort()
	word_2_list.sort()

	for i in range(len(word_1)):
		if word_1_list[i] == word_2_list[i]:
			continue
		else:
			return False
	return True


print(isAnagram(input("Enter a Word : ").replace(' ', '').lower(),
                input("Enter another Word : ").replace(' ', '').lower()))
