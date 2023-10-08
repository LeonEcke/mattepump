import random

def generateQuestion():
    return str(random.randint(0, 10)) + " + " + str(random.randint(0, 10)) + " = __"

print (generateQuestion())