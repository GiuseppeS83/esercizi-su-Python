def conta_vocali(s):
    vocali = "aeiouAEIOU"
    contatore=0
    for carattere in s:
        if carattere in vocali:
            contatore +=1
    return contatore
stringa = input("inserisci una stringa:")
numero_vocali = conta_vocali(stringa)
print("il numero di vocaliin",stringa, "è:", numero_vocali)
