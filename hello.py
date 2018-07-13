print("hello")
print("I'm M")
print("Apple" + "Car")
print("Apple" + "4")
print("Apple" + str(4))
print("1+2")
print(1 + 2)
print(float("2.1") + 1)

apple = 1
print(apple)

a = 1
b = 2
c = 3
print(a, b, c)

a, b, c = 1, 2, 3
print(a, b, c)

condition = 1
while condition < 10:
    print(condition)
    condition = condition + 1

# while True:
#     print("I'm True")

example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in example_list:
    print(i)
print("end")

for i in range(1, 10):
    print(i)

x, y, z = 1, 2, 3
if x > y:
    print("x is greater than y")
else:
    print("y is greater than x")

x = 4
y = 2
z = 3
if x > 1:
    print("x>1")
elif x < 1:
    print('x<1')
else:
    print('x=1')
print('finish running')

a = 1
b = 2
c = a + b
print(c)


def fun(a, b):
    c = a + b
    print(c)


fun(2, 3)


def sale_car(price, colour='red', brand='carmy', is_second_hand=True):
    print('price:', price, 'colour:', colour, 'brand:', brand,
          'is_second_hand:', is_second_hand)


sale_car(1000)

APPLE = 100


def fun1():
    global a
    a = 111
    APPLE = 125
    print(APPLE)
    return a + 100


print(fun1())
print(a)
print(APPLE)

test = 'This is my first test.\nThis is next line. \nThis is last line.'
print(test)

append_test = '\nThis is appended file.'
my_file = open('my_file.txt', 'a')
my_file.write(append_test)
my_file.close()

file = open('my_file.txt', 'r')
content = file.readlines()
for i in content:
    print(i)
print(content)