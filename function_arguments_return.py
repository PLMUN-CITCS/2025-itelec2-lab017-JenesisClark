# Filename: function_arguments_return.py

# Import the math module
import math

# Define the function to calculate the area of a circle
def circle_area(radius):
    """Calculate and return the area of a circle given its radius."""
    # Calculate the area using the formula: area = π * radius^2
    area = math.pi * (radius ** 2)
    return area  # Return the calculated area

# Call the function and display the result
radius_value = 5  # Define a radius value
area_result = circle_area(radius_value)  # Call the function with radius_value

# Print the result, formatted to 2 decimal places
print(f"The area of a circle with radius {radius_value} is: {area_result:.2f}")