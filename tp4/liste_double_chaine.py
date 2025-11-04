class Node:
    def __init__(self,data):
        self.item = data
        self.next = None 
        self.previous = None 

class List:
    def __init__(self):
        self.first=None
        self.last=None

    #Ajoute un noeud au début
    def add_first(self,item):
        node_item = Node(item) 
        node_item.next = self.first #l'ancien premier noeud
        self.first.previous = node_item #mtn noeud le precede
        self.first = node_item #devient premier
    
    #Ajoute un noeud spécifique au début
    def add_first_select(self, node : Node):
        node.next = self.first #mm logique
        self.first.previous = None 
        self.first = node

    #Ajoute un élem à la fin 
    def add_end(self, item):
        #Si liste vide, first et last pointent vers le meme 
        if self.first == None:
            self.first = Node(item) 
            self.last = self.first
        #Si la liste à un seul élem
        if self.first == self.last: #si premier est dernier
            self.last = Node(item) #ajoute notre noeud
            self.first.next = self.last #2 elem donc suivant est last
            self.last.previous = self.first #cad pointe vers self.first
        #Si plus d'un élem
        else: 
            current = Node(item) #instancie
            self.last.next = current #l'ajoute fin
            current.previous = self.lastself.last = current

    #Noeud en para et non item
    def add_node(self, node): 
        #Si liste vide, first et last pointent vers le meme 
        if self.first == None:
            self.first = node 
            self.last = None
        #Si la liste à un seul élem
        if self.first == self.last: #si premier est dernier
            self.last = node #ajoute notre noeud
            self.first.next = self.last #2 elem donc suivant est last
            self.last.previous = self.first #cad pointe vers self.first
        #Si plus d'un élem
        else: 
            current = node #cad actuel dernier noeud pointe vers ce new noeud
            node.previous = self.last #new noeud pointe le précedent
            self.last.next = current #changer dernier noeud

###  10min45 vidéo1
