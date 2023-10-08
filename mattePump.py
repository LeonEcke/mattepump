import random

# Generate a two value positive intiger addition question
def generateAdditionQuestion(minTotalValue: int, maxTotalValue: int):
    if minTotalValue < 2:
        raise ValueError("Minimum value == 2")
    totalValue = random.randint(minTotalValue, maxTotalValue)
    firstValue = totalValue - random.randint(1, totalValue-1)
    secondValue = totalValue - firstValue

    return str(firstValue) + " + " + str(secondValue) + " = __" + str(totalValue)

# Generate a two value positive intiger subtraction question
def generateSubtractionQuestion(minSubtractedTerm: int, maxSubtractedTerm: int):
    firstTerm = random.randint(minSubtractedTerm, maxSubtractedTerm)
    secondTerm = random.randint(1, firstTerm)

    return str(firstTerm) + " - " + str(secondTerm) + " = __"

print (generateSubtractionQuestion(2, 10))