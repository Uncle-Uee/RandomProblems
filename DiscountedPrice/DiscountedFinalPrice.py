def final_price(prices = []):
	amount = 0
	non_discount = []

	for i in range(0, len(prices)):
		for j in range(i + 1, len(prices)):
			if prices[j] <= prices[i]:
				amount += prices[i] - prices[j]
				break

			if prices[j] > prices[i]:
				continue
		if prices[j] > prices[i]:
			amount += prices[i]
			non_discount.append(i)

	amount += prices[-1]
	non_discount.append(len(prices) - 1)
	print(amount)
	for i in non_discount:
		print(i, end = " ")
