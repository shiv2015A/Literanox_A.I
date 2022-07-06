Perimeter = s1 + s2 + s3
Area = √(s*(s-s1)*(s-s2)*(s-s3))

where s = (s1 + s2 + s3)/2 

#1
s1 = float(input("Enter the first side of the triangle : "))
s2 = float(input("Enter the second side of the triangle : "))
s3 = float(input("Enter the third side of the triangle : "))

#2
p = (s1 + s2 + s3)

#3
s = p/2

#4
area = (s * (s-s1) * (s-s2)*(s-s3))**0.5

#5
print("The perimeter of the triangle is : {0:.2f}".format(p))
print("The area of the triangle is : {0:.2f}".format(area))

input()