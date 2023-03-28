def count_down(num):
    count_list = []
    for i in range(num,-1,-1):
        count_list.append(i)
    print(count_list)
    return count_list

count_down(5)

return_list = []
def print_return(return_list):
    print(return_list[0])
    return(return_list[1])

print(print_return([1,2]))

plus_list = []
def plus_length(plus_list):
    return plus_list[0] + len(plus_list)

print(plus_length([1,2,3]))

list_one = []
list_two = []
def greater_than_second(list_one):
    if len(list_one) < 2:
        return False
    for i in range(0,len(list_one)):
        if list_one[i] > list_one[1]:
            list_two.append(list_one[i])
    print(list_two)
    return list_two

print(greater_than_second([5,4,1,1,5,5,5,4,6,3,9]))



def length_value(length,value):
    list_length_value = []
    while length in range(1,length + 1):
        list_length_value.append(value)
        length = length - 1
    return list_length_value

print(length_value(5,6))