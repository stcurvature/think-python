# Calcualte the volume of sphere for the given radius
# Volume = 4/3 * pi * (r)^3

import math

def volume_of_sphere(radius):
	""" Calculate volume of sphere"""
	volume = 4.0/3.0 * (math.pi) * (radius**3)
	print("Volume of sphere with radius %.3f is %.3f units" % (radius, volume))
	return

radius = float(input("Enter radius\n"))
volume_of_sphere(radius)
