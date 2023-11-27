skryp do odczytu określonych wartości ze specyficznych plików PDF

1. Wczytuje plik PDF
2. Pobiera 1. stronę z pliku, ponieważ potrzebne wartości są na 1. stronie
3. Konwersja na tekst
4. Z uwagi na układ pliku PDF po konwersji tekst zawiera wiele znaków końca linii \n
5. Utworzenie listy z podziałem '\n'
6. Usunięcie pustych wartości z listy ' '.
7. Szukanie indeksów dla słów kluczowych
8. Następnie określanie na podstawie tych indeksów szukanych wartości przez dodanie do indeksów liczby 1 lub 2 (w przypadku klucza Honorar)
