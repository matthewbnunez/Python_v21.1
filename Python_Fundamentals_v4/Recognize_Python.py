num1 = 42 # variable declaration, Numbers
num2 = 2.3 # variable declaration, Numbers
boolean = True # variable declaration, Boolean
string = 'Hello World' # variable declaration, String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Composite-list-initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Composite-Tuples-initialize
fruit = ('blueberry', 'strawberry', 'banana') # Composite-list-initialize
print(type(fruit)) # type check, log statement
print(pizza_toppings[1]) # log statement, Composite-List-access value
pizza_toppings.append('Mushrooms') # Composite-List-add value
print(person['name']) # log statement, Composite-Tuples-access value
person['name'] = 'George' # Composite-Tuples-change value
person['eye_color'] = 'blue' # Composite-Tuples-change value
print(fruit[2]) # log statement, Composite-List-access value

if num1 > 45: # conditional if
    print("It's greater") # log statement
else: # conditional else
    print("It's lower") # log statement

if len(string) < 5: # conditional if, length check
    print("It's a short word!") # log statement
elif len(string) > 15: # conditional else if, length check
    print("It's a long word!") # log statement
else: # conditional else
    print("Just right!") # log statement

for x in range(5): # for loop
    print(x) # log statement
for x in range(2,5): # for loop
    print(x) # log statement
for x in range(2,10,3): # for loop
    print(x) # log statement
x = 0 # variable declaration, Numbers
while(x < 5): # while loop
    print(x) # log statement
    x += 1 # variable declaration, Numbers

pizza_toppings.pop() # Composite-List-delete value
pizza_toppings.pop(1) # Composite-List-access value, Composite-List-delete value

print(person) # log statement
person.pop('eye_color') # Composite-Tuples-access value, Composite-Tuples-delete value
print(person) # log statement

for topping in pizza_toppings: # for loop-start
    if topping == 'Pepperoni': # conditional if
        continue # for loop-continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # conditional if
        break # for loop-break

def print_hello_ten_times(): #function
    for num in range(10): # for loop
        print('Hello') # log statement

print_hello_ten_times() # function

def print_hello_x_times(x): #function-parameter
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_times(4) # function-parameter

def print_hello_x_or_ten_times(x = 10): #function-parameter, variable declaration, Numbers
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_or_ten_times() # function
print_hello_x_or_ten_times(4) # function-parameter


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)