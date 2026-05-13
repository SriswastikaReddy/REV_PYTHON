import math

'''#variable declarations
a=10
x,y,z =10,20,30
c=d=e=10
print(x,y,z)
print(a)
print(c,d,e)
print(id(a),id(x),id(y),id(z),id(c),id(d),id(e))'''

'''#casting
x = str(3)
y = int(3)
z = float(3)
x = 5.8

print(x)
print(y)
print(z)
print(type(x))'''

'''#unpacking
fruits = ["apple","banana","cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)'''

'''#global variables
x = "awesome"
def myfunc():
    x = "fantastic"
    print("python is " + x)
myfunc()   
print("python is " + x) 

def fun1():
    global a
    a = "sri"
    print(a)
fun1()
print(a)'''


'''#isinstance() function to check if an object was built from a specific blueprint
a = "Hello"

if isinstance(a, str):
    print(a.lower()) # We only call .lower() because we are sure it's a string!

x = 20
if isinstance(x, int):
    print(x + 10) # We only add 10 because we are sure it's an integer!'''






'''#Base conversion functions
x = 10
s1 = bin(x) # Convert to binary
s2 = oct(x) # Convert to octal
s3 = hex(x) # Convert to hexadecimal
print(s1)
print(s2) 
print(s3)
print(type(s1),type(s2),type(s3)) '''








'''#Type conversion functions
x = 10
s1 = str(x) # Convert to string     
s2 = float(x) # Convert to float
s3 = complex(x) # Convert to complex
s4 = bool(x) # Convert to boolean
print(s1)
print(s2)
print(s3)
print(s4)
print(type(s1),type(s2),type(s3),type(s4))  

y = '10'
s5 = int(y) # Convert to integer
s6 = float(y) # Convert to float
s7 = complex(y) # Convert to complex
s8 = bool(y) # Convert to boolean
print(s5)
print(s6)
print(s7)
print(s8)
print(type(s5),type(s6),type(s7),type(s8))'''



'''#Arithmetic operators
x = 10
y = 3
print(x + y) # Addition
print(x - y) # Subtraction  
print(x * y) # Multiplication
print(x / y) # floatDivision
print(x % y) # Modulus
print(x ** y) # Exponentiation
print(x // y) # Floor division'''



#Expressions
'''#Program to find the area of a rectangle
l = int(input("enter the length of a rectangle:"))
b = int(input("enter the breadth of a rectangle:"))
area = l * b
print("area of a rectangle:", area)'''


#Challenges using expressions

#area of a circle
'''r = int(input("enter the radius of a circle:"))
pi = 3.14
area = pi * r * r
print("area of a circle:", area)'''

#area of a triangle
'''a = int(input("enter the base of a triangle:"))
h = int(input("enter the height of a triangle:"))
area = 0.5 * a * h
print("area of a triangle:", area)'''

#area of a trapezium
'''a = int(input("enter the length of the first parallel side of a trapezium:"))
b = int(input("enter the length of the second parallel side of a trapezium:"))
h = int(input("enter the height of a trapezium:"))
area = 0.5 * (a + b) * h
print("area of a trapezium:", area)'''

#km to miles 
'''mile = 0.621371
km = int(input("enter the distance in km:"))
miles = km * mile
print("distance in miles:", miles)'''


#displacement
'''u = int(input("enter the initial velocity:"))
v = int(input("enter the final velocity:")) 
t = int(input("enter the time taken:"))
s = ((u + v) / 2) * t
print("displacement:", s)'''

#Syrface area of a cuboid
'''l = int(input("enter the length of a cuboid:"))
b = int(input("enter the breadth of a cuboid:"))
h = int(input("enter the height of a cuboid:"))
sa = 2 * (l * b + b * h + l * h)
print("surface area of a cuboid:", sa)'''


a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))

x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

print("the roots of the quadratic equation are:", x1, "and", x2)