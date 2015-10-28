import math

def areaSphere():
	radius = raw_input("What is the radius of the sphere?")
	if float(radius) != float:
		print "That is not a number!"
	else:
		equation = 4 * (math.pi) * float(radius)**2
		print "The area of the sphere is "+ str(equation) +"."
	
areaSphere()