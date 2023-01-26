#Task 1
# import random


# number = random.randint(1, 100)

# guess_count = 0

# guess_limit = 9     

# while guess_count <= guess_limit :
    
#     guess = int(input("Guess the number: "))

#     guess_count += 1
#     if guess > number:
#         print("Less")
#     elif guess < number:
#         print("More")
#     elif guess == number:

#         print("Number was" , number ,"you guessed it in ", guess_count,"Guesses")

#         break
    
# else:

#     print ("You failed, the correct number is", number)
# input()






# Task 2

# count = 0
# number_count = 0
# while number_count <= 10 :
#     number = int(input("Type 10 numbers: "))
#     number_count += 1
    
    
#     if number % 5 == 0:
#         count += 1
#         continue
    
# if number <= 2:
#         print("Number must be gretater than 2! Try again")

# print (str(count)  + " of your numbers multiples of 5")        











#Task 3




# a = 0
# b = 1
# while a <= 8:
#     a += 1 
#     c = a*b
#     print (str(a) + "*" + str(b) + "=" + str(c))
#     b = 0
#     while b <= 8:
#         b += 1 
#         c = a*b
#         print (str(a) + "*" + str(b) + "=" + str(c))
#     print()

# for a in range (1, 10):
#     print('')
#     for b in range (2, 10):
#         print(a, '*', b, '=', a*b)





#Task 4

# for x in range (0,6):
#     print ("*" + (x)* "." + "*")



#Task 5 

# import math


# p = 59
# h = 205




# for i in range (999) :
#     numbers= int(input("Type your numbers(type '0' if you finished) : "))
    
    
#     hmore = 1

#     for x in (0,p): 
        
#         x=+ numbers

#     for o in (h,9999999):
#        math.prod(numbers)

#     for u in (p,h):
        
#         u+= 1

#     if numbers == 0 :
#         print ("Result - " + str(u)  + " numbers between P and H, " + str(x) +" -sum of numbers less than P")
#         break     



# Task 6 
x = 1

while x == 1:
    numbers = int(input("Type your numbers(type '0' if you finished) : "))
    plus = 0
    while numbers > 0:
        plus =+ 1
    
    minus= 0
    while numbers < 0:
        minus =+ 1

    if numbers == 0 :
        print ("result- " + plus/(plus+minus)*100 +"% of positive numbers" + minus/(plus+minus)*100 +"% of negative numbers")
        break


























