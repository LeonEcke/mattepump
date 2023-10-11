"All source code within this document is covered by"
"a CC BY-NC-SA 4.0 licence. Read more in /README.md"

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from datetime import date

from questionGeneration import generateQuestion

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
        worksheet.drawString(70, ix*50+120, generateQuestion((2, 10), ['+', '-']))
    for ix in range(0, 12):
        worksheet.drawString(350, ix*50+120, generateQuestion((2, 50), ['+', '-']))

def generateQuestionSheet():
    worksheet = canvas.Canvas("MattePump.pdf", pagesize=A4)

    addInfoText(worksheet, "Addition och Subtraktion")
    addQuestions(worksheet)

    worksheet.save()

generateQuestionSheet()