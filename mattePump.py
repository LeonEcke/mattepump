import random

# Generate a two value question. 
def generateAdditionQuestion(minTotalValue: int, maxTotalValue: int):
    if minTotalValue < 2:
        raise ValueError("Minimum value == 2")
    totalValue = random.randint(minTotalValue, maxTotalValue)
    firstValue = totalValue - random.randint(1, totalValue-1)
    secondValue = totalValue - firstValue

    return str(firstValue) + " + " + str(secondValue) + " = __" + str(totalValue)

print (generateAdditionQuestion(2, 10))