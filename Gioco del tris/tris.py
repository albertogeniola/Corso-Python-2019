import random

class Griglia():
    """
    Consideriamo una griglia come di seguito, dove ogni numero indica l'indice
    nella lista celle_disponibili
    7  |  8  |  9
    4  |  5  |  6
    1  |  2  |  3
    """
    def __init__(self):
        self.celle_disponibili = {
            1: ' ',
            2: ' ',
            3: ' ',
            4: ' ',
            5: ' ',
            6: ' ',
            7: ' ',
            8: ' ',
            9: ' '
        }

    def controlla_griglia_piena(self):
        for indice in self.celle_disponibili:
            if self.celle_disponibili[indice] == ' ':
                return False
        return True

    def visualizza(self):
        print(" {} | {} | {} ".format(self.celle_disponibili[7], self.celle_disponibili[8], self.celle_disponibili[9]))
        print(" {} | {} | {} ".format(self.celle_disponibili[4], self.celle_disponibili[5], self.celle_disponibili[6]))
        print(" {} | {} | {} ".format(self.celle_disponibili[1], self.celle_disponibili[2], self.celle_disponibili[3]))
        print("")
        print("")

    def controlla_simboli_uguali_per_indici(self, lista_indici, simbolo):
        for indice in lista_indici:
            if self.celle_disponibili[indice] != simbolo:
                return False
        return True

    def controlla_vincitore(self, simbolo):
        prima_riga_vincente = self.controlla_simboli_uguali_per_indici([7, 8, 9], simbolo)
        seconda_riga_vincente = self.controlla_simboli_uguali_per_indici([4, 5, 6], simbolo)
        terza_riga_vincente = self.controlla_simboli_uguali_per_indici([1, 2, 3], simbolo)

        prima_colonna_vincente = self.controlla_simboli_uguali_per_indici([1, 4, 7], simbolo)
        seconda_colonna_vincente = self.controlla_simboli_uguali_per_indici([2, 5, 8], simbolo)
        terza_colonna_vincente = self.controlla_simboli_uguali_per_indici([3, 6, 9], simbolo)

        diagonale1_vincente = self.controlla_simboli_uguali_per_indici([1, 5, 9], simbolo)
        diagonale2_vincente = self.controlla_simboli_uguali_per_indici([3, 5, 7], simbolo)

        return prima_riga_vincente or seconda_riga_vincente \
               or terza_riga_vincente or prima_colonna_vincente \
               or seconda_colonna_vincente or terza_colonna_vincente \
               or diagonale1_vincente or diagonale2_vincente

    def occupa_cella(self, indice_griglia, simbolo):
        """
        Tenta di occupare la cella puntata da indice_griglia con il simbolo passato come argomento
        :param indice_griglia: Indice da occupare, 0-based
        :param simbolo: Carattere da utilizzare per marcare la cella
        :return: True se l'operazione ha avuto successo, false altrimenti
        """
        if self.celle_disponibili[indice_griglia] == ' ':
            self.celle_disponibili[indice_griglia] = simbolo
            return True
        else:
            return False

    def pulisci(self):
        self.celle_disponibili = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


class VideoGiocatore:
    def __init__(self, name, simbolo):
        self.name = name
        self.simbolo = simbolo

    def esegui_mossa(self, griglia):
        while True:
            print("E' il turno di {}".format(self.name))
            indice_da_riempire = input("Quale cella vuoi riempire tra quelle disponibili [1-9]?: ")
            indice_da_riempire = int(indice_da_riempire)
            if indice_da_riempire < 1 or indice_da_riempire > 9:
                print("Il valore immesso non è valido")
            elif griglia.occupa_cella(indice_da_riempire, self.simbolo):
                return True
            else:
                print("La cella è già stata occupata")


class VideoGiocatoreComputer(VideoGiocatore):
    def __init__(self, simbolo):
        super().__init__("Computer", simbolo)

    def esegui_mossa(self, griglia):
        while True:
            indice_da_riempire = random.randint(1, 9)
            if griglia.occupa_cella(indice_da_riempire, self.simbolo):
                return True


class Partita:
    def __init__(self):
        self.giocatore1 = VideoGiocatore('Videogiocatore1', 'X')
        self.giocatore2 = VideoGiocatoreComputer('O')
        #self.giocatore2 = VideoGiocatore('Videogiocatore2', 'O')
        self.griglia = Griglia()
        self.vincitore = None

    def inizia(self):
        self.giocatore1.name = input("Nome Videogiocatore1: ")
        #self.giocatore2.name = input("Nome Videogiocatore2: ")

        # Una partita si compone dei seguenti passi logici:
        # Chiedo una mossa al VideoGiocatore1
        # Controllo la validità della mossa (la cella non dovrebbe essere già occupata)
        # Controllo se ho un vincitore oppure se ho riempito la griglia. In ambo i casi la partita è finita e
        # dovrò eleggere un vincitore nel primo caso, dichiarerò pareggio nel secondo caso.
        # Se le condizioni precedenti non si sono verificate, ripeterò il processo chiedendo la mossa al giocatore2,
        # e via dicendo.

        # Assumo che cominci sempre il videogiocatore1
        videogiocatore = self.giocatore1

        while True:
            if self.griglia.controlla_vincitore(self.giocatore1.simbolo):
                print("Complimenti {}, hai vinto!".format(self.giocatore1.name))
                self.vincitore = self.giocatore1
                break
            elif self.griglia.controlla_vincitore(self.giocatore2.simbolo):
                print("Complimenti {}, hai vinto!".format(self.giocatore2.name))
                self.vincitore = self.giocatore2
                break
            elif self.griglia.controlla_griglia_piena():
                print("Pareggio!")
                break

            videogiocatore.esegui_mossa(self.griglia)
            self.griglia.visualizza()

            if videogiocatore == self.giocatore1:
                videogiocatore = self.giocatore2
            else:
                videogiocatore = self.giocatore1

        print("La partita è finita.")

partita = Partita()
partita.inizia()
