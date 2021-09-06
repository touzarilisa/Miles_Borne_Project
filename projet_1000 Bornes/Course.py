
# coding: utf-8


from Joueurs import Joueur,IA
from Jeu import Jeu
from Cartes import  Carte,Distance,Attaque,Parade,Botte
import random

class Course:
    """
        Classe Jeu
    """
    def __init__(self,jeu):
        """
            Initialisation des attributs 
        """
        self.jeu=jeu
        self.tables=[]
        for i in range (len(self.jeu.joueurs)):
            self.tables.append({'Feux':Attaque("feux rouge"), 'Etat des roues':None, 'Essence':None, 'Limite de vitesse':None, 'Accident':None,'Distance':None})

    def __repr__(self):
        """
            Affichage de la course, score et la situations des table  
        """
        print("Score: ")
        for i in range(len(self.jeu.joueurs)):
            print(self.jeu.joueurs[i],": ",self.jeu.joueurs[i].score)
        print("----------------------------\n")    
        print("Conditions :")
        for i in range(len(self.jeu.joueurs)):
            print("Table du ",self.jeu.joueurs[i],": ",self.tables[i])
        return "----------------------------"
    def depotCarte_auto(self,play,player,table_de): 
        """
            Fonction de depot de carte dans le cas ou le joueur est une IA 
        """
        if play==7:
                n_c=self.jeu.joueurs[player].choisir_carte_a_defausser()
                self.jeu.defausser(self.jeu.cartes_joueurs[player],self.jeu.cartes_joueurs[player][n_c])
                self.jeu.piocher(player)
        else:
            carte_a_remettre=None
            a=(self.jeu.cartes_joueurs[player][play]==Botte("Increvable")) or (self.jeu.cartes_joueurs[player][play]==Attaque("Crevaison")) or (self.jeu.cartes_joueurs[player][play]==Parade("roue de secours"))
            b=(self.jeu.cartes_joueurs[player][play]==Botte("Vehicule prioritaire")) or (self.jeu.cartes_joueurs[player][play]==Attaque("feux rouge")) or (self.jeu.cartes_joueurs[player][play]==Parade("feux vert"))
            c=(self.jeu.cartes_joueurs[player][play]==Botte("Citerne dessence ")) or (self.jeu.cartes_joueurs[player][play]==Attaque("Panne d'essence")) or (self.jeu.cartes_joueurs[player][play]==Parade("Essence"))
            d=(self.jeu.cartes_joueurs[player][play]==Botte("As du volant")) or (self.jeu.cartes_joueurs[player][play]==Attaque("Accident")) or (self.jeu.cartes_joueurs[player][play]==Parade("Reparation"))
            e=(self.jeu.cartes_joueurs[player][play]==Botte("Vehicule prioritaire")) or (self.jeu.cartes_joueurs[player][play]==Attaque("Limite de vitesse")) or (self.jeu.cartes_joueurs[player][play]==Parade("Fin limite de vitesse"))                                                                                                                                           

            if a:
                carte_a_remettre=self.tables[table_de]['Etat des roues']
                self.tables[table_de]['Etat des roues']=self.jeu.cartes_joueurs[player][play]

            elif b:
                carte_a_remettre=self.tables[table_de]['Feux']
                self.tables[table_de]['Feux']=self.jeu.cartes_joueurs[player][play]

            elif c:
                carte_a_remettre=self.tables[table_de]['Essence']
                self.tables[table_de]['Essence']=self.jeu.cartes_joueurs[player][play]

            elif d:
                carte_a_remettre=self.tables[table_de]['Accident']
                self.tables[table_de]['Accident']=self.jeu.cartes_joueurs[player][play]

            elif e:
                carte_a_remettre=self.tables[table_de]['Limite de vitesse']
                self.tables[table_de]['Limite de vitesse']=self.jeu.cartes_joueurs[player][play]           

            else:
                carte_a_remettre=self.tables[table_de]['Distance']
                self.tables[player]['Distance']=self.jeu.cartes_joueurs[player][play]
                self.jeu.joueurs[player].score+=self.jeu.cartes_joueurs[player][play].point
            #indent problem?
            self.jeu.cartes_joueurs[player].pop(play)
            if carte_a_remettre!=None:
                self.jeu.pioche.append(carte_a_remettre)
    
    def jouer_auto(self,play,player):
        """
            Deroulement du jeu dans le cas ou mon joeur est une IA 
        """
        if play==7:
            n_c= self.jeu.joueurs[player].choisir_carte_a_defausser()
            self.jeu.defausser(self.jeu.cartes_joueurs[player],self.jeu.cartes_joueurs[player][n_c])
        else:
            if type(self.jeu.cartes_joueurs[player][play])==Botte:
                table_de=player
                play=IA.choisir_carte(self.jeu.joueurs[player])
                self.depotCarte_auto(play,player,table_de)
                self.jeu.piocher(player)
                self.jouer_auto(play,player)
            else:
                table_de=player
                play=IA.choisir_carte(self.jeu.joueurs[player])
                self.depotCarte_auto(play,player,table_de)


    
    def tour(self,player):
        """
            Deroulement du jeu pendant un tour 
        """
        self.jeu.joueurs[player].table=self.tables[player]
        self.jeu.joueurs[player].cartes=self.jeu.cartes_joueurs[player]      
        self.jeu.joueurs[player].avance,self.jeu.joueurs[player].limit50=self.jeu.joueurs[player].Permission_davancer()
        print("C'est à ",self.jeu.joueurs[player].nom," de jouer:")
        if type(self.jeu.joueurs[player])==IA:
            play=IA.choisir_carte(self.jeu.joueurs[player])
            self.jouer_auto(play,player)
            print("Le joueur ", self.jeu.joueurs[player].nom," a jouer ")
        else: 
            print("-------------------------\n")
            print(self)
            print("Vos cartes :")
            for nc,c in enumerate(self.jeu.cartes_joueurs[player]):
                print(nc,":",c)
            print(nc+1,": Defausser une carte")
            play=int(input("Que voulez vous faire (0,7) ? "))
            print("-------------------------\n")
            if play==7:
                n_c=int(input("Quelle carte voulez defausser (0,6) ?"))
                if n_c>6:
                    n_c=int(input("Entrez une valeur entre 0 et 6 !"))
                    self.jeu.defausser(self.jeu.cartes_joueurs[player],self.jeu.cartes_joueurs[player][n_c])
                self.jeu.defausser(self.jeu.cartes_joueurs[player],self.jeu.cartes_joueurs[player][n_c])
            else:
                if type(self.jeu.cartes_joueurs[player][play])==Botte:
                    table_de=player
                    self.depotCarte(play,player,table_de)
                    print("Vous avez deposer une Botte vous avez le droit de jouer encore une carte")
                    self.jeu.piocher(player)
                    self.tour(player)

                elif type(self.jeu.cartes_joueurs[player][play])==Attaque:
                    for nj,j in enumerate(self.jeu.joueurs):
                        print(nj,":",j.nom)
                    table_de=int(input("Qui voulez vous attaquer ?"))
                    self.verifier_botte(play,player,table_de)
                else:
                    table_de=player
                    self.depotCarte(play,player,table_de)



    def depotCarte(self,play,player,table_de):  
        """
            Fonction de depot de carte  
        """
        if play==7:
                n_c=int(input("Quelle carte voulez defausser (0,6) ?"))
                if n_c>6:
                    n_c=int(input("Entrez une valeur entre 0 et 6 !"))
                    self.jeu.defausser(self.jeu.cartes_joueurs[player],self.jeu.cartes_joueurs[player][n_c])
                    self.jeu.piocher(player)
                else:
                    self.jeu.defausser(self.jeu.cartes_joueurs[player],self.jeu.cartes_joueurs[player][n_c])
                    self.jeu.piocher(player)
        else:
            carte_a_remettre=None
            a=(self.jeu.cartes_joueurs[player][play]==Botte("Increvable")) or (self.jeu.cartes_joueurs[player][play]==Attaque("Crevaison")) or (self.jeu.cartes_joueurs[player][play]==Parade("roue de secours"))
            b=(self.jeu.cartes_joueurs[player][play]==Botte("Vehicule prioritaire")) or (self.jeu.cartes_joueurs[player][play]==Attaque("feux rouge")) or (self.jeu.cartes_joueurs[player][play]==Parade("feux vert"))
            c=(self.jeu.cartes_joueurs[player][play]==Botte("Citerne dessence ")) or (self.jeu.cartes_joueurs[player][play]==Attaque("Panne d'essence")) or (self.jeu.cartes_joueurs[player][play]==Parade("Essence"))
            d=(self.jeu.cartes_joueurs[player][play]==Botte("As du volant")) or (self.jeu.cartes_joueurs[player][play]==Attaque("Accident")) or (self.jeu.cartes_joueurs[player][play]==Parade("Reparation"))
            e=(self.jeu.cartes_joueurs[player][play]==Botte("Vehicule prioritaire")) or (self.jeu.cartes_joueurs[player][play]==Attaque("Limite de vitesse")) or (self.jeu.cartes_joueurs[player][play]==Parade("Fin limite de vitesse"))                                                                                                                                           

            if a:
                carte_a_remettre=self.tables[table_de]['Etat des roues']
                self.tables[table_de]['Etat des roues']=self.jeu.cartes_joueurs[player][play]

            elif b:
                carte_a_remettre=self.tables[table_de]['Feux']
                self.tables[table_de]['Feux']=self.jeu.cartes_joueurs[player][play]

            elif c:
                carte_a_remettre=self.tables[table_de]['Essence']
                self.tables[table_de]['Essence']=self.jeu.cartes_joueurs[player][play]

            elif d:
                carte_a_remettre=self.tables[table_de]['Accident']
                self.tables[table_de]['Accident']=self.jeu.cartes_joueurs[player][play]

            elif e:
                carte_a_remettre=self.tables[table_de]['Limite de vitesse']
                self.tables[table_de]['Limite de vitesse']=self.jeu.cartes_joueurs[player][play]           

            else:
                if (self.jeu.joueurs[player].avance==False):
                    print("vous ne pouvez pas avancer! essayez une autre carte: ")
                    p=int(input("Que voulez vous faire (0,7) ? "))
                    self.depotCarte(p,player,table_de)

                else:
                    if (self.jeu.joueurs[player].limit50==True):
                        if (self.jeu.cartes_joueurs[player][play]==Distance("Papillon",75)) or (self.jeu.cartes_joueurs[player][play]==Distance("Lievre",100)) or (self.jeu.cartes_joueurs[player][play]==Distance("Guépard",200)):
                            print("vous ne pouvez pas avancer a cette vitesse votre max est a 50! essayez une autre carte:")
                            play=int(input("Que voulez vous faire (0,7) ? "))
                            if type(self.jeu.cartes_joueurs[player][play])==Attaque:
                                for nj,j in enumerate(self.jeu.joueurs):
                                    print(nj,":",j.nom)
                                table_de=int(input("Qui voulez vous attaquer ?"))
                                self.depotCarte(play,player,table_de)
                            else:
                                table_de=player
                                self.depotCarte(play,player,table_de)
                        else:
                            carte_a_remettre=self.tables[table_de]['Distance']
                            self.tables[player]['Distance']=self.jeu.cartes_joueurs[player][play]
                            self.jeu.joueurs[player].score+=self.jeu.cartes_joueurs[player][play].point
                    else:
                        carte_a_remettre=self.tables[table_de]['Distance']
                        self.tables[player]['Distance']=self.jeu.cartes_joueurs[player][play]
                        self.jeu.joueurs[player].score+=self.jeu.cartes_joueurs[player][play].point
            #indent problem?
            self.jeu.cartes_joueurs[player].pop(play)
            if carte_a_remettre!=None:
                self.jeu.pioche.append(carte_a_remettre)


    def verifier_botte(self,play,player,table_de):
        """
            Verifie si le joueur attaquer à une botte, si oui on peut pas l'attaquer
        """
        a=(self.tables[table_de]['Etat des roues']==Botte("Increvable"))and(self.jeu.cartes_joueurs[player][play]==Attaque("Crevaison"))
        b=(self.tables[table_de]['Feux']==Botte("Vehicule prioritaire"))and(self.jeu.cartes_joueurs[player][play]==Attaque("feux rouge"))
        c=(self.tables[table_de]['Limite de vitesse']==Botte("Vehicule prioritaire"))and(self.jeu.cartes_joueurs[player][play]==Attaque("Limite de vitesse"))
        d=(self.tables[table_de]['Essence']==Botte("Citerne dessence "))and(self.jeu.cartes_joueurs[player][play]==Attaque("Panne d'essence"))
        e=(self.tables[table_de]['Accident']==Botte("As du volant"))and(self.jeu.cartes_joueurs[player][play]==Attaque("Accident"))

        if(a or b or c or d or e):
            print("Vous ne pouvez pas attaquer ce joueur car il a une protection Botte !")
            y=int(input("Voulez vous attaquer un autre joueur (tapez 1) ou jouer une autre carte (tapez 2) "))
            if y==1:
                table_de=int(input("Qui voulez vous attaquer ?"))
                self.verifier_botte(play,player,table_de)
            elif y==2:
                play=int(input("Que voulez vous faire (0,7) ? "))
                self.depotCarte(play,player,table_de)
        else:

            self.depotCarte(play,player,table_de)
                    

           

       
       
         
                    
        
        

