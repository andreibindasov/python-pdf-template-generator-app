from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="L", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Arial", style="B", size=14)
    pdf.set_text_color(99, 111, 199)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="C", ln=1, border=0)
    pdf.line(9, 21, 290, 21)

    pdf.cell(w=0, h=9, txt="", align="", ln=1, border=0)

    pdf.set_font(family="Arial", style="", size=12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=279, h=9, txt="Subtitle string goes here...", align="L", ln=1, border=1)
    pdf.set_font(family="Arial", style="", size=9)
    for i in range(31):
        pdf.cell(w=9, h=11, txt="v", align="C", ln=0, border=1)

    for i in range(row["Pages"]):
        pdf.add_page()
        pdf.line(9, 21, 290, 21)

pdf.output("output.pdf")