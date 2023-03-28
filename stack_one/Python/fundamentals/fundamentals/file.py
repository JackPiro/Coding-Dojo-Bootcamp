num1 = 42 #integer variable decleration
num2 = 2.3 #float variable decleration
boolean = True #boolean
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') #tuples initialize
print(type(fruit)) #type check
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #dictionary add item
print(person['name']) #log statement
person['name'] = 'George' #access value Change value
person['eye_color'] = 'blue' #key error eye_color
print(fruit[2]) #log statement

if num1 > 45:
    print("It's greater") #if else statement
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!") #else if statement
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop increment numbers starting at 0
    print(x)
for x in range(2,5): #for loop increment numbers starting at 2
    print(x)
for x in range(2,10,3): # for loop increment numbers by three 1-10
    print(x)
x = 0
while(x < 5): #while loop
    print(x)
    x += 1

pizza_toppings.pop() #list delete item
pizza_toppings.pop(1) #list delete item //deletes sausage index

print(person) #log statement
person.pop('eye_color') #key error eye_color
print(person) #log statement

for topping in pizza_toppings: # for loop checks if it is value in squence
    if topping == 'Pepperoni':
        continue #
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): #initialize function print hello ten times
    for num in range(10):
        print('Hello')

print_hello_ten_times() #function call

def print_hello_x_times(x): #function initiization
    for num in range(x):
        print('Hello') #log statement

print_hello_x_times(4) #function call default parameter 4

def print_hello_x_or_ten_times(x = 10): #sunction initialization with default parameter to print x
    for num in range(x): #checks if x is sequence data type
        print('Hello')

print_hello_x_or_ten_times() #function call
print_hello_x_or_ten_times(4) #function call 4 times


"""
Bonus section
"""

print(num3) #log statement err0r variable not fpound
num3 = 72 #initialize variable num3
fruit[0] = 'cranberry' #error tuples cannot be modified once defined
print(person['favorite_team']) #key error no access value favorite_team exists
print(pizza_toppings[7]) #error pizza_toppings 7 doesnt exist
print(boolean) #log statement true
fruit.append('raspberry') #adds rasberruy to fruit list
fruit.pop(1) #deletes strawberry