import  math 


#вибрати фігуру
figure = input( "Choose figure (triangle, rectangle, circle?): ")
#ввести довжину сторін трикутника
if  figure == "triangle" :
    a = float(input("Type height: "))
    b = float(input ("Type one side: "))
    c = a*b/2
    print("Square= " + str(c))
#ввести довжину сторін прямокутника 
elif figure == "rectangle" :
    a = float(input("Type height: "))
    b = float(input("Type lenght: "))
    c = a*b
    print("Square= " + str(c))
#ввести радіус кола
elif figure == "circle":
    a = float(input("Type radius: "))
    c = a*math.pi
    print("Square= " + str(c))