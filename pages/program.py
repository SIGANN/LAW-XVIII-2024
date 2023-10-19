# Take the information from paper_author_information.csv and add to program

import csv

global poster_sessions
poster_sessions = {"Onsite Poster Session 1": [7, 9, 13, 22, 34, 41, 61, 62, 64],
                   "Remote Poster Session 1": [8, 11, 18, 27, 38, 40, 63],
                   "Onsite Poster Session 2": [44, 48, 50, 51, 52, 58, 66, 68, 69],
                   "Remote Poster Session 2": [12, 20, 28, 33, 42, 47, 71]
                   }
assert sum(map(len, poster_sessions.values())) == 32

global session_chairs
session_chairs = {"Remote Poster Session 1": "Djamé Seddah",
                  "Remote Poster Session 2": "Heike Zinsmeister"}


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

def add_poster_session_info(new_program_html):
    for poster_session in poster_sessions:
        new_program_html += "<br/<br/><br/>\n\n<h2>" + poster_session + "</h2>\n"
        if poster_session.startswith("Remote"):
            new_program_html += "<i>Session Chair: " + session_chairs[poster_session] + "</i><br/><br/>\n"
        if len(poster_sessions[poster_session]) == 0:
            new_program_html += "<i>Info on papers will be added soon.</i><br/><br/>\n\n"

        for paper_no in poster_sessions[poster_session]:
            title = info[paper_no][0]
            authors = info[paper_no][1]
            if paper_no >= 61:
                new_program_html += "(ACL Findings) "
            new_program_html += title + "<br/>\n"
            new_program_html += "<i>" + authors + "</i><br/><br/>\n\n"
    return new_program_html



for row in program_html.split("\n"):
    if row != "</table>": # hack to find end of program overview table
        new_program_html += row + "\n"
    else:
        new_program_html += row + "\n\n"
        new_program_html = add_poster_session_info(new_program_html)

with open("program.html", "w", encoding="utf-8") as f:
    f.write(new_program_html)
