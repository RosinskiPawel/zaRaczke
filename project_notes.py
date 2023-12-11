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


from datetime import datetime

d = ["2023-01-02", "2023-01-03", "2023-01-04"]
# d2 = []
# for x in d:
#     d2.append(datetime.strptime(x, "%Y-%m-%d").strftime("%y/%m/%d"))
d3 = [datetime.strptime(x, "%Y-%m-%d").strftime("%y/%m/%d") for x in d]
print(d3)
