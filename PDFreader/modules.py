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
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox


root = Tk()
root.geometry("400x200")
root.resizable(False, False)
root.title("PDF PO to Excel")
root.config(bg="#EEE9BF")

lb = Label(root, text="Convert", bg="#EEE9BF", font=("Arial,15,bold"))
lb.pack(pady=10)
lb1 = Label(root, text="choose a file: ", bg="#EEE9BF", font=("Courier,15,bold"))
lb1.place(x=10, y=58)

filename2 = StringVar()
Enl = Entry(root, width=30)
Enl.place(x=160, y=65)

btn1 = Button(root, text="Select", bg="#EEE9BF", font=("Courier,15,bold"))
btn1.place(x=70, y=140)
btn2 = Button(root, text="Convert", bg="#EEE9BF", font=("Courier,15,bold"))
btn2.place(x=170, y=140)
btn3 = Button(root, text="Exit", bg="#EEE9BF", font=("Courier,15,bold"))
btn3.place(x=280, y=140)
root.mainloop()


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
print(pageL)


# # indeksy dla słow kluczowych

projectPM_index = pageL.index("PROJEKTLEITER")
projectNum_index = pageL.index("PROJEKTNUMMER")
projectDate_index = pageL.index("LIEFERTERMIN")
# projectValue_index = pageL.index("Honorar")
projValue = []
# tu jest magia ;-) szuka el z końcówą "€", tworzy listę wartości, usuwa "€", zamienia ',' na '.' i tworzy ze stringów liczby zmiennoprzecinkowe, aby wyszukać największą, która jest sumą w euro na zamówieniu PO
for el in pageL:
    if el.endswith("€"):
        projValue.append(float(el.removesuffix("€").replace(",", ".")))
print(projValue)
# wartości dla kluczy
projectPM = pageL[projectPM_index + 1]
projectNumber = pageL[projectNum_index + 1]
# projectValue = pageL[projectValue_index + 2]
projectValue = max(projValue)

# modyfikcja zapisu daty
projectDateTemp = pageL[projectDate_index + 1].split(", ")
data_object = datetime.strptime(projectDateTemp[1], "%d. %B %Y")
projectDate = data_object.strftime("%d.%m.%Y")


print(
    f"Nr projektu: {projectNumber}; PM: {projectPM}; data: {projectDate}, wartość {projectValue}"
)


# first = Invoice(122, 34, "DF", 23112023, 150)
# print(first.name)
# print(first.toList()[3])
