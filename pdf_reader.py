from PyPDF2 import PdfReader

match_summary_pdf = "FIGxARN.pdf"
reader = PdfReader(match_summary_pdf)

def extract_until_line_break(text, label):
    start_index = text.find(label)
    start_index += len(label)
    end_index = text.find('\n', start_index)
    return text[start_index:end_index].strip()

def extract_until_doc_end(text, label):
    start_index = text.find(label)
    start_index += len(label)
    return text[start_index:]

# def extract_from_summary():
cbf_pdf = ""
for page in reader.pages:
    cbf_pdf += page.extract_text()

# General information
full_match_date = extract_until_line_break(cbf_pdf, "Data:")
full_location = extract_until_line_break(cbf_pdf, "Estádio:")
stadium = full_location.split(" / ")[0]
city = full_location.split(" / ")[1]
time = extract_until_line_break(full_match_date, "Horário:")[:5]
date = full_match_date[:10]
round = extract_until_line_break(cbf_pdf, "Rodada:")
home = True if stadium =="Orlando Scarpelli" else False
opponent = [team for team in extract_until_line_break(extract_until_doc_end(cbf_pdf, "Jogo:"), "Jogo:").split(" X ") if team != "Figueirense Fc S.a.f. / SC"]

# Score information
final_score = extract_until_line_break(cbf_pdf, "Resultado Final:").strip().split(" X ")
if home:
    fig_final_score = final_score[0]
    opponent_final_score = final_score[1]
else:
    fig_final_score = final_score[1]
    opponent_final_score = final_score[0]

# Time and additional minutes
first_half_added_minutes = extract_until_line_break(cbf_pdf, "Acréscimo:").split(" min")[0]
second_half_added_minutes = extract_until_line_break(extract_until_line_break(cbf_pdf, "Término do 2"),"Acréscimo:").split(" m")[0]
first_half_minutes = 45 + int(first_half_added_minutes)
second_half_minutes = 45 + int(second_half_added_minutes)
match_minutes = first_half_minutes + second_half_minutes

# Goal information
goal_summary = extract_until_doc_end(cbf_pdf,"Gols").split("Cartões Amarelos")[0]
if goal_summary != "NÃO HOUVE MARCADORES":
    goal_summary = extract_until_doc_end(goal_summary,"Equipe").split("NR = Normal")[0].split("\n")
    goal_summary = [item for item in goal_summary if item != '']
    for goal in goal_summary:
        ...

# Yellow and red cards
yellow_card_summary = extract_until_doc_end(extract_until_doc_end(cbf_pdf,"Cartões Amarelos").split("Cartões Vermelhos")[0], "Equipe")