from fpdf import FPDF
import os

class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such as names, due amount and
    period of their stays
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, the_bill):
        pdf = FPDF(orientation="P", unit='pt', format="A4")
        pdf.add_page()

        # add image
        pdf.image("files/house.png", w=40, h=40)
        # Insert Title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        # Insert period label & values
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period: ", border=1)
        pdf.cell(w=150, h=40, txt=the_bill.period, border=1, ln=1)

        # Insert name & due amount of 1st flatmate
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100, h=40, txt=str(flatmate1.name), border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatmate1.pays(mbill=the_bill, flatmate2=flatmate2), 3)), border=1, ln=1)

        # Insert name & due amount of 2nd flatmate
        pdf.cell(w=100, h=40, txt=str(flatmate2.name), border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatmate2.pays(mbill=the_bill, flatmate2=flatmate1), 3)), border=1, ln=1)

        os.chdir("files")
        pdf.output(self.filename)
