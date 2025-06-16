# Type casting
# int() --> to convert any data type to integer but not string alphabets
# float() --> to convert any data type to float but not string alphabets
# str() --> to convert any data type to string
# bool() --> to covert into boolean value.

n =  20
print('The type of n:', type(n))
f = float(n)
print(f'The type of f: {f}--{type(f)}')

string = str(n)
print('The type of string:', type(string))

s = '123'
print('The type of s:',type(int(s)))

name = 'Ali'
print(int(name)) # givers error
print(chr(65))