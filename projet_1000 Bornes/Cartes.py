
# coding: utf-8



import random
import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Carte(metaclass=abc.ABCMeta):
    """
        Classe Carte
    """

    #@abc.abstractmethod
    #abstract class --> no need initialisation

    def multiple(self,n):
        """
            Fonction pour dupliquer n fois ma carte
        """
        mul=[]
        for i in range (n):
            mul.append(self)
        return mul
    
    def __repr__(self):
        """
            Affichage d'une carte Distance 
        """
        pass
    def __eq__(self, other): 
        """
            Verifie si deux carte sont egaux 
        """
        # don't attempt to compare against unrelated types
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.type_carte == other.type_carte


class Distance(Carte):
    """
        Classe Distance 
    """
    def __init__(self,type_carte:str,point:int):
        """
            Initialisation des attributs 
        """
        self.type_carte=type_carte
        self.point=point
    def __repr__(self):
        """
            Affichage d'une carte Distance 
        """
        return "Distance: {}, {}".format(self.type_carte, self.point)
    
    def __gt__(self, other): 
        """
            Verifie si une carte est plus grande que l'autre  
        """
        # don't attempt to compare against unrelated types
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.point >= other.point
    def __lt__(self, other):
        """
            Verifie si une carte est plus petite que l'autre  
        """
        # don't attempt to compare against unrelated types
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.point < other.point


class Attaque(Carte):
    def __init__(self,type_carte:str):
        """
            Initialisation des attributs 
        """
        self.type_carte=type_carte
    def __repr__(self):
        """
            Affichage d'une carte Attaque 
        """
        return "Attaque: {} ".format(self.type_carte)
    


class Parade(Carte):
    def __init__(self,type_carte:str):
        """
            Initialisation des attributs 
        """
        self.type_carte=type_carte
    def __repr__(self):
        """
            Affichage d'une carte Parade 
        """
        return "Parade: {} ".format(self.type_carte) 

    
class Botte(Carte):
    def __init__(self,type_carte:str):
        """
            Initialisation des attributs 
        """
        self.type_carte=type_carte
    def __repr__(self):
        """
            Affichage d'une carte Botte
        """
        return "Botte: {} ".format(self.type_carte)
   

