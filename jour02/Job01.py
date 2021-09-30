class Personne:                 #classe Personne
    def __init__(self, prenom, nom):    #Constructeur
        self.prenom = prenom
        self.nom = nom

    def sePresenter(self):
        print(self.nom, self.prenom)

    def getPrenom(self):            #accesseurs
        return self.prenom

    def getNom(self):
        return self.nom

    def setPrenom(self, prenom):    #mutateurs
        self.prenom = prenom

    def setNom(self, nom):
        self.nom = nom


P1 = Personne("Benjamin", "Bigot")
P2 = Personne("Jean", "Dupont")
P3 = Personne("Victor", "Hugo")
P1.sePresenter()
P2.sePresenter()
P3.sePresenter()
P2.setNom("Durant")
P2.sePresenter()
print(P3.getPrenom())