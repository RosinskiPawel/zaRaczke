# PODSTAWA:
# Cykliczne sprawdzanie w ustawionym okresie czasu wartości EUR do PLN i zapisywanie w bazie danych (watrość i godzina).
# OPCJA:
# Utworzenie wykresu zmienności ceny EUR do PLN w czasie.

from bs4 import BeautifulSoup
import requests
import sqlite3

# url = "https://www.scrapethissite.com/pages/simple/"
# url = "http://api.nbp.pl/api/exchangerates/tables/A/"
# page = requests.get(url)
# data = page.json()
# print(data[1])
# soup = BeautifulSoup(page.text, "html.parser")


# countries = soup.find_all(class_="country-name")
# capitals = soup.find_all(class_="country-capital")
# population = soup.find_all(class_="country-population")

# list_countries = []
# list_capitals = []
# list_population = []

# for element in countries:
#     list_countries.append(element.get_text(strip=True))

# # print(list_countries)
# for element in capitals:
#     list_capitals.append(element.get_text(strip=True))
# # print(list_capitals)
# for element in population:
#     list_population.append(element.get_text(strip=True))

# dic = {}
# for count, cap, popul in zip(list_countries, list_capitals, list_population):
#     dic[count] = {"capital": cap, "population": popul}


# for x, y in dic.items():
#     print(f"{x}: {y['population']}")
# ___________________________________

# data_big = [
#     {
#         "table": "A",
#         "no": "238/A/NBP/2023",
#         "effectiveDate": "2023-12-08",
#         "rates": [
#             {"currency": "bat (Tajlandia)", "code": "THB", "mid": 0.1137},
#             {"currency": "dolar amerykański", "code": "USD", "mid": 4.0181},
#             {"currency": "dolar australijski", "code": "AUD", "mid": 2.6546},
#             {"currency": "dolar Hongkongu", "code": "HKD", "mid": 0.5145},
#             {"currency": "dolar kanadyjski", "code": "CAD", "mid": 2.959},
#             {"currency": "dolar nowozelandzki", "code": "NZD", "mid": 2.4699},
#             {"currency": "dolar singapurski", "code": "SGD", "mid": 3.0009},
#             {"currency": "euro", "code": "EUR", "mid": 4.3303},
#             {"currency": "forint (Węgry)", "code": "HUF", "mid": 0.011317},
#             {"currency": "frank szwajcarski", "code": "CHF", "mid": 4.5913},
#             {"currency": "funt szterling", "code": "GBP", "mid": 5.0458},
#             {"currency": "hrywna (Ukraina)", "code": "UAH", "mid": 0.1093},
#             {"currency": "jen (Japonia)", "code": "JPY", "mid": 0.027848},
#             {"currency": "korona czeska", "code": "CZK", "mid": 0.1779},
#             {"currency": "korona duńska", "code": "DKK", "mid": 0.5808},
#             {"currency": "korona islandzka", "code": "ISK", "mid": 0.028849},
#         ],
#     }
# ]

# for x in data_big:
#     c = x.get("rates")
#     for el in c:
#         if el.get("code") == "CHF":
#             print(el.get("mid"))

# ______________________________

# print(d)
# for el in d:
#     if el.get("code") == "CHF":
#         print(el.get("mid"))


# for x in data_big:
#     d = x.get("rates")
#     c = x.get("effectiveDate")
#     for el in d:
#         if el.get("code") == "EUR":
#             print(f"w dniu {c} euro kosztowało {el.get("mid")} PLN.")


# from datetime import datetime

# d = ["2023-01-02", "2023-01-03", "2023-01-04"]
# # d2 = []
# # for x in d:
# #     d2.append(datetime.strptime(x, "%Y-%m-%d").strftime("%y/%m/%d"))
# d3 = [datetime.strptime(x, "%Y-%m-%d").strftime("%y/%m/%d") for x in d]
# print(d3)

import sqlite3

# code = "EUR"
# output_value = ["aa", "bb", "cc", "dd"]
# output_date = ["0.0", "1.1", "2.2", "3.3"]


# def dbEngine():
#     code = input("EUR or USD")
#     output_value = ["aa", "bb", "cc", "dd"]
#     output_date = ["0.0", "1.1", "2.2", "3.3"]
#     connection = sqlite3.connect("currencies.db")
#     cursor = connection.cursor()
#     create_table = (
#         "CREATE TABLE IF NOT EXISTS Currencies(Code TEXT, Date TEXT, Value TEXT);"
#     )
#     cursor.execute(create_table)
#     for i in range(len(output_value)):
#         insert_values = "INSERT INTO Currencies(Code, Date, Value) VALUES (?, ?, ?);"
#         cursor.execute(insert_values, (code, output_value[i], output_date[i]))

#     connection.commit()
#     connection.close()


# # dbEngine()

# connection = sqlite3.connect("currencies.db")
# cursor = connection.cursor()
# query = "SELECT Date, Value FROM Currencies WHERE Code = 'USD';"
# cursor.execute(query)
# for row in cursor.fetchall():
#     print(row[0])
# connection.close()


# ########_____________________________
# from bs4 import BeautifulSoup
# import requests
# import sqlite3
# from tkinter import *
# from matplotlib import pyplot as plt
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import pandas as pd
# from datetime import datetime


# class SearchModul:
#     def __init__(self, root):
#         self.root = root

#         # currency code to search
#         self.label = Label(root, text="Enter the currency code: ")
#         self.label.pack(side="top", anchor="w", padx=5, pady=5)
#         self.entry1 = Entry(root, width=10)
#         self.entry1.pack(side="top", anchor="w", padx=5, pady=5)

#         # analyse start date
#         self.label2 = Label(root, text="Enter the start date (rrrr-mm-dd): ")
#         self.label2.pack(side="top", anchor="w", padx=5, pady=5)
#         self.entry2 = Entry(root, width=10)
#         self.entry2.pack(side="top", anchor="w", padx=5, pady=5)

#         # analyse end date
#         self.label3 = Label(root, text="enter the start date (rrrr-mm-dd): ")
#         self.label3.pack(side="top", anchor="w", padx=5, pady=5)
#         self.entry3 = Entry(root, width=10)
#         self.entry3.pack(side="top", anchor="w", padx=5, pady=5)

#         # get-button
#         self.btn1 = Button(
#             root,
#             text="Get",
#             command=self.get_inputs,
#         )
#         self.btn1.pack(side="top", anchor="w", padx=5, pady=5)

#         # proceed-button
#         self.btn2 = Button(root, text="Save in DB", command=self.writeToDB)
#         self.btn2.pack(side="top", anchor="w", padx=5, pady=5)

#         # self.plot_button = Button(root, text="Plot Chart", command=self.plot_chart)
#         # self.plot_button.pack(side="top", padx=5, pady=10)

#         # # Matplotlib figure
#         # self.figure = Figure(figsize=(10, 6), dpi=100)
#         # self.ax = self.figure.add_subplot(111)

#         # # Canvas to embed the Matplotlib figure in Tkinter
#         # self.canvas = FigureCanvasTkAgg(self.figure, master=root)
#         # self.canvas_widget = self.canvas.get_tk_widget()
#         # self.canvas_widget.pack(side="top", padx=5, pady=5)

#     # def plot_chart(self):
#     #     # dataScraping method returns two values
#     #     output_date, output_value = self.dataScraping()

#     #     data = {
#     #         "value": output_value,
#     #         "date": output_date,
#     #     }
#     #     df = pd.DataFrame(data)
#     #     df.plot(y="value", x="date", ax=self.ax, kind="line", legend=False)

#     #     self.canvas.draw()

#     def get_inputs(self):
#         self.currency_code = self.entry1.get()
#         self.start_date = self.entry2.get()
#         self.end_date = self.entry3.get()

#     def requestInfo(self):
#         url = f"http://api.nbp.pl/api/exchangerates/rates/A/{self.currency_code}/{self.start_date}/{self.end_date}/"
#         page = requests.get(url)
#         all_date = page.json()
#         return all_date

#     def dataScraping(self):
#         output_date_temp = []
#         output_value = []

#         currency_rates = self.requestInfo().get("rates")
#         for rate in currency_rates:
#             output_date_temp.append(rate.get("effectiveDate"))
#             output_value.append(rate.get("mid"))
#         # shorter date format
#         output_date = [
#             datetime.strptime(el, "%Y-%m-%d").strftime("%y/%m/%d")
#             for el in output_date_temp
#         ]
#         return output_date, output_value

#     def writeToDB(self):
#         output_date1, output_value1 = self.dataScraping()
#         connection = sqlite3.connect("currencies_main.db")
#         cursor = connection.cursor()
#         create_table = (
#             "CREATE TABLE IF NOT EXISTS Currencies(Code TEXT, Date TEXT, Value TEXT);"
#         )
#         cursor.execute(create_table)
#         for i in range(len(output_value1)):
#             insert_values = (
#                 "INSERT INTO Currencies(Code, Date, Value) VALUES (?, ?, ?);"
#             )
#             cursor.execute(
#                 insert_values, (self.currency_code, output_value1[i], output_date1[i])
#             )

#         connection.commit()
#         connection.close()


# def main():
#     root = Tk()
#     root.geometry("1000x800")
#     root.resizable(True, True)
#     root.title("Currency Analizer")
#     app = SearchModul(root)

#     root.mainloop()


# if __name__ == "__main__":
#     main()
import json

# currency_code = "eur"
# start_date = "2021-10-10"
# end_date = "2023-10-10"
# url = "http://api.nbp.pl/api/exchangerates/rates/a/usd/2022-10-01/2023-01-01/"
# # url = f"http://api.nbp.pl/api/exchangerates/rates/A/{currency_code}/{start_date}/{end_date}/?format=json"
# url = "http://api.nbp.pl/api/exchangerates/tables/a/today/"
# response = requests.get(url)
# result = response.json()

# print(result)


connection = sqlite3.connect("currencies_del.db")
cursor = connection.cursor()
create_table = (
    "CREATE TABLE IF NOT EXISTS Currencies(Code TEXT, Date TEXT, Value TEXT);"
)
cursor.execute(create_table)
inser_val = "INSERT INTO Currencies VALUES('EUR', '2023-01-03', '4.8988')"
cursor.execute(inser_val)
cursor.execute("SELECT COUNT(*) FROM Currencies;")
print("Liczba rekordów przed DELETE:", cursor.fetchone()[0])

cursor.execute("DELETE FROM Currencies;")

cursor.execute("SELECT COUNT(*) FROM Currencies;")
print("Liczba rekordów po DELETE:", cursor.fetchone()[0])


connection.commit()
connection.close()

# connection = sqlite3.connect("currencies_del.db")
# cursor = connection.cursor()
# cursor.execute("DELETE FROM Currencies;")
