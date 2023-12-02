from PyPDF2 import PdfReader
from pathlib import Path
from datetime import datetime
from tkinter import *
from tkinter import filedialog
import locale

locale.setlocale(locale.LC_TIME, "de_DE")

# import openpyxl
# from openpyxl import Workbook


class MyOrdersReader:
    def __init__(self, root):
        self.root = root
        self.chosen_files = []
        self.list_pages = []
        self.pure_info = []

        self.btn_open = Button(
            root,
            text="Select files to open",
            bg="#EEE9BF",
            font=("Courier,15,bold"),
            command=self.openFiles,
        )
        self.btn_open.pack()

        self.btn2_convert = Button(
            root,
            text="Convert",
            bg="#EEE9BF",
            font=("Courier,15,bold"),
            command=self.action,
        )
        self.btn2_convert.pack()

        self.btn3_save = Button(
            root,
            text="Select file to save",
            bg="#EEE9BF",
            font=("Courier,15,bold"),
            command=self.fileToSaveIn,
        )
        self.btn3_save.pack()

        self.btn4_exit = Button(
            root, text="Exit", bg="#EEE9BF", font=("Courier,15,bold"), command=exit
        )
        self.btn4_exit.pack()

    def openFiles(self):
        # utworzenie listy plików, które zostaną otwarte z katalogu
        self.chosen_files = filedialog.askopenfilenames(
            defaultextension=".pdf",
            filetypes=[("Pliki PDF", "*.pdf"), ("Wszystkie pliki", "*.*")],
        )

    def action(self):
        # działanie po naciśnięciu przycisku Convert
        self.gettingFirstPages()
        self.converting()

    def gettingFirstPages(self):
        # tworzenie list z przekonwertowanymi pierwszymi stronami plików pdf
        for file in self.chosen_files:
            pdfPath = Path(file)
            pdf_file = PdfReader(str(pdfPath))
            main_page = pdf_file.pages[0]
            # konwersja na tekst
            converted_page = main_page.extract_text()

            # z uwagi na trudne formatowanie tekstu zostaje on zamieniony na liste, a elementy sa dzielone na podstawie znaku nowego wiersza \n
            page_as_list = converted_page.split("\n")

            # usuwanie pustych elementow, aby bylo latwiej okreslac indeksy
            cleaned_list = [el.strip() for el in page_as_list if el.strip()]
            print(cleaned_list)

            # dodwanie do listy oczyszczonych list
            self.list_pages.append(cleaned_list)
        return self.list_pages

    def converting(self):
        for page in self.list_pages:
            temp_list = []
            results = [
                self.extracting_num(page),
                self.extracting_pm(page),
                self.extracting_data(page),
                self.extracting_value(page),
            ]
            temp_list.extend(results)
            self.pure_info.append(temp_list)
        return self.pure_info

    def extracting_pm(self, page):
        # szukanie nazwiska PM
        pm_index = page.index("PROJEKTLEITER")
        pm = page[pm_index + 1]
        return pm

    def extracting_num(self, page):
        # szukanie numeru zamówienia PO
        num_index = page.index("PROJEKTNUMMER")
        num = page[num_index + 1]
        return num

    def extracting_data(self, page):
        # szukanie daty PO i zmiana formatu z "dd. month po niemiecku yyyy" na 'dd.mm.yyyy'
        date_index = page.index("LIEFERTERMIN")

        if page[date_index + 1] == "BEMERKUNG ZUM LIEFERTERMIN":
            date_index = page.index("AUFTRAG ERTEILT AM")

        projectDateTemp = page[date_index + 1].split(", ")
        data_object = datetime.strptime(projectDateTemp[1], "%d. %B %Y")
        projectDate = data_object.strftime("%d.%m.%Y")
        return projectDate

    def extracting_value(self, page):
        # tworzy listę wartości z końcówką "€" i następnie wybiera z nich największą, która stanowi łączna wartość zamówienia"
        proj_value = []
        for el in page:
            if el.endswith("€"):
                proj_value.append(float(el.removesuffix("€").replace(",", ".")))
        return max(proj_value)

    def fileToSaveIn(self):
        # wybór pliku do zapisu
        fileName = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Pliki arkusza", "*.txt"), ("Wszystkie pliki", "*.*")],
        )
        with open(fileName, "w") as file:
            file.write(str(self.pure_info))
            print(f"dane zostały zapisane w plik {fileName}")


root = Tk()
app = MyOrdersReader(root)
root.mainloop()
