Program do pobieranie ze specyficznych plików PDF określonych informacji

1. Wczytuje z katalogu pliki PDF
2. Pobiera z każdego pliku pierwszą stronę, ponieważ to na niej znajdują się wymagane wartości
3. Konwertuje na tekst
4. Tworzy listę, oczyszcza ze znaków podziału i pustych miejsc
5. Wyszukiwanie słów kluczowych
6. Następnie określanie szukanych wartości na podstawie indeksów słów kluczowych przez dodanie do indeksów liczby 1 lub 2 (w przypadku klucza 'Honorar')
7. Tworzenie listy przy każdej iteracji z zebranymi informacjami (nr. projektu, nazwisko PM, data, wartość)
8. Zapis listy list do pliku .txt
