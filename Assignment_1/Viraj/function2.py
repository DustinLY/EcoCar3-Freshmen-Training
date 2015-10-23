import math

def sphereVolume():
    radius=raw_input("What is the radius of your sphere?")
	loop=True
	 while loop:
		try:
			 equation=(4/3)*(math.pi)*float(radius)**3
			 print "The volume of your sphere is " +str(equation)+"."
			 loop=False
		 except:
			print "Your response is invalid."
     return
	
sphereVolume()