"All source code within this document is covered by"
"a CC BY-NC-SA 4.0 licence. Read more in /README.md"

import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from datetime import date

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

# Adds the title, name line, and creator text at the bottom.
def addInfoText(worksheet: canvas.Canvas, title: str):
    worksheet.setFillColor(colors.black)

    worksheet.setFont("Courier", 30)
    worksheet.drawString(70, 770, title)

    worksheet.setFont("Courier", 15)
    worksheet.drawString(70, 720, "Namn: ________________________________")

    worksheet.setFont("Courier", 10)
    worksheet.drawString(70, 70, "Genererad av MattePump 1.0")
    worksheet.drawString(70, 55, "Generarad " + str(date.today()))
    worksheet.drawString(70, 40, "CC BY-NC-SA 4.0")

def addQuestions(worksheet: canvas.Canvas):
    worksheet.setFillColor(colors.black)
    worksheet.setFont("Courier", 24)
    for ix in range(0, 12):
        worksheet.drawString(70, ix*50+120, generateAdditionQuestion(2, 10))
    for ix in range(0, 12):
        worksheet.drawString(350, ix*50+120, generateSubtractionQuestion(2, 10))

def generateQuestionSheet():
    worksheet = canvas.Canvas("MattePump.pdf", pagesize=A4)

    addInfoText(worksheet, "Addition och Subtraktion")
    addQuestions(worksheet)

    worksheet.save()

generateQuestionSheet()