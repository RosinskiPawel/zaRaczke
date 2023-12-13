def bubble(liczby):
    for z in range(len(liczby)):
        for i in range(len(liczby) - 1):
            if liczby[i] > liczby[i + 1]:
                liczby[i], liczby[i + 1] = liczby[i + 1], liczby[i]
            else:
                continue
    print(liczby)


bubble([1, 2, 5, 3, 1, 7, 9, 1, 12, 83, 1, 5, 3, 2])
# lista_do_sort = [44, 7, 33, -2, 1, 4, 0]
# posort = bubble(lista_do_sort)
# print(posort)
