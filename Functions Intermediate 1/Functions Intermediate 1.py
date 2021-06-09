import random

def randInt( min = 0 , max = 100 ):
    if max < min or min > max:
        return "Not Possible"
    else:
        range = max - min
        return round(random.random() * range + min)


#print(randInt()) 		# should print a random integer between 0 to 100
#print(randInt(max=50)) # should print a random integer between 0 to 50
#print(randInt(min=50)) 	# should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500