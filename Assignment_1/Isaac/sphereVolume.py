import math

def sphereVolume():
	radius = raw_input("Enter the value of the radius")
	try: 
		equation = 4/3 * math.pi * float(radius)
		print "The volume of the sphere is " + str(equation) + "."
	except:
		print"You entered an invalid number!"
		
sphereVolume()