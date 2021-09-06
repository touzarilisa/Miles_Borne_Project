
# coding: utf-8


import random
class Jeu:
    """
        Classe Jeu
    """
    def __init__(self,joueurs,totCartes):
        """
            Initialisation des attributs 
        """
        self.joueurs=joueurs
        self.cartes_joueurs=[]
        self.pioche=self.distribuer(totCartes)[1]
        for i in range (len(joueurs)):
            self.cartes_joueurs.append(self.distribuer(totCartes)[0])
    def distribuer(self,totCartes):
        pioche=[]
        """
            Distribuer les cartes pour les joueurs
        """
        for j in self.joueurs:
            random.shuffle(totCartes)
            cartes=random.sample(totCartes, k=6)
            for c in cartes:
                for i,ca in enumerate(totCartes):
                    if (c==ca):
                        totCartes.pop(i)
                    break
        pioche=totCartes
        return cartes,pioche
    def defausser(self,cartes_joueurs,carte):
        """
            Remettre une carte qui est dans la main du joueur dans la pioche 
        """
        for n,ca in enumerate(cartes_joueurs):
            if (carte==ca):
                cartes_joueurs.pop(n)
                break
        self.pioche.append(carte)
    def piocher(self,i):
        """
            Piocher une carte de la pioche pour un joueur
        """
        carte=random.sample(tuple(self.pioche), k=1)
        for m,ca in enumerate(self.pioche):
            if (carte==ca):
                self.pioche.pop(m)
                break
        self.cartes_joueurs[i]+=carte
        

