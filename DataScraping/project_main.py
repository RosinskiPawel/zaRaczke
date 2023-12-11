from bs4 import BeautifulSoup
import requests
import sqlite3
from tkinter import *
from tkinter import filedialog


class SearchModul:
    def __init__(self, root):
        self.root = root

        # currency code to search
        self.label = Label(root, text="Enter the currency code: ")
        self.label.pack(side="top", anchor="w", padx=5, pady=5)
        self.entry1 = Entry(root, width=10)
        self.entry1.pack(side="top", anchor="w", padx=5, pady=5)

        # analyse start date
        self.label2 = Label(root, text="Enter the start date (rrrr-mm-dd): ")
        self.label2.pack(side="top", anchor="w", padx=5, pady=5)
        self.entry2 = Entry(root, width=10)
        self.entry2.pack(side="top", anchor="w", padx=5, pady=5)

        # analyse end date
        self.label3 = Label(root, text="enter the start date (rrrr-mm-dd): ")
        self.label3.pack(side="top", anchor="w", padx=35, pady=5)
        self.entry3 = Entry(root, width=10)
        self.entry3.pack(side="top", anchor="w", padx=35, pady=5)

        # get-button
        self.btn1 = Button(
            root,
            text="Get",
            command=self.get_inputs,
        )
        self.btn1.pack(side="top", anchor="w", padx=5, pady=5)

    def get_inputs(self):
        self.entered_currency = self.entry1.get()
        self.start_date = self.entry2.get()
        self.endDate = self.entry3.get()
        print(self.entered_currency)

    def requestInfo(self):
        self.currency_code = input("podaj kod waluty")
        self.startDate = input("podaj początek zakresu (rrrr-mm-dd)")
        self.endDate = input("podaj koniec zakresu (rrrr-mm-dd)")

        url = f"http://api.nbp.pl/api/exchangerates/rates/A/{self.currency_code}/{self.startDate}/{self.endDate}/"
        page = requests.get(url)
        all_date = page.json()
        return all_date

    def exraction(self):
        output_data = []
        currency_rates = self.requestInfo().get("rates")
        for rate in currency_rates:
            output_data.append((rate.get("effectiveDate"), rate.get("mid")))
        return output_data


def main():
    root = Tk()
    root.geometry("800x600")
    root.resizable(True, True)
    root.title("Currency Analizer")
    app = SearchModul(root)

    root.mainloop()


if __name__ == "__main__":
    main()
