# - variable declaration
num1 = 42
num2 = 2.3
# - Boolean
boolean = True
# - Strings
string = 'Hello World'
"""
    - Composite
        - List 
            - initialize
"""
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
"""
    - Composite
        - Dictionary
            - initialize
"""
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
"""
    - Composite
        - Tuples
            - initialize
"""
fruit = ('blueberry', 'strawberry', 'banana')
# - log statement
"""
    - Composite
        -Tuples
            access value
"""
print(type(fruit))
"""
    - Composite
        -List
            -type check
"""
print(pizza_toppings[1])
# - add value
pizza_toppings.append('Mushrooms')
"""
    - Composite
        -Dictionary
            access value
"""
print(person['name'])
# -change value
person['name'] = 'George'
# -change value
person['eye_color'] = 'blue'
# - access value
print(fruit[2])

"""
- conditional
    - if
    -else
"""
if num1 > 45:
    print("It's greater")

else:
    print("It's lower")

"""
- conditional
    - if
    -else if
    -else
"""

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# - for loop
# 0 - start

for x in range(5):
# 5 - stop
# - log statement
    print(x)

# - for loop
# 2 - start
# - - increment
for x in range(2,5):
# 5 - stop
# - log statement
    print(x)

# - for loop
# 2 - start

for x in range(2,10,3):
# 10 - stop
# - log statement
    print(x)
# 0 - variable declaration
x = 0

# - while loop
#     - start
while(x < 5):
    print(x)
# - increment
# 5 - stop
    x += 1

# - delete value
pizza_toppings.pop()
# - delete value 1
pizza_toppings.pop(1)

# - log statement
print(person)
# - delete value
person.pop('eye_color')
# 'name': 'John', 'location': 'Salt Lake', 'age': 37 - log statement 
print(person)

"""
- for loop
    - start
"""
for topping in pizza_toppings:
    """
    - conditional
    - if
    - if
    """
    if topping == 'Pepperoni':
        # if topping is Pepperoni - continue
        continue
    # 'After 1st if statement' - log statement
    print('After 1st if statement')
    if topping == 'Olives':
        # if topping is olives - break
        break

"""
print_hello_ten_times - function

- for loop
    0 - start
    10 - stop
"""
def print_hello_ten_times():
    for num in range(10):
        print('Hello')
# - parameter
print_hello_ten_times()

"""
print_hello_x_times - function
- for loop
    0 - start
    4 - stop
"""
def print_hello_x_times(x):
    for num in range(x):
        # 'Hello' 'Hello' 'Hello' 'Hello' - log statement
        print('Hello')
# - argument
print_hello_x_times(4)

"""
print_hello_x_or_ten_times - function
- for loop
    0 - start
    10,4 - stop
"""
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        # hello * 10, hello * 4 - log statement
        print('Hello')

# - argument
print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)

"""
- comment
- multiline
"""

"""
Bonus section
"""

#- single line

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)