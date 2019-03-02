"""
1. Read the Postfix expression from left to right
2. If the symbol is an operator, then pop two operands from the Stack
3. Create a string by concatenating the two operands and the operator before them.
4. string = operator + operand2 + operand1
5. And push the resultant string back to Stack
6. If the symbol is an operand, then push it onto the Stack
7. Repeat the above steps until end of Prefix expression.
"""

def postfix_to_prefix(postfixes = []):
	stack = []
	prefix = ""
	prefixes = []

	for postfix in postfixes:
		for i in range(0, len(postfix)):

			if postfix[i] == "+" or postfix[i] == "-" or postfix[i] == "*" or postfix[i] == "/":
				operator_1 = stack.pop()
				operator_2 = stack.pop()
				prefix = postfix[i] + operator_2 + operator_1
				stack.append(prefix)
			else:
				stack.append(postfix[i])

		prefixes.append(prefix)
		prefix = ""
		stack.clear()

	return prefixes

# Example
print(postfix_to_prefix(["ABC/-AK/L-*"]))
