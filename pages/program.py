# Take the information from paper_author_information.csv and add to program

import csv

global sessions
sessions = {"Long Papers 1": [13, 22, 43],
           "Short Papers 1": [6, 7],
           "Long Papers 2": [10, 19, 26],
           "In-Person Poster Session": [8, 23, 25, 38, 42, 47],
           "Short Papers 2": [18, 24],
           "Long Papers 3": [21, 29, 41],
           "Short Talk": [15]
           }
assert sum(map(len, sessions.values())) == 20


global info
info = {}
with open("paper_author_information.csv", encoding="utf-8") as f:
    r = csv.reader(f, delimiter=",", quotechar='"')
    next(r) # skip header
    for row in r:
        paper_no = int(row[0])
        info[paper_no] = (row[1], row[2]) # title, authors

# Modify lower part of program.html
with open("mainprogram.html", encoding="utf-8") as f:
    program_html = f.read()

new_program_html = ""

def add_session_info(new_program_html):
    for session in sessions:
        new_program_html += "<br/>\n\n<h2>" + session + "</h2>\n"
        if len(sessions[session]) == 0:
            new_program_html += "<i>Info on papers will be added soon.</i><br/><br/>\n\n"

        for paper_no in sessions[session]:
            title = info[paper_no][0]
            authors = info[paper_no][1]
            new_program_html += title + "<br/>\n"
            new_program_html += "<i>" + authors + "</i><br/><br/>\n\n"
    return new_program_html



for row in program_html.split("\n"):
    if row != "</table>": # hack to find end of program overview table
        new_program_html += row + "\n"
    else:
        new_program_html += row + "\n\n"
        new_program_html = add_session_info(new_program_html)

with open("program.html", "w", encoding="utf-8") as f:
    f.write(new_program_html)
