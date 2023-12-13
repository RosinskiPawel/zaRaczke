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
        self.output_date = []
        self.output_value = []

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
        self.label3 = Label(
            root,
            text="Enter the start date (rrrr-mm-dd). Limit: 367 days: ",
        )
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
        self.btn2 = Button(root, text="Proceed", command=self.data_scraping)
        self.btn2.pack(side="top", anchor="w", padx=5, pady=5)

        # save-button
        self.btn3 = Button(root, text="Save in DB", command=self.write_to_data_DB)
        self.btn3.pack(side="top", anchor="w", padx=5, pady=5)

        self.plot_button = Button(root, text="Plot Chart", command=self.plot_chart)
        self.plot_button.pack(side="top", anchor="w", padx=5, pady=5)

        # Matplotlib figure
        self.figure = Figure(figsize=(10, 6), dpi=100)
        self.ax = self.figure.add_subplot(111)

        # Canvas to embed the Matplotlib figure in Tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side="top", padx=5, pady=5)

    def plot_chart(self):
        # self.ax.clear()
        dates_DB, values_DB = self.get_data_from_DB()
        values_DB = [float(value) for value in values_DB]
        data = {
            "value": values_DB,
            "date": dates_DB,
        }
        df = pd.DataFrame(data)
        df.plot(y="value", x="date", ax=self.ax, kind="line", legend=False)

        self.canvas.draw()

    def get_inputs(self):
        self.currency_code = self.entry1.get()
        print(self.currency_code)
        self.start_date = self.entry2.get()
        self.end_date = self.entry3.get()

    def request_info(self):
        url = f"http://api.nbp.pl/api/exchangerates/rates/a/{self.currency_code}/{self.start_date}/{self.end_date}/"
        print(url)
        page = requests.get(url)
        all_date = page.json()
        return all_date

    def data_scraping(self):
        output_date_temp = []
        currency_rates = self.request_info().get("rates")
        for rate in currency_rates:
            output_date_temp.append(rate.get("effectiveDate"))
            self.output_value.append(rate.get("mid"))
        # shorter date format
        self.output_date = [
            datetime.strptime(el, "%Y-%m-%d").strftime("%y/%m/%d")
            for el in output_date_temp
        ]
        return self.output_date, self.output_value

    def open_DB_connection(self):
        self.connection = sqlite3.connect("currencies.db")
        self.cursor = self.connection.cursor()
        return self.cursor

    def close_BD_connection(self):
        self.connection.commit()
        self.connection.close()

    def write_to_data_DB(self):
        self.open_DB_connection()

        create_table = (
            "CREATE TABLE IF NOT EXISTS Currencies(Code TEXT, Date TEXT, Value TEXT);"
        )
        self.cursor.execute(create_table)
        # for i in range(len(self.output_value)):
        for value, date in zip(self.output_value, self.output_date):
            insert_values = (
                "INSERT INTO Currencies(Code, Date, Value) VALUES (?, ?, ?);"
            )
            self.cursor.execute(
                insert_values,
                (self.currency_code, date, value),
            )

        self.close_BD_connection()

    def get_data_from_DB(self):
        values_from_DB = []
        dates_from_DB = []
        self.open_DB_connection()

        self.cursor.execute("SELECT COUNT(*) FROM Currencies;")
        print("Liczba rekordów przed DELETE:", self.cursor.fetchone()[0])

        try:
            query = "SELECT Date, Value FROM Currencies;"
            self.cursor.execute(query)

            for row in self.cursor.fetchall():
                dates_from_DB.append(row[0])
                values_from_DB.append(row[1])
            print(dates_from_DB, values_from_DB)
        except Exception as e:
            print(f"An error occured: {e}")

        finally:
            self.cursor.execute("DELETE FROM Currencies;")
            self.cursor.execute("SELECT COUNT(*) FROM Currencies;")
            print("Liczba rekordów po DELETE:", self.cursor.fetchone()[0])
            self.close_BD_connection()

        return dates_from_DB, values_from_DB

    # def clear_DB(self):
    #     self.cursor.execute("DELETE FROM Currencies;")
    #     self.connection.commit()
    #     self.connection.close()


def main():
    root = Tk()
    root.geometry("1000x800")
    root.resizable(True, True)
    root.title("Currency Analizer")
    app = SearchModul(root)

    root.mainloop()


if __name__ == "__main__":
    main()
