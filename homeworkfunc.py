# Task 1


# def calc(x,y):
    
#     operation = input("type +,-,*,/:  ")
#     if operation == "+" :
#         print (x+y)
#     elif operation == "-" :
#         print (x-y)
#     elif operation == "*" :
#         print (x*y)
#     elif operation == "/" :
#         print (x/y)
#     else:
#         print("Uknown operation")

# calc(20,5)



# Task 2


def deposit ():
    n= int(input ("Type amount of money: "))
    years= int(input ("On how many years: "))

    # for i in range (0,years):
    money = n*((1+(0.01*1.1))** years)
    print (money)

deposit()


#Task 3


#Task 4
# import random


# num = random.randint(1, 10)

# def is_prime(num) :

#     if num == 1:
#         print(num, "False")
#     elif num > 1:
    
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"False")
#                 break
#     else:
#         print(num,"True")
# is_prime(num)

#Task 5 


# def CheckLeap(year):


#  if((year % 400 == 0) or  
#      (year % 100 != 0) and  
#      (year % 4 == 0)):    
#     print("True")
#  else:  
#     print ("False") 
# year = int(input("Enter the number: ")) 
# CheckLeap(year)   


