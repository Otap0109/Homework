#Площа квадратної зали
S = float(input("Type hall square: "))
a = S**0.5
#Радіус круглої сцени 
R = float(input("Type stage radius: "))
b = R*2
#Відступ від стіни
K = float(input("Type minimum passage from the wall to the stage: "))
#вивести на екран можливо чи ні
c = a-b
if ((c > K) or
    (c == K)):
    print("It's possible")
else:
    print("It's impossible")
