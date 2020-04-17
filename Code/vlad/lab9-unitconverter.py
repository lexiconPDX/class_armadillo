#Lab 9: Unit Converter Version # 4
""" This lab will involve writing a program that allows the user to convert a number between units.

Version 1
Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m
Version 2
Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m 

Version 3
Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m
Version 4
Now we'll ask the user for the distance, the starting units, and the units to convert to.

You can think of the values for the conversions as elements in a matrix, where the rows will be the units you're converting from, and the columns will be the units you're converting to. Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).

ft	mi	m	km
ft	1		0.3048	
mi		1	1609.34	
m	1/0.3048	1/1609.34	1	1/1000
km			1000	1
But instead of filling out that matrix, and checking for each pair of units (if from_units == 'mi' and to_units == 'km'), we can just convert any unit to meters, then convert the distance in meters to any other unit.

Furthermore you can convert them from meters by dividing a distance (in meters) by those same values used above. So first convert from the input units to meters, then convert from meters to the output units.

Below is some sample input/output:

> what is the distance? 100
> what are the input units? ft
> what are the output units? mi
100 ft is 0.0189394 mi
distance in miles to the moom 238,900
"""

units = {
    'ft': .3048,
    'm': 1,
    'mi': 1609.34,
    'km': 1000,
    'yd':  0.9144,
    'in': 0.0254,

}


num = int(input("Please enter a number to convert: "))
c_unit = input("Would you please enter the unit to convert from: ")
b_unit = input("Please enter the unit to convert to")

product = num * units[c_unit]
product2 = product / units[b_unit]
result = f'{num} {c_unit} is equal to {product2} {b_unit} '
print(result)




   