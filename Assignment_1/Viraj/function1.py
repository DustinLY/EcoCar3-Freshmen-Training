import math

def sphereArea():
	loop=True
	while loop:
		radius=raw_input("What is the radius of your sphere?")
		'''equation=4*(math.pi)*(float(radius)**2)
		print "The area of your sphere is "+ str(equation)+"."'''
		try:
			equation=4*(math.pi)*float(radius)**2
			print "The area of your sphere is "+ str(equation)+"."
			loop=False
		except:
			print "Your response is invalid." 


sphereArea()
