from PyPDF2 import PdfReader
from pathlib import Path
from datetime import datetime
from tkinter import *
from tkinter import filedialog


class MyOrdersReader:
    # def __init__(self):
    #     self.list_pages = []

    def __init__(self, root):
        self.root = root
        self.chosen_files = []
        self.list_pages = []

        self.btn_open = Button(
            root,
            text="Select folder to open",
            bg="#EEE9BF",
            font=("Courier,15,bold"),
            command=self.openFiles,
        )
        self.btn_open.pack()

        self.btn2_save = Button(
            root,
            text="Select file to save",
            bg="#EEE9BF",
            font=("Courier,15,bold"),
            command=self.fileToSaveIn,
        )
        self.btn2_save.pack()

        self.btn3_convert = Button(
            root,
            text="Convert",
            bg="#EEE9BF",
            font=("Courier,15,bold"),
            command=self.action,
        )
        self.btn3_convert.pack()

        self.btn4_exit = Button(
            root, text="Exit", bg="#EEE9BF", font=("Courier,15,bold"), command=exit
        )
        self.btn4_exit.pack()

    def openFiles(self):
        self.chosen_files = filedialog.askopenfilenames(
            defaultextension=".pdf",
            filetypes=[("Pliki PDF", "*.pdf"), ("Wszystkie pliki", "*.*")],
        )

    def action(self):
        self.gettingFirstPages()
        self.converting()

    def gettingFirstPages(self):
        # filesList = ("C:/CODING/pdfToRead.pdf", "C:/CODING/pdfToRead2.pdf")
        # lista list z przekonwertowanymi pierwszymi stronami plików pdf

        # dla kazdego pliku z listy otwartych plikow
        # for file in filesList:
        for file in self.chosen_files:
            pdfPath = Path(file)
            pdf_file = PdfReader(str(pdfPath))
            main_page = pdf_file.pages[0]
            # konwersja na tekst
            converted_page = main_page.extract_text()
            # z uwagi na trudne formatowanie tekstu zostaje on zamieniony na liste, a elementy sa dzielone na podstawie znaku nowego wiersza \n
            page_as_list = converted_page.split("\n")

            #     for el in page_as_list:
            #         page_as_list.remove(el) if el == " " else el
            #         list_pages.append(page_as_list)
            # print(list_pages)
            # usuwanie pustych elementow, aby bylo latwiej okreslac indeksy
            cleaned_list = [el.strip() for el in page_as_list if el.strip()]
            # dodwanie do listy oczyszczonych list
            self.list_pages.append(cleaned_list)

        return self.list_pages

    def converting(self):
        pure_info = []
        for page in self.list_pages:
            temp_list = []
            results = [
                self.extracting_num(page),
                self.extracting_pm(page),
                self.extracting_data(page),
                self.extracting_value(page),
            ]
            temp_list.extend(results)
            pure_info.append(temp_list)
        print(pure_info)

    def extracting_pm(self, page):
        pm_index = page.index("PROJEKTLEITER")
        pm = page[pm_index + 1]
        return pm

    def extracting_num(self, page):
        num_index = page.index("PROJEKTNUMMER")
        num = page[num_index + 1]
        return num

    def extracting_data(self, page):
        date_index = page.index("LIEFERTERMIN")
        projectDateTemp = page[date_index + 1].split(", ")
        data_object = datetime.strptime(projectDateTemp[1], "%d. %B %Y")
        projectDate = data_object.strftime("%d.%m.%Y")
        return projectDate

    def extracting_value(self, page):
        proj_value = []
        for el in page:
            if el.endswith("€"):
                proj_value.append(float(el.removesuffix("€").replace(",", ".")))
        return max(proj_value)

    # def extracting_value(self):
    #     proj_value = []
    #     for page in self.list_pages:
    #         for el in page:
    #             if el.endswith("€"):
    #                 proj_value.append(float(el.removesuffix("€").replace(",", ".")))
    #     return proj_value

    def fileToSaveIn(output):
        fileName = filedialog.askopenfilename(
            defaultextension="xls",
            filetypes=[("Pliki arkusza", "*.xls"), ("Wszystkie pliki", "*.*")],
        )
        with open(fileName, "w") as file:
            file.write(output)
            print(f"dane zostały zapisane w plik {fileName}")


# app = MyOrdersReader()


# def main():
#     app.gettingFirstPages()
#     app.converting()


# main()

root = Tk()
app = MyOrdersReader(root)
root.mainloop()


# root = Tk()
# root.geometry("500x300")
# root.resizable(False, False)
# root.title("PDF to Excel")
# root.config(bg="#EEE9BF")

# lb = Label(root, text="PO's Reader and Convert", bg="#EEE9BF", font=("Arial,15,bold"))
# lb.pack(pady=10)


# btn1 = Button(
#     root,
#     text="Select folder to open",
#     bg="#EEE9BF",
#     font=("Courier,15,bold"),
#     command=openFiles,
# )
# btn1.place(x=140, y=70)
# btn2 = Button(
#     root,
#     text="Select file to save",
#     bg="#EEE9BF",
#     font=("Courier,15,bold"),
#     command=fileToSaveIn,
# )
# btn2.place(x=140, y=120)

# btn3 = Button(
#     root,
#     text="Convert",
#     bg="#EEE9BF",
#     font=("Courier,15,bold"),
#     command=gettingFirstPages,
# )
# btn3.place(x=140, y=200)
# btn4 = Button(root, text="Exit", bg="#EEE9BF", font=("Courier,15,bold"), command=exit)
# btn4.place(x=145, y=250)
# root.mainloop()


# def exit(self):
#     self.root.destroy()


# # wczytuje plik pdf
# pdf_path = Path("C:/CODING/pdfToRead2.pdf")
# pdf = PdfReader(str(pdf_path))
# # pobiera 1.stronę
# first_page = pdf.pages[0]
# # konwertuje na tekst
# pageToWord = first_page.extract_text()

# # tekst ma wiele lini konca wiersza, więc tworzona jest lista z podziałem konca wiersza '\n'
# pageL = pageToWord.split("\n")
# # usuwanie pustych miejsc
# for el in pageL:
#     pageL.remove(el) if el == " " else el
# print(pageL)


# # # indeksy dla słow kluczowych

# projectPM_index = pageL.index("PROJEKTLEITER")
# projectNum_index = pageL.index("PROJEKTNUMMER")
# projectDate_index = pageL.index("LIEFERTERMIN")
# # projectValue_index = pageL.index("Honorar")
# projValue = []
# # tu szuka el z końcówą "€", tworzy listę wartości, usuwa "€", zamienia ',' na '.' i tworzy ze stringów liczby zmiennoprzecinkowe, aby wyszukać największą, która jest sumą w euro na zamówieniu PO
# for el in pageL:
#     if el.endswith("€"):
#         projValue.append(float(el.removesuffix("€").replace(",", ".")))
# print(projValue)
# # wartości dla kluczy
# projectPM = pageL[projectPM_index + 1]
# projectNumber = pageL[projectNum_index + 1]
# # projectValue = pageL[projectValue_index + 2]
# projectValue = max(projValue)

# # modyfikcja zapisu daty
# projectDateTemp = pageL[projectDate_index + 1].split(", ")
# data_object = datetime.strptime(projectDateTemp[1], "%d. %B %Y")
# projectDate = data_object.strftime("%d.%m.%Y")


# print(
#     f"Nr projektu: {projectNumber}; PM: {projectPM}; data: {projectDate}, wartość {projectValue}"
# )


# # first = Invoice(122, 34, "DF", 23112023, 150)
# # print(first.name)
# # print(first.toList()[3])
