from PyPDF2 import PdfReader

match_summary_pdf = "FIGxMAN.pdf"
reader = PdfReader(match_summary_pdf)

def extract_info_after_label(text, label):
    start_index = text.find(label)
    start_index += len(label)
    end_index = text.find('\n', start_index)
    return text[start_index:end_index].strip()

# def extract_from_summary():
page = reader.pages[0]
text = page.extract_text()

full_match_date = extract_info_after_label(text, "Data:")
full_location = extract_info_after_label(text, "Estádio:")
stadium = full_location.split(" / ")[0]
city = full_location.split(" / ")[1]
time = extract_info_after_label(full_match_date, "Horário:")[:5]
date = full_match_date[:10]