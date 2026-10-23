string = input("Inserisci il nome: ")
var = ""

for n in range(len(string) - 1, -1, -1):
    var = var + string[n]

print(var)