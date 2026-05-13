'''for i in range(1, 6):
    for j in range(1, 4):
        print(i, j, end=' ')
    print()'''
    


'''#prime numbers from 0 to n
n = 100
prime_list = []
for i in range(1,n+1):
	count = 0
	for j in range(1,i+1):
		if(i %j ==0):
			count += 1
	if count ==2:
		prime_list.append(i)
print(f"list of prime numbers from 0 1 to {n} = {prime_list}")'''



'''r = int(input("enter number of rows :"))
c = int(input("enter number of columns :"))

for i in range(1,r+1):
	for j in range(1,c+1):
		print(' * ', end=' ')
	print()'''
 
 
 
'''r = int(input("enter number of rows :"))
c = int(input("enter number of columns :"))

for i in range(1,r+1):
	for j in range(1,i+1):
		print(' ? ', end=' ')
	print()'''
 
 
 
 
'''r = int(input("enter number of rows :"))
c = int(input("enter number of columns :"))

for i in range(1,r+1):
	for j in range(1,(c+1)-(i-1)):
		print(' * ', end=' ')
	print()'''
 
 
'''r = int(input("enter number of rows :"))
c = int(input("enter number of columns :")) 
for i in range(1, r+1):
    print('*' * (c-i), end=' ')
    print()'''
    


'''n = 5

# 'i' represents the row (1 to 5)
for i in range(1, n + 1):
    
    # 'j' represents the column (1 to 5)
    for j in range(1, n + 1):
        if j >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ") # Print space for the empty boxes
            
    print() # Move to the next line after each row is done'''
    

#check the day of the week
#match case statement
'''num = int(input("enter a number: "))
match num:
	case 0:
		print('monday')
	case 1:
		print('tuesday')
	case 2:
		print('wednesday')
	case 3:
        print('thursday')
	case 4:
        print('friday')
	case 5:
        print('saturday')
	case 6:
        print('sunday')
	case _:
        print('invalid')'''
        
        


 