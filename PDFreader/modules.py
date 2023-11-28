class Invoice:
    def __init__(self, name, id, pm, date, value):
        self.name = name
        self.id = id
        self.pm = pm
        self.date = date
        self.value = value

    def toList(self):
        return [self.name, self.id, self.pm, self.date, self.value]

    def readProjNr(self):
        # projnr = oczytuje nr porojektu z plik w postaci xxxx-xxx i ten nr musi rodzielić na name i id
        projnr = "xxxx-xx"
        tempprojnr = projnr.split("-")
        # name = tempprojnr[0]
        # id = tempprojnr[1]
        return tempprojnr


from PyPDF2 import PdfReader
from pathlib import Path
from datetime import datetime
import pdfminer

months = {"January": 1, "February": 2, "November": 11}

# wczytuje plik pdf
pdf_path = Path("C:/CODING/pdfToRead2.pdf")
pdf = PdfReader(str(pdf_path))
# pobiera 1.stronę
first_page = pdf.pages[0]
# konwertuje na tekst
pageToWord = first_page.extract_text()

# tekst ma wiele lini konca wiersza, więc tworzona jest lista z podziałem konca wiersza '\n'
pageL = pageToWord.split("\n")
# usuwanie pustych miejsc
for el in pageL:
    pageL.remove(el) if el == " " else el
# print(pageL)


# # indeksy dla słow kluczowych

projectPM_index = pageL.index("PROJEKTLEITER")
projectNum_index = pageL.index("PROJEKTNUMMER")
projectDate_index = pageL.index("LIEFERTERMIN")
projectValue_index = pageL.index("Honorar") if "Honorar" in pageL else None

# wartości dla kluczy
projectPM = pageL[projectPM_index + 1]
projectNumber = pageL[projectNum_index + 1]
projectValue = pageL[projectValue_index + 2]

projectDateTemp = pageL[projectDate_index + 1].split(", ")
data_object = datetime.strptime(projectDateTemp[1], "%d. %B %Y")

projectDate = data_object.strftime("%d.%m.%Y")


print(
    f"Nr projektu: {projectNumber}; PM: {projectPM}; data: {projectDate}, wartość {projectValue}"
)


# first = Invoice(122, 34, "DF", 23112023, 150)
# print(first.name)
# print(first.toList()[3])