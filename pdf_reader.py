from PyPDF2 import PdfReader

match_summary_pdf = "FIGxMAN.pdf"
reader = PdfReader(match_summary_pdf)

# def extract_from_summary():
page = reader.pages[0]
text = page.extract_text()