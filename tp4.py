#Ex1
class Cell: #Sert juste à initialiser cellule
    def __init__(self, valeur=None,precedent=None,suivant=None):
        self.val= valeur
        self.prev= precedent
        self.svt= suivant

class LinkedList: #pour modifs et commandes
    def __init__(self,premier=None,dernier=None):
        self.size = 0
        self.tete=premier
        self.queue=dernier
        if self.tete != None and self.queue != None:
            self.tete.svt=self.queue
            self.queue.prev=self.tete
            self.tete.prev = self.queue
            self.queue.svt = self.tete

    def est_vide(self):
        return self.size == 0

































    def len(self):
        f"""
        - Function allowing to know the size of our list 
        :return: {int} The current size of the list
        """

        return self.size

    def head(self) -> IntLLCell:
        f"""
        - Function to know the first element of the chained list
        :return: {IntLLCell} The first cell of the list
        """

        return self.first_cell

    def tail(self) -> IntLLCell:
        f"""
        - Function to know the last element of the chained list
        :return: {IntLLCell} The last cell of the list
        """

        return self.last_cell




    def ajoutTete(self, x):
        nouveau = Cell(x, self.tete) #rajoute au new élément un lien sorti désignant liste initiale
        self.tete = nouveau  #peut mtn rattacher la meme tete à la new liste
    #EX FACULTATIF:
    def ajoutApresValeur(self, x, y):
        nouveau = Cell(y) #créer new élément avec valeur y (et x désigant None)
        courant = self.tete
        while courant!= None & courant.val != x: #parcourir liste jusqu'à trouver x ou None
            courant=courant.svt
        #en dehors du while, courant est soit None (x pas trouvé) soit le Cell avec val x
        if courant != None: #x trouvé
            nouveau.svt = courant.svt #le suivant du new Cell est le suivant de courant
            courant.svt = nouveau #le suivant de courant est le new Cell
    def ajoutFin(self, x):
        mx = Cell(x)
        if self.tete is None: #liste vide
            self.tete = mx
        else:
            lpred = self.tete
            lsvt = lpred.svt
            while lsvt is not None: #insertion après lpred
                lpred=lsvt
                lsvt=lsvt.svt
            lpred.svt = mx

#Ex2

#Ex3
