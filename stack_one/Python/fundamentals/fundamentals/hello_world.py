# 1. TASK: print "Hello World"
print('hello world')
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print('hello(name)')
print( "hello","world")	# with a comma
print( "hello" + "world")	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print('hello ',name)
print('hello','world')	# with a comma
# print('hello'+ -- 'world')	# with a +	-- this one should give us an error
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print('I love to eat {} and {}.'.format('sushi','pizza')) # with .format()
print(f'I love to eat {fave_food1} and {fave_food2}.') # with an f string

print('hello world'.encode(encoding ="ascii",errors= "backslashreplace"))

print(fave_food1.encode(encoding = "ascii",errors = "namereplace"))
print(fave_food1.find("s"))
txt = 'I love to eat b sushi and b pizza.'
print(txt.rpartition("and"))

def string_func():
    txt.find("b")
    print(txt.find("b"))

string_func()

for i in range(12,100,10):
    print(i)
