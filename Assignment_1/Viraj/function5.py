def fToC():
	loop=True
	while loop:
		try:
			 fahrenheit=float(raw_input("What is the temperature in Fahrenheit?"))
			 temperature=float((fahrenheit-32)*5/9)
			 print "The temperature is "+str(temperature)+" degrees Celcius."
			 loop=False
		except:
			print "Your input was invalid"
	 return

fToC()