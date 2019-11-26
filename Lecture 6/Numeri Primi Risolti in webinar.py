def controlla_se_primo(numero):
    for possibile_divisore in range(1, numero+1):
        e_divisore = (numero % possibile_divisore) == 0
        if e_divisore and possibile_divisore != 1 and possibile_divisore != numero:
            print("Il numero {} non è primo (trovato il divisore {})".format(numero, possibile_divisore))
            return False
    return True


def controlla_fino_a(limite):
    numeri_primi = []
    for numero_da_controllare in range(1, limite+1):
        primo = controlla_se_primo(numero_da_controllare)
        if primo:
            numeri_primi.append(numero_da_controllare)

    return numeri_primi


def menu_utente():
    input_utente = input("Premere q per uscire, altrimenti inserire il numero limite per il calcolo dei primi: ")
    while input_utente != 'q':
        if not input_utente.isdigit():
            print("Valore inserito non valido")
        else:
            limite_intero = int(input_utente)
            numeri_primi = controlla_fino_a(limite_intero)
            print(numeri_primi)

        input_utente = input("Premere q per uscire, altrimenti inserire il numero limite per il calcolo dei primi: ")

    print("Ciao e grazie!")

menu_utente()