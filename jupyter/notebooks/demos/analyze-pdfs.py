import os
from PyPDF2 import PdfReader

reports_path = os.path.join("/mnt/c/dev/cl/fun_with/jupyter/notebooks/demos/",'pdfs')
print(reports_path)
all_reports = []

for filename in os.listdir(reports_path):
    f = os.path.join(reports_path, filename)
    if os.path.isfile(f):
        all_reports.append(f)
print(all_reports)

txt = ''
for pdf in all_reports:
    report = all_reports.pop()

    reader = PdfReader(report)
    number_of_pages = len(reader.pages)
    
    pages_left = number_of_pages
    
    # This needs some work
    if pages_left <= 1:
        pass
    else:
        page = reader.pages[pages_left-1]
        text = page.extract_text()
        txt = txt + text
        pages_left =- 1
