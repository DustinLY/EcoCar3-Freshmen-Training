def cToF():
	loop: True
	while loop:
		try:
			 celcius=float(raw_input("What is the temperature in Celcius?"))
			 temperature=float(celcius*9/5+32)
			 print "The temperature is "+str(temperature)+" degrees Fahrenheit."
		 except:
			print "Your response is invalid."
	 return
	 
cToF()