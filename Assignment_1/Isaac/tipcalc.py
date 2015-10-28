def tipcalc():
	price = raw_input("How much did you pay?")
	equation = float(price) + float(price) * 0.09
	print "Your total will be " + str(equation) +"."
	
tipcalc()