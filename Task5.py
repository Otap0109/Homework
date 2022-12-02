amount = int(input("Type amount of money: "))
if amount > 200:
    a = amount / 200
    b = amount % 200
   
    b > 100
    c = b / 100
    d = b % 100
    
    d > 10
    f = d / 10
    g = d % 10
   
    g > 1
    x = g / 1 
    # if ((a == 0) or
    #     (c == 0) or
    #     (g == 0)
    #     (x == 0)):

    print (str(int(a)) + " banknotes 200 UAH, " + str(int(c)) + " banknotes 100 UAH, " + str(int(f)) + " banknotes 10 UAH," + str(int(x)) + " banknotes 1 UAH,")
   
# print (str(a) + "banknotes 200 UAH, " + str(c) + "banknotes 100 UAH, " + str(f) + "banknotes 10 UAH," + str(x) + "banknotes 1 UAH,")
elif 100 < amount < 200:
    b = amount % 200

    b > 100
    c = b / 100
    d = b % 100
    
    d > 10
    f = d / 10
    g = d % 10
    
    g > 1
    x = g / 1
    print (str(int(c)) + " banknote 100 UAH, " + str(int(f)) + " banknotes 10 UAH," + str(int(x)) + " banknotes 1 UAH,")
elif 10 <  amount < 100:
    b = amount % 100
    d = b % 100
        
    d > 10
    f = d / 10
    g = d % 10
        
    g > 1
    x = g / 1
    print (str(int(f)) + " banknotes 10 UAH," + str(int(x)) + " banknotes 1 UAH,")

elif 0 < amount < 10:
    b = amount % 10
    d = b % 100
            
    d > 10
    f = d / 10
    g = d % 10
            
    g > 1
    x = g / 1
    print (str(int(x)) + " banknotes 1 UAH,")
else:
    print("Wrong type of information!")