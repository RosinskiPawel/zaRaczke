from PyPDF2 import PdfReader
from pathlib import Path
from datetime import datetime
from tkinter import *
from tkinter import filedialog
import os


class Order:
    def __init__(self, number, pm, date, value):
        self.number = number
        self.pm = pm
        self.date = date
        self.value = value


def openkat():
    chosenKat = filedialog.askdirectory()


def iterPoPlikach(funkcja):
    for file in os.listdir(funkcja):
        fullPath = os.path.join(funkcja, file)

def fileToSaveIn(output):
    fileName = filedialog.askopenfilename(defaultextension="xls")
    with open(fileName, "w") as file:
        file.write(output)
        print(f"dane zostały zapisane w plik {fileName}")
        
     

root = Tk()
root.geometry("500x300")
root.resizable(False, False)
root.title("PDF to Excel")
root.config(bg="#EEE9BF")

lb = Label(root, text="PO's Reader and Convert", bg="#EEE9BF", font=("Arial,15,bold"))
lb.pack(pady=10)

# jeszcze muszę utworzyć przycisk do wyboru pliku Excel, w którym ma zostać zapisany wynik

btn1 = Button(
    root, text="Select folder to open", bg="#EEE9BF", font=("Courier,15,bold"), command=openkat
)
btn1.place(x=40, y=140)
btn2=Button(root, text="Select a file to save", bg="#EEE9BF", font=("Courier,15,bold"), command=)

btn3 = Button(root, text="Convert", bg="#EEE9BF", font=("Courier,15,bold"))
btn3.place(x=180, y=140)
btn4 = Button(root, text="Exit", bg="#EEE9BF", font=("Courier,15,bold"), command=exit)
btn4.place(x=275, y=140)
root.mainloop()


def exit():
    root.destroy()


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
# tu szuka el z końcówą "€", tworzy listę wartości, usuwa "€", zamienia ',' na '.' i tworzy ze stringów liczby zmiennoprzecinkowe, aby wyszukać największą, która jest sumą w euro na zamówieniu PO
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
