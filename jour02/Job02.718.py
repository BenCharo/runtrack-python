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


A1 = Auteur("Victor", "Hugo", [])
L1 = Livre("Livre1", A1)
A1.ecrireUnLivre("Livre2")
A1.sePresenter()
A1.listerOeuvre()
