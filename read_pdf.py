from PyPDF2 import PdfReader

def pdf_to_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

pdf_file = 'Pandas cheat sheet.pdf'  # Replace with your PDF file path
text = pdf_to_text(pdf_file)
print(text)
