# Task 1

# string = "962656---554*/"
# result = "".join(dict.fromkeys(string))
# print (string)
# print(result)


#Task 2 
#  
#Task 3

# dict1 = {'Ukraine': 'Kyjiv, Lviv, Kharkiv, Krimea' , 'Germany': 'Berlin, Munich, Kologne ', 'Czech' : 'Prague, Brno, Olomouc', 'Poland': 'Warsaw, Krakow, Katowice'}
# country =input (print('Type the country: '))
# print (dict1.get(country,'Not found'))


#Task 4

keys = input(print('Text: '))
def convert(string):
    li = list(string.split(" ")) 
    return li
values = convert(keys)
dict1 = dict(zip(convert(keys),values.count))
print (dict1)

