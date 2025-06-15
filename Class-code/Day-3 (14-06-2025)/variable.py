# x : int = 100 (-32768 to 32767)

age = 30 # Integers
height = 5.4 # Float
name = 'Kamran' # String
disable = True # Boolean
comp = 3 + 2j # complex

print('The value of age:', age)
print('The value of height:', height)
print('My name is:', name)

print('The type of age:', type(age))
print('The type of comp:', type(comp))


print('My name is:', name, 'and my age is', age, 'and my height is', height)
print(f'My name is {name} and my age is {age} and my height is {height}')

print('My name is {0}. My age is {1}. I am {2}ft tall.'.format(name, age, height))