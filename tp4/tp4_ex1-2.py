##Ex1
#Q1
class Cell: #Sert juste à initialiser cellule
    def __init__(self, valeur=None,precedent=None,suivant=None):
        self.val= valeur
        self.prev= precedent
        self.svt= suivant

#Q2
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

#Q3
    def est_vide(self):
        return self.size == 0
    def len(self):
        return self.size
    def head(self):
        return self.tete
    def tail(self):
        return self.queue

##Ex2
    #Q1
    def insert(self, item: int, neighbor: Cell, after: bool = True) -> LinkedList:
        if self.est_vide():
            return False
        courant = self.tete
        if after==True:
            if courant.val == neighbor:
                nouveau = Cell(item)
                suivant = courant.svt

                # insérer entre courant et suivant
                courant.svt = nouveau
                nouveau.prev = courant
                nouveau.svt = suivant
                suivant.prev = nouveau
        return False 

    #Q2
    def insert_tete(self, x):
        
        self.size += 1

    def insert_fin(self, x):
        
        self.size += 1