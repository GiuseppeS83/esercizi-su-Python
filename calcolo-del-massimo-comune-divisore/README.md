# Calcolo del massimo comune divisore

Calcola il massimo comune divisore (MCD) di due numeri interi.

## Come funziona

Implementa l'algoritmo di Euclide: finché `b` non è 0 sostituisce la coppia `(a, b)` con `(b, a % b)`. Alla fine `a` è il MCD.

## Requisiti

- Python 3 (nessuna libreria esterna)

## Esecuzione

```bash
python Calcolo_del_massimo_comune_divisore.py
```

## Esempio di esecuzione

```text
Inserisci il primo numero: 48
Inserisci il secondo numero: 18
Il MCD è: 6
```

## Struttura

```text
calcolo-del-massimo-comune-divisore/
├── Calcolo_del_massimo_comune_divisore.py
├── README.md
└── .gitignore
```
