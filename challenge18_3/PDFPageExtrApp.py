import easygui as gui
from PyPDF2 import PdfReader, PdfWriter



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
