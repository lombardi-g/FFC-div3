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
cbf_pdf = page.extract_text()

# General information
opponent = extract_info_after_label(cbf_pdf, "Jogo:")
full_match_date = extract_info_after_label(cbf_pdf, "Data:")
full_location = extract_info_after_label(cbf_pdf, "Estádio:")
stadium = full_location.split(" / ")[0]
city = full_location.split(" / ")[1]
time = extract_info_after_label(full_match_date, "Horário:")[:5]
date = full_match_date[:10]
home = True if stadium =="Orlando Scarpelli" else False

# Score information
final_score = extract_info_after_label(cbf_pdf, "Resultado Final:").strip().split(" X ")
if home:
    fig_final_score = final_score[0]
    opponent_final_score = final_score[1]
else:
    fig_final_score = final_score[1]
    opponent_final_score = final_score[0]

# Time and additional minutes
first_half_added_minutes = extract_info_after_label(cbf_pdf, "Acréscimo:").split(" min")[0]
second_half_added_minutes = extract_info_after_label(extract_info_after_label(cbf_pdf, "Término do 2"),"Acréscimo:").split(" m")[0]
first_half_minutes = 45 + int(first_half_added_minutes)
second_half_minutes = 45 + int(second_half_added_minutes)
match_minutes = first_half_minutes + second_half_minutes

print(cbf_pdf)