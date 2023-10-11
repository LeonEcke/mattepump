"All source code within this document is covered by"
"a CC BY-NC-SA 4.0 licence. Read more in /README.md"

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from datetime import date

from questionGeneration import generateQuestion

# Massive blob of formatting
horizontalMargin = 70
verticalMargin = 40
titleSize = 30
nameAreaSize = 15
nameAreaMargin = nameAreaSize*2
infotextSize = 10
infotextMargin = 3

# Adds the title, name line, and creator text at the bottom.
def addInfoText(worksheet: canvas.Canvas, title: str):

    worksheet.setFillColor(colors.black)

    titleVerticalPlacement = A4[1] - verticalMargin - titleSize
    worksheet.setFont("Courier", titleSize)
    worksheet.drawString(horizontalMargin,
                         titleVerticalPlacement,
                         title)

    nameAreaPlacement = titleVerticalPlacement - nameAreaSize - nameAreaMargin
    worksheet.setFont("Courier", nameAreaSize)
    worksheet.drawString(horizontalMargin,
                         nameAreaPlacement,
                         "Namn: ________________________________")

    worksheet.setFont("Courier", infotextSize)

    worksheet.drawString(horizontalMargin,
                         verticalMargin + ( infotextSize + infotextMargin ) * 2,
                         "Genererad av MattePump 1.0")
    
    worksheet.drawString(horizontalMargin,
                         verticalMargin + ( infotextSize + infotextMargin ) * 1,
                         "Generarad " + str(date.today()))
    
    worksheet.drawString(horizontalMargin,
                         verticalMargin + ( infotextSize + infotextMargin ) * 0,
                         "CC BY-NC-SA 4.0")

def addQuestions(worksheet: canvas.Canvas,
                 operands: [chr],
                 valueRange: (int, int)):
    worksheet.setFillColor(colors.black)
    worksheet.setFont("Courier", 24)
    for ix in range(0, 12):
        worksheet.drawString(horizontalMargin,
                             ix*50+120,
                             generateQuestion(valueRange, operands))
    for ix in range(0, 12):
        question = generateQuestion(valueRange, operands)
        worksheet.drawString(A4[0] - len(question) * 17 - horizontalMargin,
                             ix*50+120,
                             question)