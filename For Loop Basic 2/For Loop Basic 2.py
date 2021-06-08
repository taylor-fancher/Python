#1 Biggie Size - Given a list, write a function that changes all positive numbers in the list to 'big'
def a(list):
    for i in range(0,len(list),1):
        if list[i] > 0:
            list[i] = 'big'
    print(list)
#2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.
def a(list):
    positive_values = 0
    for i in range(0,len(list),1):
        if list[i] > 0:
            positive_values +=1
    list.pop()
    list.append(positive_values)
    print(list)
#3 Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
def a(list):
    sum = 0
    for i in range(0,len(list),1):
        sum = sum + list[i]
    print(sum)
#4 Average - Create a function that takes a list and returns the average of all the values.
def a(list):
    sum = 0
    for i in range(0,len(list),1):
        sum = sum + list[i]
    avg = sum / len(list)
    print(avg)
#5 Length - Create a function that takes a list and returns the length of the list.
def a(list):
    print(len(list))
#6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def a(list):
    min = list[0]
    for i in range(1,len(list),1):
        if list[i] < min:
            min = list[i]
    print(min)
#7 Maximum - Creat a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
def a(list):
    max = list[0]
    for i in range(1,len(list),1):
        if list[1] > max:
            max = list[i]
    print(max)
#8 Ultimate Analysis - Creat a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def a(list):
    analysis = {}
    sum = 0
    min = list[0]
    max = list[0]
    for i in range(0,len(list),1):
        sum = sum + list[i]
        if list[i] < min:
            min = list[i]
        if list[i] > max:
            max = list[i]
    analysis['sumTotal'] = sum
    analysis['average'] = sum / len(list)
    analysis['minimum'] = min
    analysis['maximum'] = max
    analysis['lenghth'] = len(list)
    print(analysis)
#9 Reverse List - Create a funtion that takes a list and returns that list with values reversed. Do this without creating a second list.
def a(list):
    list_len = len(list)
    for i in range(list_len/2):
        temp = list[list_len - 1 - i]
        list[list_len - 1 - i] = list[i]
        list[i] = temp
    print(list)
