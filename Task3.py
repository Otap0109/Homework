#ввести число
number = input("Type your number: ")
#скільки цифр
digit = len(number)
#від'ємне 
if number < str(0):
    print ("negative, " + str(digit) + "-digit")
#додатнє
elif number > str(0):
    print ("positive, " + str(digit) + "-digit")
else: 
    print ("Your number is 0")
