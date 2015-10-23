def tipCalculator():
	loop=True
	while loop:
		price=raw_input("What was the price of the bill?")
		try:
			total=float(price)*.09+float(price)
			print "The total price is $"+str(total)+" with 9% included."
			loop=False
		except:
			print "Your response was invalid."
	return
tipCalculator()