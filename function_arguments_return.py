# Filename: function_arguments_return.py

#Import the math module
import math
#Define the function
def circle_area(radius):
#Add a docstring
def circle_area(radius):
    """Calculate and return the area of a circle given its radius."""
	#Calculate the area
	    area = math.pi * (radius ** 2)
		#Return the calculated area
		    return area
			#Call the function and display the result
			radius_value = 5
area_result = circle_area(radius_value)

print(f"The area of a circle with radius {radius_value} is: {area_result:.2f}")
