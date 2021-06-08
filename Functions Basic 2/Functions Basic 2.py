#1 Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0(as the last element)
def a(num):
    list = []
    for i in range(num,-1,-1):
        list.append(i)
    print(list)
#2 Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second
def a(list):
    print(list[0])
    return list[1]
#3 First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length
def a(list):
    sum = 0
    sum = list[0] + len(list)
    print(sum)
#4 Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def a(list):
    greater_than_list = []
    value = list[1]
    for i in range(len(list)):
        if list[i] > value:
            greater_than_list.append(list[i])
    print(len(greater_than_list))
    print(greater_than_list)
#5 This Length, That Value - Write a function that accepts two integers as parameters: size and value. The funtion should create and return a list whose length is equal to the given size, and whose values are all the given value.
list = []
def a(value, length):
    for i in range(1,length+1,1):
        list.append(value)
    print(list)