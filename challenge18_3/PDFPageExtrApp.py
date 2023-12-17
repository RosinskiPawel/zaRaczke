import easygui as gui
from PyPDF2 import PdfReader, PdfWriter


# path = gui.fileopenbox(title="Select")
# if path is None:
#     exit()


# gui.msgbox(msg="To ja!", title="WTF", ok_button="Click me")
# choices1 = ("YES", "NO", "DON'T KNOW")
# butn = gui.buttonbox(msg="Click one button", title="buttons", choices=choices1)

# print(butn)

# wybor = gui.enterbox(
#     msg="Enter name",
#     title="Name"
#     )
# print(wybor)


# file_to_open = gui.fileopenbox(msg="Select a file")
# print(file_to_open)
# gui.enterbox(msg="What is your name?")
# class PageRotator:
#     def open_file(self):
#         input_path = gui.fileopenbox(msg="Open a PDF file", title="PDF FILES")
#         if input_path is None:
#             exit()
#         return input_path

#     def select_degrees(self):
#         degrees = ("90", "180", "270")
#         choice = gui.buttonbox(msg="Choose degrees:", title="Degrees", choices=degrees)
#         return int(choice)

#     def save_path(self):
#         output_path = gui.filesavebox(
#             msg="choose the location", title="Where to save file"
#         )
#         while output_path == input_path:
#             gui.msgbox(msg="Cannot overwrite the original file!")
#             output_path = gui.filesavebox(
#                 msg="choose the location", title="Where to save file"
#             )
#         if output_path is None:
#             exit()

#     def rotation(self):
#         input_file = PdfReader(self.open_file())
#         output_pdf = PdfWriter()

#         for page in input_file.pages:
#             page = page.rotate(self.select_degrees())
#             output_pdf.add_page(page)
#         with open(self.save_path(), "wb") as output_file:
#             output_pdf.write(output_file)


# app = PageRotator()


# def main():
#     app.rotation()


# if __name__ == "__main__":
#     main()


# class PageRotator:
#     def open_file(self):
#         input_path = gui.fileopenbox(
#             msg="Open a PDF file", title="PDF FILES", default="*.pdf"
#         )
#         if input_path is None:
#             exit()
#         return input_path

#     def select_degrees(self):
#         degrees = ("90", "180", "270")
#         choice = gui.buttonbox(msg="Choose degrees:", title="Degrees", choices=degrees)
#         return int(choice)

#     def save_path(self, input_path):
#         output_path = gui.filesavebox(
#             msg="Choose the location", title="Where to save file"
#         )
#         while output_path == input_path:
#             gui.msgbox(msg="Cannot overwrite the original file!")
#             output_path = gui.filesavebox(
#                 msg="Choose the location", title="Where to save file", default="*.pdf"
#             )
#         if output_path is None:
#             exit()
#         return output_path

#     def rotation(self):
#         input_path = self.open_file()
#         input_file = PdfReader(input_path)
#         output_pdf = PdfWriter()

#         for page in input_file.pages:
#             rotated_page = page.rotate(self.select_degrees())
#             output_pdf.add_page(rotated_page)

#         output_path = self.save_path(input_path)

#         with open(output_path, "wb") as output_file:
#             output_pdf.write(output_file)


# app = PageRotator()


# def main():
#     app.rotation()


# if __name__ == "__main__":
#     main()

# input_path = gui.fileopenbox(title="Open PDF-File", default="*.pdf")
# if input_path is None:
#     exit()

# choices3 = ("90", "180", "270")
# choosen_rotat = gui.buttonbox(msg="Chose", choices=choices3)

# output_path = gui.filesavebox(title="save as", default="*.pdf")
# while input_path == output_path:
#     gui.msgbox(msg="file exists")
#     output_path = gui.filesavebox(title="save as", default="*.pdf")

# if output_path is None:
#     exit()

# input_file = PdfReader(input_path)
# output_pdf = PdfWriter()

# for page in input_file.pages:
#     page = page.rotate(int(choosen_rotat))
#     output_pdf.add_page(page)

# with open(output_path, "wb") as output_file:
#     output_pdf.write(output_file)


# ________________


class PageExtract:
    def open_file(self):
        open_path = gui.fileopenbox(msg="Open file", default="*.pdf")
        if open_path is None:
            exit()

        return open_path

    def starting_page(self):
        return self.enter_page("starting")

    def ending_page(self):
        return self.enter_page("ending")

    def enter_page(self, page):
        page_num = gui.enterbox(msg=f"enter the {page} page")

        while int(page_num) < 1:
            gui.msgbox(msg="invalide page number. The number must be bigger then 0.")
            page_num = gui.enterbox(msg=f"enter the {page} page")
        if page_num is None:
            exit()

        return int(page_num)

    def save_path(self, open_path):
        output_path = gui.filesavebox(msg="save as", default="*.pdf")
        while output_path == open_path:
            gui.msgbox(msg="Cannot overwrite the file.")
            output_path = gui.filesavebox(msg="save as", default="*.pdf")
        if output_path is None:
            exit()
        return output_path

    def extract(self):
        input_path = self.open_file()
        input_file = PdfReader(input_path)
        output_pdf = PdfWriter()
        start = self.starting_page()
        end = self.ending_page()

        for n in range(start, end + 1):
            page = input_file.pages[n - 1]
            output_pdf.add_page(page)

        out_path = self.save_path(input_path)

        with open(out_path, "wb") as output_file:
            output_pdf.write(output_file)


app = PageExtract()
app.extract()
