

'''print(range(5))
print(list(range(5)))

for i in range(5):
    print(i)

for i in [1,2,3,4,5]:
    print(i)
s = 'hello'
for i in s:
    print(i)'''
    

#sum of N numbers
'''n = int(input("enter a number: "))
sum = 0
for i in range(n + 1):
    sum += i

print("sum of given number", sum)'''



#factorial of a number
'''n = int(input('enter a number: '))
fact = 1
for i in range(1, n+1):
	fact *= i

print("factorial of given number", fact)'''



#fibonacci series
'''n = int(input('enter a number:'))
a = 0
b = 1
for i in range(2, n+1):
	
	c = a+b
	a = b
	b = c
print('fib(',i,') is ',c)'''


#factors of a number
'''
n = int(input('enter a number: '))
factors = []
for i in range(1, n+1):
    if (n % i == 0):
        factors.append(i)
print(f"The factors of {n} are: {factors}")'''



#prime number check
'''n = int(input('enter a number: '))
count =0
for i in range(1,n+1):
	if (n % i ==0):
	    count += 1
if count == 2:
	print('prime')
else:
	print('not prime')'''
 
 
 #break statement
for i in range(1, 11):
    if i == 5:
        break
    print(i)
print('loop ended')

#continue statement
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
print('loop ended')

#pass statement- used as a placeholder when we don't want to write any code in a block but the syntax requires it. It does nothing and is ignored by the interpreter.
for i in range(1, 11):
    pass
print('loop ended')


#else suite in for loop
for i in range(1, 11):
    if i == 5:
        break
    print(i)
else:
    print('loop ended because of else suite statement')

print('loop ended beacuse of break statement')   

  

