#1 Update values in Dictionaries and Lists
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

def a():
    x[1] = [15,8,9] #changes 10 to 15
    print(x)

    students[0]['last_name'] = 'Bryant' #changes 'Jordan' to 'Bryant'
    print(students[0])

    sports_directory.update(soccer = ['Andres', 'Ronaldo', 'Rooney']) #changes 'Messi' to 'Andres'
    print(sports_directory)

    z[0].update(y = 30) #changes 20 to 30
    print(z)

#2 Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(list):
    for i in range(0,len(list)+1,1):
        print(list[i])

# iterateDictionary(students) should output:
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#3 Get Values From a List of Dictionaries
def iterateDictionary2(key,list):
    for i in range(len(list)):
        print(list[i][key])
# iterateDictionary2('first_name', students) should output
# Michael
# John
# Mark
# KB

# iterateDictionary2('last_name', students) should output
# Jordan
# Rosales
# Guillen
# Tonel


#4 Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo():
    pass
# printInfo(dojo) should output:
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
