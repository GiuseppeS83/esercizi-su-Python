string = input("Inserisci una stringa: ")

lunghezza = len(string)

sinistra = 0
destra = lunghezza - 1

palindromo = True

while sinistra < destra:
    if string[sinistra] != string[destra]:
        palindromo = False
        break

    sinistra += 1
    destra -= 1

if palindromo:
    print("La stringa è palindroma")
else:
    print("La stringa non è palindroma")