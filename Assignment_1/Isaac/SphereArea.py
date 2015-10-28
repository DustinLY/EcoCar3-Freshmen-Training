import math

def areaSphere():
	radius = raw_input("What is the radius of the sphere?")
	length = float(radius) 
	equation = 4 * (math.pi) * float(length)**2
	print "The area of the sphere is " + str(equation) + "." 
	
areaSphere()

