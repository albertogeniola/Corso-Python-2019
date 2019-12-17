#  0 | 1 | 2
#  3 | 4 | 5
#  6 | 7 | 8


class Griglia():
    def __init__(self):
        self.celle_disponibili = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def visualizza(self):
        print(" {} | {} | {} ".format(self.celle_disponibili[0], self.celle_disponibili[1], self.celle_disponibili[2]))
        print(" {} | {} | {} ".format(self.celle_disponibili[3], self.celle_disponibili[4], self.celle_disponibili[5]))
        print(" {} | {} | {} ".format(self.celle_disponibili[6], self.celle_disponibili[7], self.celle_disponibili[8]))
        print("")
        print("")

    def occupa_cella(self, indice_griglia, simbolo):
        if self.celle_disponibili[indice_griglia] == ' ':
            self.celle_disponibili[indice_griglia] = simbolo
        else:
            print("Attenzione, la cella è già stata occupata!")

    def pulisci(self):
        self.celle_disponibili = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


class VideoGiocatore:
    def __init__(self, name, simbolo):
        self.name = name
        self.simbolo = simbolo

    def chiedi_mossa(self):
        while True:
            print("E' il turno di {}".format(self.name))
            indice_da_riempire = input("Quale cella vuoi riempire tra quelle disponibili?")
            indice_da_riempire = int(indice_da_riempire)
            if indice_da_riempire < 0 or indice_da_riempire > 8:
                print("Il valore immesso non è valido")
            else:
                return indice_da_riempire



p1 = VideoGiocatore("Alberto", 'X')
p1.chiedi_mossa()

#
# griglia_di_gioco = Griglia()
# griglia_di_gioco.occupa_cella(1, 'X')
# griglia_di_gioco.visualizza()
# griglia_di_gioco.occupa_cella(2, 'O')
# griglia_di_gioco.visualizza()
