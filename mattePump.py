import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from datetime import date

# returns a string of "x _ y _ z" where _ is operand 1 and 2 respectively
def formatQuestion(operand1: chr, operand2: chr, x: str, y: str, z: str):
    return x + " " + operand1 + " " + y + " " + operand2 + " " + z

# randomizes between z = x ? __, and x ? y = __, where ? == operand
def outputFormatRandomizer(operand: chr,
                           firstValue: int,
                           secondValue: int,
                           totalValue: int):
    if random.randint(0, 1) == 0:
        return formatQuestion(operand, '=', str(firstValue), str(secondValue), "__")
    else:
        return formatQuestion('=', operand, str(totalValue), str(firstValue), "__")

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

def addInfoText(worksheet: canvas.Canvas, title: str):
    worksheet.setFillColor(colors.black)

    worksheet.setFont("Helvetica", 30)
    worksheet.drawString(70, 770, title)

    worksheet.setFont("Helvetica", 15)
    worksheet.drawString(70, 720, "Namn: ________________________________")

    worksheet.setFont("Helvetica", 10)
    worksheet.drawString(70, 70, "Genererad av MattePump 1.0")
    worksheet.drawString(70, 55, str(date.today()))

def addQuestions(worksheet: canvas.Canvas):
    worksheet.setFillColor(colors.black)
    worksheet.setFont("Helvetica", 24)
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
#print (generateSubtractionQuestion(2, 10))