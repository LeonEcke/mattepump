"All source code within this document is covered by"
"a CC BY-NC-SA 4.0 licence. Read more in /README.md"

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from pdfGeneration import addInfoText, addQuestions

def generateQuestionSheet():
    worksheet = canvas.Canvas("MattePump.pdf", pagesize=A4)

    addInfoText(worksheet, "Addition och Subtraktion")
    addQuestions(worksheet, ['+', '-'], (2, 15))

    worksheet.save()

generateQuestionSheet()