# Python Program to find Volume and Surface Area of a Cube

l = float(input('Please Enter the Length of any Side of a Cube: '))

sa = 6 * (l * l)
Volume = l * l * l
LSA = 4 * (l * l)

print("\n Surface Area of Cube = %.2f" %sa)
print(" Volume of cube = %.2f" %Volume)
print(" Lateral Surface Area of Cube = %.2f" %LSA)