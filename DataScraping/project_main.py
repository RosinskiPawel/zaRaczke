from bs4 import BeautifulSoup
import requests
import sqlite3
from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd


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
        self.label3.pack(side="top", anchor="w", padx=5, pady=5)
        self.entry3 = Entry(root, width=10)
        self.entry3.pack(side="top", anchor="w", padx=5, pady=5)

        # get-button
        self.btn1 = Button(
            root,
            text="Get",
            command=self.get_inputs,
        )
        self.btn1.pack(side="top", anchor="w", padx=5, pady=5)

        self.plot_button = Button(root, text="Plot Chart", command=self.plot_chart)
        self.plot_button.pack(side="top", padx=5, pady=10)

        # Matplotlib figure
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)

        # Canvas to embed the Matplotlib figure in Tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side="top", padx=5, pady=5)

    def plot_chart(self):
        # plt.plot([1, 2, 3, 4, 3, 2, 5, 3])
        # plt.show()
        output_data, _ = self.exraction()
        _, output_value = self.exraction()
        data = {
            "value": output_value,
            "date": output_data,
        }
        df = pd.DataFrame(data)
        df.plot(y="value", x="date", ax=self.ax, kind="line", legend=False)

        self.canvas.draw()

    def get_inputs(self):
        self.currency_code = self.entry1.get()
        self.startDate = self.entry2.get()
        self.endDate = self.entry3.get()

    def requestInfo(self):
        # self.currency_code = input("podaj kod waluty")
        # self.startDate = input("podaj początek zakresu (rrrr-mm-dd)")
        # self.endDate = input("podaj koniec zakresu (rrrr-mm-dd)")

        url = f"http://api.nbp.pl/api/exchangerates/rates/A/{self.currency_code}/{self.startDate}/{self.endDate}/"
        page = requests.get(url)
        all_date = page.json()
        return all_date

    # def exraction(self):
    #     output_data = []
    #     currency_rates = self.requestInfo().get("rates")
    #     for rate in currency_rates:
    #         output_data.append((rate.get("effectiveDate"), rate.get("mid")))
    #     return output_data
    def exraction(self):
        output_data = []
        output_value = []
        currency_rates = self.requestInfo().get("rates")
        for rate in currency_rates:
            output_data.append(rate.get("effectiveDate"))
            output_value.append(rate.get("mid"))
        return output_data, output_value


def main():
    root = Tk()
    root.geometry("800x600")
    root.resizable(True, True)
    root.title("Currency Analizer")
    app = SearchModul(root)

    root.mainloop()


if __name__ == "__main__":
    main()
