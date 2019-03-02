"""
1. Read the Prefix expression in reverse order (from right to left)
2. If the symbol is an operator, then pop two operands from the Stack
3. Create a string by concatenating the two operands and the operator after them.
4. string = operand1 + operand2 + operator
5. And push the resultant string back to Stack
6. If the symbol is an operand, then push it onto the Stack
7. Repeat the above steps until end of Prefix expression.
"""

def prefix_to_postfix(prefixes):
	# Python Array Act as Stack
	stack = []
	# Post Fix String to Save
	postfix = ""
	# Collection of Post Fixes
	postfixes = []

	# For Each Prefix in the Prefixes Array
	for prefix in prefixes:

		# Get Reverse Order of Characters
		for i in range(len(prefix) - 1, -1, -1):
			# Check for and Operator
			if prefix[i] == "+" or prefix[i] == "-" or prefix[i] == "/" or prefix[i] == "*":
				# Get and Pop the Last Element
				operand_1 = stack.pop()
				# Get and Pop the Last Element
				operand_2 = stack.pop()
				# Concat Operand_1 and Operand_2 and the ith Element of the Prefix
				postfix = operand_1 + operand_2 + prefix[i]
				stack.append(postfix)
			# If no Operator then Add to Stack
			else:
				stack.append(prefix[i])

		# Add Postfix to Postfixes Array
		postfixes.append(postfix)
		# Clear Data
		postfix = ""
		stack.clear()

	# Return Postfixes Array
	return postfixes

# Example
print(prefix_to_postfix(["*+AB-CD"]))
