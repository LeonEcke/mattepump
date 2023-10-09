import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from datetime import date

# Generate a two value positive intiger addition question
# Largest sum
def generateAdditionQuestion(minTotalValue: int, maxTotalValue: int):
    if minTotalValue < 2:
        raise ValueError("Minimum value == 2")
    totalValue = random.randint(minTotalValue, maxTotalValue)
    firstValue = totalValue - random.randint(1, totalValue-1)
    secondValue = totalValue - firstValue

    output = ""
    equalsPlacement = random.randint(0, 1)

    if equalsPlacement == 0:
        output = str(firstValue) + " + " + str(secondValue) + " = __"
    else:
        output = str(totalValue) + " = " + str(firstValue) + " + __"

    return output

# Generate a two value positive intiger subtraction question
# Largest value subtracted
def generateSubtractionQuestion(minSubtractedTerm: int, maxSubtractedTerm: int):
    firstTerm = random.randint(minSubtractedTerm, maxSubtractedTerm)
    secondTerm = random.randint(1, firstTerm)
    totalValue = firstTerm - secondTerm

    output = ""
    equalsPlacement = random.randint(0, 1)

    if equalsPlacement == 0:
        output = str(firstTerm) + " - " + str(secondTerm) + " = __"
    else:
        output = str(totalValue) + " = " + str(firstTerm) + " - __"


    return output

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