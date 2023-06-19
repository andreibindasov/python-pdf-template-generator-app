from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="L", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # The Header
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

    for i in range(61, 191, 10):
        pdf.line(9, i, 290, i)

    # The Footer
    pdf.ln(160)
    pdf.set_font(family="Arial", style="I", size=7)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=9, txt=row["Topic"].lower(), align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        for j in range(21, 191, 10):
            pdf.line(9, j, 290, j)

        # The Footer
        pdf.ln(190)
        pdf.set_font(family="Arial", style="I", size=7)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=9, txt=row["Topic"].lower(), align="R")

pdf.output("output.pdf")