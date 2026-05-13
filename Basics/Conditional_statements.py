'''#check a number is positive or negitive
a = int(input("Enter a number: "))
if a>=0:
    print("The number is positive")
else:
    print("The number is negative")'''




#Compound conditional statements
'''a = 10
b = 20
c = 30
if a>b and a>c:
    print("a is the greatest")
elif b>a and b>c:
    print("b is the greatest")
else:
    print("c is the greatest")  '''




#even or odd
'''a = int(input("enter a number: "))
if a % 2 ==0:
    print("the number is even")
else:
    print("the number is odd")'''


#minor or major
'''age = int(input("enter your age: "))
if age <18:
    print("you are a minor")
else:
    print("you are not a minor")'''


#eligible to work
'''age = int(input("enter your age: "))
if age >= 18 and age <=60:
    print ("you are eligible to work")
else:
    print("you are not eligible to work")'''


#grade
'''marks = int(input("enter your marks: "))
if marks>=0 and marks<=100:
    if marks>=90:
        print("grade A")
    elif marks>=80:
        print("grade B")
    elif marks>=70:
        print("grade C")
    elif marks>=60:
        print("grade D")
    else:
        print("grade F")
else:
    print("invalid marks")'''



#gender check
'''gender = input("please select your gender m or f: ")
if gender == "m" or gender == "M":
	print("male")
else:
	print("female")'''


#vowel or constant
'''a = input("enter any lower alphabet letter: ")
#if a in ['a','e','i','o','u']:
if a in 'aeiou':
	print('Vowels')
else:
	print('constant')'''


#temperature check
'''temp = float(input('enter temp: '))
if temp == 25:
	print('normal')
elif temp <25:
	print('cold')
else:
	print('hot')'''


#discount on bill amount

'''bill_amount = float(input('enter your bill amount: '))
final_amount = 0
if bill_amount<=1000:
	final_amount = bill_amount - bill_amount*0.10
elif bill_amount>=1000 and bill_amount<5000:
	final_amount = bill_amount - bill_amount*0.15
elif bill_amount>=5000 and bill_amount<10_000:
	final_amount = bill_amount - bill_amount*0.20
elif bill_amount>=10_000:
	final_amount = bill_amount - bill_amount*0.25
	
else:
	print('not eligible to discount')
	
print('final amount to be paid: ',final_amount)'''



#check the day of the week
'''num = int(input("enter a number: "))

if num == 0:
	print('monday')
elif num == 1:
	print('tuesday')
elif num == 2:
	print('wednesday')
elif num == 3:
	print('thursday')
elif num == 4:
	print('friday')
elif num == 5:
	print('saturday')
elif num == 6:
	print('sunday')
else:
	print('invalid')'''


#leap year check
'''year = int(input("enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")'''

#bitwise operator
'''a = 10 & 13
b = 10 | 13
c = 10 ^ 13
d = ~10
e = 10 << 2
f = 10 >> 2
print(a,b,c,d,e,f)'''


#chanining comparisons
'''a = 3
b = 5
c= 7
if a < b < c:
    print("a is less than b and b is less than c")
else:    
    print("the condition is not satisfied")'''



