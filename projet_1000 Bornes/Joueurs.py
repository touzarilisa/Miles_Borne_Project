
# coding: utf-8

from Cartes import  Carte,Distance,Attaque,Parade,Botte


class Joueur:

    def __init__(self,nom,table={},cartes=[],score=0):
        """
            initialisation des attributs 
        """
        self.catres=cartes
        self.nom = nom
        self.score=score
        self.table=table
        self.avance, self.limit50=self.Permission_davancer()

    def __repr__(self):
        """
            affichage de Joueur
        """
        return ("Joueur: %s"%self.nom)

    def Permission_davancer(self):  
        """
            determine si mon joueur peut avancer ou pas et avec quelle vitesse
        """
        avance=True
        limit50=False  
        for i,v in self.table.items():
            if v==Attaque("Limite de vitesse"):
                limit50=True
            if v==Attaque("feux rouge"):
                avance=False
            if v==Attaque("Crevaison"):
                avance=False
            if v==Attaque("Panne d'essence"):
                avance=False
            if v==Attaque("Accident"):
                avance=False
        return avance,limit50
    
    
class IA(Joueur):
    """
        Classe IA 
    """
    def __init__(self,nom,table={},cartes=[],score=0):
        """
            initialisation des attributs 
        """
        Joueur.__init__(self,nom,table={},cartes=[],score=0)

    def __repr__(self):
        """
            affichage de l'IA
        """
        return ("IA: %s"%self.nom)

    def lire_board(self):
        """
            Verifie si l'IA est attaquer 
        """
        attaque=[]
        for i,v in self.table.items():
            if type(v)==Attaque:
                attaque.append(i)
        return attaque

    def lire_main(self):
        """
            trie des cartes que l'IA a dans les mains
        """
        botte=[]
        att=[]
        parade=[]
        dist=[]
        for nc,c in enumerate(self.cartes):
            if type(c)==Botte:
                botte.append(nc)
            elif type(c)==Attaque:
                att.append(nc)
            elif type(c)==Parade:
                parade.append(nc)
            elif type(c)==Distance:
                dist.append(nc)
        return botte,att,parade,dist

    def choisir_carte_a_defausser(self)->int:
        """
            choix de la carte à defausser dans le cas ou mon IA va defausser une carte
        """
        if self.lire_main()[2]:
            return self.lire_main()[2][0]
        elif self.lire_main()[3]:
            cartes_distance=[]
            for nc in self.lire_main()[3]:
                cartes_distance.append(self.cartes[nc])
            carte_a_defausser=min(cartes_distance)
            for i in range(len(self.cartes)):
                if self.cartes[i]==carte_a_defausser:
                    jouer=i
        return jouer

    def choisir_carte(self)->int:
        """
            choix de la carte à jouer pour l'IA
        """        
        jouer=7
        if self.lire_main()[0]:
            jouer=self.lire_main()[0][0]

        elif self.lire_board():
            for n_attaque in self.lire_board():
                if n_attaque=='Feux':
                    if (self.lire_main()[2]):
                        for nc in self.lire_main()[2]:
                            if self.cartes[nc]==Parade("feux vert"):
                                jouer=nc
                elif n_attaque=='Etat des roues':
                    if (self.lire_main()[2]):
                        for nc in self.lire_main()[2]:
                            if self.cartes[nc]==Parade("roue de secours"):
                                jouer=nc
                elif n_attaque=='Essence':
                    if (self.lire_main()[2]):
                        for nc in self.lire_main()[2]:
                            if self.cartes[nc]==Parade("Essence"):
                                jouer=nc
                elif n_attaque=='Limite de vitesse':
                    if (self.lire_main()[2]):
                        for nc in self.lire_main()[2]:
                            if self.cartes[nc]==Parade("Fin limite de vitesse"):
                                jouer=nc
                elif n_attaque=='Accident':
                    if (self.lire_main()[2]):
                        for nc in self.lire_main()[2]:
                            if self.cartes[nc]==Parade("Reparation"):
                                jouer=nc
                else:
                    jouer=7

        elif self.lire_main()[3]:
            cartes_distance=[]
            for nc in self.lire_main()[3]:
                cartes_distance.append(self.cartes[nc])
            carte_a_jouer=max(cartes_distance)
            for i in range(len(self.cartes)):
                if self.cartes[i]==carte_a_jouer:
                    jouer=i
                
        return jouer

        
            
    

    
    



      

