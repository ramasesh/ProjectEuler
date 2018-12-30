import numpy as np
from fractions import gcd

def lattice_points_inside(a,b):
    """returns the number of lattice points between the x-axis, y-axis, and the line defined by (a,0) and (0,b), NOT including any points on the x-axis or y-axis, or on the hypotenuse"""

    # imagine the rectangle (0,0), (a,0), (0,b), (a,b)
    # this strictly contains (a-2)*(b-2) lattice points

    # how many are on the diagonal?  
    # gcd(a,b) - 1?

    return 0.5*((a-1)*(b-1) - gcd(a,b) + 1)

def lattice_points_inside(a,b,c,d):
    """returns the number of lattice points inside the quadrilateral a,b,c,d"""
    return a + b + c + d - 1 + 0.5*((a - 1)*(b - 1) + (b-1)*(c - 1)+ (c -1)*(d - 1) + (d - 1)*(a - 1)) - 0.5*(gcd(a,b) + gcd(b,c) + gcd(c,d) + gcd(d,a))
