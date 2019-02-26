def Fibonacci(n = 3):
	fib_sequence = [0, 1]

	if n < 2:
		return fib_sequence

	for i in range(n - 2):
		fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
	return fib_sequence
