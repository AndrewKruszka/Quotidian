from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from news import *
from folder import *


# Registering font
pdfmetrics.registerFont(TTFont('Kefa', 'Kefa.ttc'))

# Creating Style sheet
styles = getSampleStyleSheet()

pdf_name = "Quotidian " + str(return_num_date()) + ".pdf"

# Creating canvas object
canvas = Canvas(get_path() + pdf_name, pagesize=LETTER)

def get_volume():
    with open("volume.txt", "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val

def create_title():
    # The Quotidana
    canvas.setFont("Kefa", 60)
    canvas.drawCentredString(4 * inch, 10 * inch, "The Quotidian")

    # Folio
    canvas.setLineWidth(1)
    canvas.setLineCap(1)
    canvas.line(.25 * inch, 9.75 * inch, 8.25 * inch, 9.75 * inch)
    canvas.line(.25 * inch, 9.50 * inch, 8.25 * inch, 9.50 * inch)

    # Volume
    volume = get_volume()
    canvas.setFont("Times-Roman", 10)
    canvas.drawString(.25 * inch, 9.55 * inch, "Volume " + str(volume))

    # Date
    canvas.setFont("Times-Roman", 12)
    canvas.drawCentredString(4 * inch, 9.55 * inch, return_word_date())

    canvas.setFont("Kefa", 25)
    canvas.drawCentredString(4 * inch, 8.75 * inch, "Top Headlines")
    canvas.line(2.75 * inch, 8.6 * inch, 5.25 * inch, 8.6 * inch)

############## AP NEWS #############

def ap_news():
    canvas.setFont("Times-Bold", 20)
    canvas.drawCentredString(4 * inch, 8 * inch, "Associated Press")

    f_title, f_content, f_link, s_title, s_content, s_link= get_ap_headlines()

    canvas.setFont("Times-Bold", 13)
    canvas.drawString(.25 * inch, 7.5 * inch, f_title)
    canvas.drawString(.25 * inch, 6.5 * inch, s_title)

    canvas.setFont("Times-Roman", 10)

    p1 = Paragraph(f_content + " [<link href=" + f_link + " color=Blue>Link</link>]", styles['Normal'])
    p1.wrap(7.5 * inch, 7.75 * inch)
    p1.drawOn(canvas, .5 * inch, 7 * inch)

    p2 = Paragraph(s_content + " [<link href=" + s_link + " color=Blue>Link</link>]", styles['Normal'])
    p2.wrap(7.5 * inch, 7.75 * inch)
    p2.drawOn(canvas, .5 * inch, 6 * inch)

############### TECH NEWS #############

def tech_news():
    canvas.setFont("Times-Bold", 20)
    canvas.drawCentredString(4 * inch, 5.5 * inch, "Technology News")

    f_title, f_content, f_link, s_title, s_content, s_link = get_tech_headlines()

    canvas.setFont("Times-Bold", 13)
    canvas.drawString(.25 * inch, 5 * inch, f_title)
    canvas.drawString(.25 * inch, 4 * inch, s_title)

    canvas.setFont("Times-Roman", 10)

    p1 = Paragraph(f_content + " [<link href=" + f_link + " color=Blue>Link</link>]", styles['Normal'])
    p1.wrap(7.5 * inch, 7.75 * inch)
    p1.drawOn(canvas, .5 * inch, 4.5 * inch)

    p2 = Paragraph(s_content + " [<link href=" + s_link + " color=Blue>Link</link>]", styles['Normal'])
    p2.wrap(7.5 * inch, 7.75 * inch)
    p2.drawOn(canvas, .5 * inch, 3.5 * inch)


############## US NEWS #############
def us_news():
    canvas.setFont("Times-Bold", 20)
    canvas.drawCentredString(4 * inch, 3 * inch, "United States")

    f_title, f_content, f_link, s_title, s_content, s_link = get_us_headlines()

    canvas.setFont("Times-Bold", 12)
    canvas.drawString(.25 * inch, 2.5 * inch, f_title)
    canvas.drawString(.25 * inch, 1.5 * inch, s_title)

    canvas.setFont("Times-Roman", 10)

    p1 = Paragraph(f_content + " [<link href=" + f_link + " color=Blue>Link</link>]", styles['Normal'])
    p1.wrap(7.5 * inch, 7.75 * inch)
    p1.drawOn(canvas, .5 * inch, 2 * inch)

    p2 = Paragraph(s_content + " [<link href=" + s_link + " color=Blue>Link</link>]", styles['Normal'])
    p2.wrap(7.5 * inch, 7.75 * inch)
    p2.drawOn(canvas, .5 * inch, 1 * inch)

create_title()
ap_news()
tech_news()
us_news()

canvas.save()



