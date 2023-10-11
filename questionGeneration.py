"All source code within this document is covered by"
"a CC BY-NC-SA 4.0 licence. Read more in /README.md"

import random

def combineSymbols(operands: [chr], values: [str]):
    if len(values) != len(operands) + 1:
        raise ArithmeticError("Operand to value amount missmatch.")
        # There needs to be exactly one fewer operands than values
    output: str = ""

    operands.reverse()
    values.reverse()

    # Im sure this can be done better. 
    for ix in range(0, len(operands)):
        output += values.pop() + " "
        output += operands.pop() + " "
    output += values.pop()

    return output

# randomizes between z = x ? __, and x ? y = __, where ? == operand
def outputFormatRandomizer(operand: chr,
                           firstValue: int,
                           secondValue: int,
                           totalValue: int):
    if random.randint(0, 1) == 0:
        return combineSymbols([operand, '='], [str(firstValue), str(secondValue), "__"])
    else:
        return combineSymbols(['=', operand], [str(totalValue), str(secondValue), "__"])

# Generate a two value positive intiger addition question
# Largest sum
def generateAdditionQuestion(minTotalValue: int, maxTotalValue: int):
    if minTotalValue < 2:
        raise ValueError("Minimum value == 2")
    totalValue = random.randint(minTotalValue, maxTotalValue)
    firstValue = totalValue - random.randint(1, totalValue-1)
    secondValue = totalValue - firstValue

    return outputFormatRandomizer('+', firstValue, secondValue, totalValue)

# Generate a two value positive intiger subtraction question
# Largest value subtracted
def generateSubtractionQuestion(minSubtractedTerm: int, maxSubtractedTerm: int):
    firstTerm = random.randint(minSubtractedTerm, maxSubtractedTerm)
    secondTerm = random.randint(1, firstTerm)
    totalValue = firstTerm - secondTerm

    return outputFormatRandomizer('-', firstTerm, secondTerm, totalValue)

def generateQuestion(controllingRange: (int, int), operands: [chr]):
    match random.choice(operands):
        case '+':
            return generateAdditionQuestion(controllingRange[0], controllingRange[1])
        case '-':
            return generateSubtractionQuestion(controllingRange[0], controllingRange[1])
        case _:
            return "Error, invalid operand"