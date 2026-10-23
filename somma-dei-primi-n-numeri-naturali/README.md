# Somma dei primi N numeri naturali

Dovrebbe calcolare la somma dei numeri naturali da 1 a N.

## Come funziona

Se `N > 0`, accumula in `somma` i valori da 1 a N con un ciclo `for`.

## Requisiti

- Python 3 (nessuna libreria esterna)

## Esecuzione

```bash
python Somma_dei_primi_N_numeri_naturali.py
```

## Esempio di esecuzione

```text
inserisci un numero: 5
la somma dei numeri è
la somma dei numeri è
la somma dei numeri è
la somma dei numeri è
la somma dei numeri è
```

## Note

**Problema noto:** il `print` è dentro il ciclo e stampa solo il testo "la somma dei numeri è", senza il valore di `somma`. Per correggere basta spostare un `print("la somma dei numeri è", somma)` fuori dal ciclo.

## Struttura

```text
somma-dei-primi-n-numeri-naturali/
├── Somma_dei_primi_N_numeri_naturali.py
├── README.md
└── .gitignore
```
