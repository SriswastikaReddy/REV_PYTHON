# Exercise 1: Write a program that takes a number as input and prints all the even numbers from 1 to that number.
'''n = int(input("enter a number: "))
even = []
odd = []
for i in range(1,n+1):
	if i%2 ==0:
		even.append(i)
	else:
		odd.append(i)

print('even numbers:',even)
print(f'odd numbers: {odd}')'''



#Guess the number game
'''print("Welcome! Guess the number between 1 and 10.")
while(True):
	n = int(input("Enter your guess: "))
	if n == 7:
		break
    
	print("try again")

print('you are correct')'''


#multiplication table
'''n = int(input('enter a number of table you want to print:'))

for i in range(1, 11):
	c = n * i
	print(n ,'x',i, '=' ,c)

n = int(input('enter a number of table you want to print:'))
i = 1
while(i <=10):
	print(f'{n} x {i} = {n*i}')
	i+= 1	'''
 
 

#sum of N random numbers using while loop
'''total = 0
n = 1
while(n != 0):
    n = int(input("enter next number to sum:"))
    total += n
print('total sum is :', total)'''


