
#while loop

'''n = int(input("enter a number: "))
i = 0
while i < 10:
	i += 1
	print(n, "x", i, "=", n*i)'''


'''n = int(input("enter any bigger digit: "))
while n>0:
	
	r = n % 10
	print('n =',n ,'r =', r)
	n = n // 10'''


#number of digits in a number
'''n = int(input('enter a number:'))
i = 0
while n>0:
	n = n // 10
	i +=1
	
print('number of digits:', i)'''


#sum of digits in a number
'''n = int(input('enter a number:'))
sum = 0
while n>0:
	r = n % 10
	sum += r
	n = n // 10
print('sum of digits:', sum)'''



#reverse of a number
'''n = int(input('enter a number:'))
rev = 0
while n>0:
	r = n % 10
	rev = rev * 10 + r
	n = n // 10
    
	
print('reverse of a given number: ', rev)'''



#palindrome check
'''n = int(input('enter a number:'))
i = n
rev = 0
while i>0:
	r = i % 10
	rev = rev * 10 + r
	i = i // 10
print('reverse of a num :',rev)    
if rev == n:	
	print('its palindrome')
else:
	print('not a palindrome')'''


#sum of N numbers
'''n = int(input('enter a number to calculate sum of those N numbers: '))
i = 0
sum =0

while(i<n):
	i +=1
	sum += i
print(sum)'''


#sum of N numbers
'''n = 5
i = 0
sum =0
print('enter a number to calculate sum of those N numbers: ', n)
while(i<n):
	i +=1
	x = int(input(""))
	sum += x
print(sum)'''


#max and min of N numbers
'''n = 5
i = 0
# Professional initialization - great job!
max_val = float('-inf') 
min_val = float('inf') 

print('Enter a list of', n, 'numbers:')
while i < n:
    x = int(input(""))
    if x > max_val:
        max_val = x
    
    # Use 'if' instead of 'elif' so the first number 
    # can be BOTH the max and the min
    if x < min_val:
        min_val = x
    
    i += 1

print('max value is:', max_val)
print('min value is:', min_val)'''




#break
'''i = 0
while i < 5:
    i += 1
    if i == 3:
        break
    print(i)
print('loop ended')	

#continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
print('loop ended')'''



#else with while loop
i = 0
while i < 5:
    i += 1
    if i == 8:
        break
    print(i)
else:
	print('loop ended without break')
     
print('loop ended')

