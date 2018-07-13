class Calculator:
    # name = 'Good calculator'
    # price = 18

    def __init__(self, name='Good calculator', price='18'):
        self.name = name
        self.price = price

    def add(self, x, y):
        result = x + y
        print(result)

    def minux(self, x, y):
        result = x - y
        print(result)

    def times(self, x, y):
        print(x * y)

    def divide(self, x, y):
        print(x / y)

    def show(self, ss):
        self.s = ss


calcul = Calculator('new Cal', 20)
calcul2 = Calculator()
print(calcul.name)
calcul2.show('qwe')
print(calcul2.s)
calcul.add(4, 5)
calcul.minux(5, 4)

a_input = input('Please give a number:')
print('This input number is:', a_input)

a = [1, 2, 3, 4, 5]
print(len(a))

a_list = [1, 2, 3, 5, 4, 5, 4]
d = {'apple': 1, 'pear:': 2, 'orange': 3}
print(d['apple'])
del d['pear']
print(d)

d1 = {'apple': {1, 2, 3}, 'pear': {1: 3, 3: 'a'}, 'orange': 3}
print(d1['apple'])
print(d1['pear'][3])

# import time
# print(time.localtime())

print(1, 2, 3, 4)

try:
    file = open('eee', 'r')
except Exception as e:
    print(e)

a = [1, 2, 3]
b = [4, 5, 6]
list(zip(a, b))
for i, j in zip(a, b):
    print(i / 2, j * 2)

a = [1, 2, 4]
b = a
print(id(a))
print(id(b))
b[0] = 11
print(a)

import pickle
a_dict = {'da': 111, 2: [1, 2, 3], '23': {1: 2, 'd': 'sad'}}
file = open('pickle_example.pickle', 'wb')
pickle.dump(a_dict, file)
file.close()

# file=open('pickle_example.pickle', 'rb')
# a_dict1 = pickle.load(file)
with open('pickle_example.pickle', 'rb') as file:
    a_dict1 = pickle.load(file)
print(a_dict1)

a_dict = {'da': 111, 2: [1, 2, 3], '23': {1: 2, 'd': 'sad'}}
print(a_dict['23'][1])

char_list = ['a', 'b', 'c', 'c', 'd']
print(set(char_list))

import re
print(re.findall(r'r[ua]n', 'run ran ren'))
print(re.findall(r'run|ran', 'run ran ren'))
