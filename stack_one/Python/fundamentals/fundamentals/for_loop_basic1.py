# # task 1
# from math import remainder

def basics():
    for i in range(1,151):
        print(i)

# basics()

def multiples_of_five():
    for i in range(0,1000,5):
        print(i)

# multiples_of_five()

def suckers_huge():
    i = 1
    adding_numbers = []
    while i in range(0,501):
        adding_numbers.append(i)
        i += 2
        if i <= 500:
            print(i)
        else:
            print(sum(adding_numbers))
        
# suckers_huge()

def counting_the_dojo_way():
    i = 0
    while i in range(0,100):
        i += 1
        if i%10 == 0:
            print('coding dojo')
        elif i%5 == 0:
            print('coding')
        else:
            print(i)

counting_the_dojo_way()

# i = place_holder
#         elif i == 'coding':
#             i = 'coding dojo'
#             print('i')

    # elif remainder_5 == 0:
    #     place_holder = i
    #     i = 'coding dojo'
    #     print('i')
    #     i = place_holder
    # else:
    #     print(i)



    #count down by fours
number1 = 200
def counting_fours():
    for number1 in range(200,-4,-4):
        print(number1)
        # number1 -= 4

# counting_fours()

def flex_counter():
    low_num = 2
    high_num = 10
    mult = 2
    for i in range(low_num,high_num):
        if i % mult == 0:
            print(i)

flex_counter()
