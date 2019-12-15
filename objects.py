class Livre:
    def __init__(self, auteur, titre) :
        self.auteur = auteur
        self.titre = titre

    def getDescription(self) :
        return self.titre + " de " + self.auteur

l1 = Livre("Victor Hugo", "Les Misérables")
print(l1.getDescription())

l2 = Livre("Albert Camus", "L'écume des jours")
print(l2.getDescription())


class Roman(Livre):
    def __init__(self, auteur, titre, annee):
        super().__init__(auteur, titre)
        self.annee = annee

    def getDescription(self) :
        return Livre.getDescription(self) + " en " + str(self.annee)


l3 = Roman("Jean-Paul Sartre", "Les Mots", 1964)
print(l3.getDescription())    