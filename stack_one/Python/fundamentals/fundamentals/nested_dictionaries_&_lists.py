# 1
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]["last_name"] = "bryant"
sports_directory["soccer"][0] = "Andres"
z[0]['y'] = 30

#i have questions here
def iterateDictionary(list):
    for i in range(0,len(list)):
        output = ""
        for key,val in list[i].items():
            output += f" {key} - {val},"
    print(output)

# iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for i in range(0,len(some_list)):
        output = ""
        for key, val in some_list[i].items():
            output += f"{key} - {val}, "
            if key == key_name:
                print(output)

iterateDictionary2('first_name', students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for i in range(0,len(some_dict)):
        output = ""
        for key, val in some_dict.items():
            output += f"{key} - {len(key)} {val}\n"
    print(output)


printInfo(dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
