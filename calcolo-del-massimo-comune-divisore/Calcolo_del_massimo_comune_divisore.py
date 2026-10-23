numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))

a = numero1
b = numero2

while b != 0:
    resto = a % b
    a = b
    b = resto

print("Il MCD è:", a)