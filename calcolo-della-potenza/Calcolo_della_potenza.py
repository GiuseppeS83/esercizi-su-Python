base = int(input("Inserisci la base: "))

esponente = int(input("Inserisci l'esponente: "))

risultato = 1

for i in range(esponente):
    risultato = risultato * base

print("La potenza è:", risultato)