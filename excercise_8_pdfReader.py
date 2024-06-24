# ----------------------Exercise exp 8-------------------
from PyPDF2 import PdfReader

reader = PdfReader("example.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()


from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]
for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()