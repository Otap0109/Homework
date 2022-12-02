place = int(input("Type you number of place: "))
if ((place % 2 == 0) and 
    (55 > place > 37)):
    print("Your place in on the top, side")
elif ((place % 2 != 0) and 
    (55 > place > 37)):
    print("Your place is on the bottom, side")
elif ((place % 2 == 0) and 
    (0 < place < 37)):
    print("Your place is on the top, compartment") 
elif ((place % 2 != 0) and 
    (0 < place < 37)):
    print("Your place is on the bottom, compartment") 
else:
    print("Your place is near parasha")     