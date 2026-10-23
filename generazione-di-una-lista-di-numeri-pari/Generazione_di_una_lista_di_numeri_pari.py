def numeri_pari(n):
    lista_pari = []

    for i in range(1, n + 1):
        if i % 2 == 0:
            lista_pari.append(i)

    return lista_pari


n = int(input("Inserisci un numero intero: "))

lista_numeri_pari = numeri_pari(n)

print("La lista dei numeri pari tra 1 e", n, "è:", lista_numeri_pari)