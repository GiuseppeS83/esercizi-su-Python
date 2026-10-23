var = 0

N = int(input("Inserisci il primo numero: "))
M = int(input("Inserisci il secondo numero: "))

for i in range(1, M + 1):
    var = var + N

print("Il primo numero è:", N)
print("Il secondo numero è:", M)
print("Il risultato è:", var)