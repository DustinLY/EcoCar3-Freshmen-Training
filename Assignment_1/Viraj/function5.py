"""
		This function converts Fahrenheit to Celsius using fourmula blah. Please do not input strings or chars. Please 
		enter ints or floats. Thanks peace homie
"""
def fToC():

	loop=True
	while loop:
		try:
			 fahrenheit=float(raw_input("What is the temperature in Fahrenheit? Ex: 14\n"))
			 temperature=float((fahrenheit-32)*5/9)
			 print "The temperature is "+str(temperature)+" degrees Celcius."
			 loop=False
		except:
			print "Your input was invalid"

fToC()
