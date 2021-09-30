class Livre:                    #classe Livre

    def __init__(self, titre, auteur):  #Constructeur
        self.titre = titre
        self.auteur = auteur
        auteur.oeuvre.append(self)      #reference classe auteur

    def afficherLivre(self):
        print(self.titre)


class Personne:                 #classe Personne
    def __init__(self, prenom, nom):    #Constructeur
        self.prenom = prenom
        self.nom = nom

    def sePresenter(self):
        print(self.nom, self.prenom)

    def getPrenom(self):
        return self.prenom

    def getNom(self):
        return self.nom

    def setPrenom(self, prenom):
        self.prenom = prenom

    def setNom(self, nom):
        self.nom = nom


class Auteur(Personne):         #classe Auteur héritant de la classe Personne

    def __init__(self, prenom, nom, oeuvre):         #Constructeur
        super().__init__(prenom, nom)              #appel au constructeur de la classe mère
        self.oeuvre = oeuvre

    def listerOeuvre(self):
        for i in self.oeuvre:
            i.afficherLivre()

    def ecrireUnLivre(self, titre):
        Livre(titre, self)


class Bibliotheque:
    def __init__(self, nom, catalogue):
        self.nom = nom
        self.catalogue = catalogue

    def acheterLivre(self, auteur, titre, quantite):
        list = []
        for liv in auteur.oeuvre:
            list.append(liv.titre)
        if titre in list:
            self.catalogue[titre] = quantite
        else:
            print("Ce livre n'est pas une oeuvre de cet auteur")

    def inventaire(self):
        print("Inventaire de la Bibliothèque : ")
        for titre, quantite in self.catalogue.items():
            print(titre, " : ", quantite)
        print("\n")

    def louer(self, client, titre):
        if self.catalogue[titre] > 0:
            client.collection.append(titre)
            self.catalogue[titre] -= 1
        else:
            print("Ce livre n'est plus en stock")

    def rendreLivres(self, client):
        while len(client.collection) != 0:
            for i in client.collection:
                self.catalogue[i] += 1
                client.collection.remove(i)


class Client(Personne):
    def __init__(self, prenom, nom, collection):
        super().__init__(prenom, nom)
        self.collection = collection

    def inventaire(self):
        print("Inventaire de ", self.prenom, " : ")
        for titre in self.collection:
            print(titre)
        print("\n")



A1 = Auteur("Victor", "Hugo", [])
A2 = Auteur("Francois", "Rabelais", [])
A3 = Auteur("Jean", "De La Fontaine", [])
A1.ecrireUnLivre("Les Miserables")
A1.ecrireUnLivre("Les Chatiments")
A2.ecrireUnLivre("Pantagruel")
A2.ecrireUnLivre("Gargantua")
A3.ecrireUnLivre("Les fables de La Fontaine")
B1 = Bibliotheque("Bibliotheque n°1", {})
B1.acheterLivre(A1, "Les Miserables", 5)
B1.acheterLivre(A2, "Pantagruel", 8)
B1.acheterLivre(A3, "Les fables de La Fontaine", 2)
B1.inventaire()
C1 = Client("Benjamin", "Bigot", [])
B1.louer(C1, "Les Miserables")
B1.louer(C1, "Pantagruel")
B1.inventaire()
C1.inventaire()
B1.rendreLivres(C1)
B1.inventaire()
C1.inventaire()
