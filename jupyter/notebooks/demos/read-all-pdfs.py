import os
from PyPDF2 import PdfReader

"""Read all pdfs and creates a txt file"""

reports_path = os.path.join("/mnt/c/dev/cl/fun_with/jupyter/notebooks/demos/",'pdfs')
print(reports_path)
all_reports = []

for filename in os.listdir(reports_path):
    f = os.path.join(reports_path, filename)
    if os.path.isfile(f):
        all_reports.append(f)
print('Reading ' + str(len(all_reports)) + ' pdf reports!')


def combine_pdfs():
    txt = ''
    print("Combining " + str(len(all_reports)) + '!')
    for pdf in all_reports:
        report = all_reports.pop()

        reader = PdfReader(report)
        number_of_pages = len(reader.pages)
        z = number_of_pages-1
        y  = range(4,z)
        for p in y:
            page = reader.pages[p]
            x = page.extract_text()
            txt = x + txt
        txt_x = txt.replace('/n','')
        return txt_x

all_text = combine_pdfs()


with open("all_text.txt","w") as f:
    print("Writing base file!")
    f.write(all_text)
    print("Done!")
