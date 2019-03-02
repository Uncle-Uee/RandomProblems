"""
1. Read the Postfix expression from left to right
2. If the symbol is an operand, then push it onto the Stack
3. If the symbol is an operator, then pop two values from the Stack
4. Create a string by concatenating the value2 then the operator and then the value1.
5. string = "(" + value2 + operator + value1 + ")"
6. And push the resultant string back to Stack
7. Repeat the above steps until end of Prefix expression.
"""

def postfix_to_infix(postfixes = []):
	stack = []
	infix = ""
	infixes = []

	for postfix in postfixes:
		for i in range(0, len(postfix)):

			# Found An Operand
			if str(postfix[i]).isalpha():
				stack.append(postfix[i])

			# Found An Operator
			else:
				# Get 2 Values from the Stack
				value_1 = stack.pop()
				value_2 = stack.pop()

				# Without Brackets
				# infix = value_2 + postfix[i] + value_1
				# With Brackets
				infix = "(" + value_2 + postfix[i] + value_1 + ")"
				stack.append(infix)

		infixes.append(infix)
		infix = ""
		stack.clear()
	return infixes

print(postfix_to_infix(["ab*c+"]))
