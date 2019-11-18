"""
Given a list of elements, remove all the duplicates and print all the elements in a DESC sorted manner

Hint!
There are two ways for doing so... one is to use low memory and much CPU,
the other way around is to use more memory and less CPU.
"""

dati = [50, 48, 0, 10, 22, 5, 37, 22, 50, 19, 32, 42, 21, 5, 4, 16, 44, 42, 21, 7, 28, 43, 47, 33, 13, 8, 50, 29, 35, 12,
        39, 44, 36, 46, 45, 26, 13, 50, 37, 1, 31, 30, 6, 18, 38, 14, 31, 2, 25, 1, 41, 1, 20, 43, 50, 28, 30, 25, 33,
        4, 11, 36, 49, 24, 7, 29, 32, 2, 10, 11, 2, 0, 43, 31, 3, 42, 39, 39, 28, 29, 8, 4, 6, 5, 5, 13, 49, 16, 25, 1,
        32, 24, 27, 48, 27, 9, 22, 14, 5, 10, 0]


# Attempt 1: CPU-Iterative way with logic error
# for elemento_scansionato in dati:
#     occorrenze = 0
#
#     for elemento2 in dati:
#         if elemento2 == elemento_scansionato:
#             occorrenze = occorrenze + 1
#         if occorrenze == 1:
#             dati.remove(elemento2)
#
# print(dati)


# Soluzione barando: creo una nuova lista di appoggio, effettuo il calcolo e poi ne aggiorno il puntatore...
# Creo una nuova lista vuota
dati_senza_duplicati = []

# Ciclo sulla lista originale
for elemento_scansionato in dati:
    # Per ogni elemento che trovo, lo aggiungo alla lista senza duplicati solo se questo non vi è già presente
    if elemento_scansionato not in dati_senza_duplicati:
        dati_senza_duplicati.append(elemento_scansionato)

dati = dati_senza_duplicati
print(dati)


dati = [50, 48, 0, 10, 22, 5, 37, 22, 50, 19, 32, 42, 21, 5, 4, 16, 44, 42, 21, 7, 28, 43, 47, 33, 13, 8, 50, 29, 35, 12,
        39, 44, 36, 46, 45, 26, 13, 50, 37, 1, 31, 30, 6, 18, 38, 14, 31, 2, 25, 1, 41, 1, 20, 43, 50, 28, 30, 25, 33,
        4, 11, 36, 49, 24, 7, 29, 32, 2, 10, 11, 2, 0, 43, 31, 3, 42, 39, 39, 28, 29, 8, 4, 6, 5, 5, 13, 49, 16, 25, 1,
        32, 24, 27, 48, 27, 9, 22, 14, 5, 10, 0]

# Attempt 2: Using another data structure as helper
senza_duplicati = set(dati)
senza_duplicati_lista = list(senza_duplicati)
senza_duplicati_lista.sort()
senza_duplicati_lista.reverse()
print(senza_duplicati_lista)
