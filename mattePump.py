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

def generateQuestionSheet():
    c = canvas.Canvas("MattePump.pdf", pagesize=A4)
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 24)
    for ix in range(0, 14):
        c.drawString(70, ix*50+100, generateAdditionQuestion(2, 10))
    for ix in range(0, 14):
        c.drawString(350, ix*50+100, generateSubtractionQuestion(2, 10))

    c.setFont("Helvetica", 10)
    c.drawString(70, 70, "Genererad av MattePump 1.0" + "     " + str(date.today()))

    c.save()

generateQuestionSheet()
#print (generateSubtractionQuestion(2, 10))