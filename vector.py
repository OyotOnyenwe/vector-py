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

# Convert Angle to a value between 0 and 360

if dirA1 == "N" and dirA2 == "E":
    trueangleA = 90-angleA
elif dirA1 == "N" and dirA2 == "W":
    trueangleA = 270+angleA
elif dirA1 == "S" and dirA2 == "E":
    trueangleA = 90+angleA
elif dirA1 == "S" and dirA2 == "W":
    trueangleA = 270-angleA
elif dirA1 == "E" and dirA2 == "N":
    trueangleA = 0+angleA
elif dirA1 == "E" and dirA2 == "S":
    trueangleA = 180-angleA
elif dirA1 == "W" and dirA2 == "N":
    trueangleA = 360-angleA
elif dirA1 == "W" and dirA2 == "S":
    trueangleA = 180+angleA

if dirB1 == "N" and dirB2 == "E":
    trueangleB = 90-angleB
elif dirB1 == "N" and dirB2 == "W":
    trueangleB = 270+angleB
elif dirB1 == "S" and dirB2 == "E":
    trueangleB = 90+angleB
elif dirB1 == "S" and dirB2 == "W":
    trueangleB = 270-angleB
elif dirB1 == "E" and dirB2 == "N":
    trueangleB = 0+angleB
elif dirB1 == "E" and dirB2 == "S":
    trueangleB = 180-angleB
elif dirB1 == "W" and dirB2 == "N":
    trueangleB = 360-angleB
elif dirB1 == "W" and dirB2 == "S":
    trueangleB = 180+angleB
    
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

AngleR = math.degrees(math.atan(Ry/Rx))

print('The resultant vector is:', magnitudeR, units, dirR1, 'of', dirR2)
