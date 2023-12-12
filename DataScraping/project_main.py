from bs4 import BeautifulSoup
import requests
import sqlite3
from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from datetime import datetime


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

        # proceed-button
        self.btn2 = Button(root, text="Save in DB", command=self.writeToDB)
        self.btn2.pack(side="top", anchor="w", padx=5, pady=5)

        # self.plot_button = Button(root, text="Plot Chart", command=self.plot_chart)
        # self.plot_button.pack(side="top", padx=5, pady=10)

        # # Matplotlib figure
        # self.figure = Figure(figsize=(10, 6), dpi=100)
        # self.ax = self.figure.add_subplot(111)

        # # Canvas to embed the Matplotlib figure in Tkinter
        # self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        # self.canvas_widget = self.canvas.get_tk_widget()
        # self.canvas_widget.pack(side="top", padx=5, pady=5)

    # def plot_chart(self):
    #     # dataScraping method returns two values
    #     output_date, output_value = self.dataScraping()

    #     data = {
    #         "value": output_value,
    #         "date": output_date,
    #     }
    #     df = pd.DataFrame(data)
    #     df.plot(y="value", x="date", ax=self.ax, kind="line", legend=False)

    #     self.canvas.draw()

    def get_inputs(self):
        self.currency_code = self.entry1.get()
        self.start_date = self.entry2.get()
        self.end_date = self.entry3.get()

    def requestInfo(self):
        url = f"http://api.nbp.pl/api/exchangerates/rates/A/{self.currency_code}/{self.start_date}/{self.end_date}/"
        page = requests.get(url)
        all_date = page.json()
        return all_date

    def dataScraping(self):
        output_date_temp = []
        output_value = []

        currency_rates = self.requestInfo().get("rates")
        for rate in currency_rates:
            output_date_temp.append(rate.get("effectiveDate"))
            output_value.append(rate.get("mid"))
        # shorter date format
        output_date = [
            datetime.strptime(el, "%Y-%m-%d").strftime("%y/%m/%d")
            for el in output_date_temp
        ]
        return output_date, output_value

    def writeToDB(self):
        output_date1, output_value1 = self.dataScraping()
        connection = sqlite3.connect("currencies_main.db")
        cursor = connection.cursor()
        create_table = (
            "CREATE TABLE IF NOT EXISTS Currencies(Code TEXT, Date TEXT, Value TEXT);"
        )
        cursor.execute(create_table)
        for i in range(len(output_value1)):
            insert_values = (
                "INSERT INTO Currencies(Code, Date, Value) VALUES (?, ?, ?);"
            )
            cursor.execute(
                insert_values, (self.currency_code, output_value1[i], output_date1[i])
            )

        connection.commit()
        connection.close()


def main():
    root = Tk()
    root.geometry("1000x800")
    root.resizable(True, True)
    root.title("Currency Analizer")
    app = SearchModul(root)

    root.mainloop()


if __name__ == "__main__":
    main()
