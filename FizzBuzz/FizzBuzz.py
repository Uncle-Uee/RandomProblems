def FizzBuzz(array = list()):
	for i in array:
		mod3 = i % 3 == 0
		mod5 = i % 5 == 0
		if mod3 and mod5:
			print("fizz buzz")
		elif mod3:
			print("fuzz")
		elif mod5:
			print("buzz")
		else:
			print(i)

#added this in case the modCalculation ever needs to change
def ModCalculation(i, a):               
        return (i%a)

def FizzBuzz_Recursion(array = list()):
	if len(array) == 0:
		return

	mod3 = ModCalculation(array[0], 3) == 0
	mod5 = ModCalculation(array[0], 5) == 0
	#by making these values variable they can be changed once and it will change throughout the program
	fizz = "Fizz"
	buzz = "Buzz"

	if mod3 and mod5:
		print(fizz + " " + buzz)
	elif mod3:
		print(fizz)
	elif mod5:
		print(buzz)
	else:
		print(array[0])

	FizzBuzz_Recursion(array[1:])

FizzBuzz(list((i for i in range(1, abs(int(input("Enter a Value: "))) + 1))))
