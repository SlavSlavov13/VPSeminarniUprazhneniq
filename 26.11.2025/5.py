import math

def fits_in_circle(width, height, radius):
	diagonal = math.sqrt(width**2 + height**2)

	diameter = 2 * radius

	return diagonal <= diameter

w, h, r = 3, 4, 3
print(f"Побира ли се? {fits_in_circle(w, h, r)}")