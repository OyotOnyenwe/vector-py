#Vector Addition Calculator

import math

# Input Magnitude

magnitudeA = float(input("What is the magnitude of the first vector? "))
magnitudeB = float(input("What is the magnitude of the second vector? "))
units = str(input("What are the units of magnitude? "))

# Input Angle

angleA = float(input("What is the angle of the first vector in degrees? "))
dirA1 = str(input("What direction? "))
dirA2 = str(input("of? "))
angleB = float(input("What is the angle of the second vector in degrees? "))
dirB1 = str(input("What direction? "))
dirB2 = str(input("of? "))

# Convert to radians

radiansA = math.radians(angleA)
radiansB = math.radians(angleB)

# Find Vx and Vy

Ax = magnitudeA*math.sin(radiansA)
Ay = magnitudeA*math.cos(radiansA)

Bx = magnitudeB*math.cos(radiansB)
By = magnitudeB*math.cos(radiansB)

# Convert direction

if dirA1 == "N":
    Ay = Ay*1
elif dirA1 == "S":
    Ay = Ay*-1
elif dirA1 == "E":
    Ax = Ax*1
elif dirA1 == "W":
    Ax = Ax*-1


if dirA2 == "N":
    Ay = Ay*1
elif dirA2 == "S":
    Ay = Ay*-1
elif dirA2 == "E":
    Ax = Ax*1
elif dirA2 == "W":
    Ax = Ax*-1

if dirB1 == "N":
    By = By*1
elif dirB1 == "S":
    By = By*-1
elif dirB1 == "E":
    Bx = Bx*1
elif dirB1 == "W":
    Bx = Bx*-1


if dirB2 == "N":
    By = By*1
elif dirB2 == "S":
    By = By*-1
elif dirB2 == "E":
    Bx = Bx*1
elif dirB2 == "W":
    Bx = Bx*-1

# Add x and y components

Rx = Ax + Bx
Ry = Ay + By

# Find resultant magnitude

magnitudeR = math.sqrt((Rx**2)+(Ry**2))

# get final direction based on -/+ of resultant 

if Rx >= 0 and Ry >= 0:
    dirR1 = 'N'
    dirR2 = 'E'
elif Rx >= 0 and Ry <=0:
    dirR1 = 'S'
    dirR2 = 'E'
elif Rx <=0 and Ry >=0:
    dirR1 = 'N'
    dirR2 = 'W'
elif Rx <=0 and Ry <=0:
    dirR1 = 'S'
    dirR2 = 'W'

# get angle of the resultant

AngleR = math.degrees(math.atan(Ry/Rx))

# print the results

print('The resultant vector is:', magnitudeR, units, dirR1, 'of', dirR2)
