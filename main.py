"""
Exercice lecture de données
"""
#### Imports et définition des variables globales
#import random

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """Lit le contenu du fichier et retourne une liste de listes d'entiers.

    Args:
        filename (str): nom du fichier à lire

    list: Liste de listes d'entiers, où chaque ligne est transformée en liste d'entiers
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        return [[ int(i) for i in l.strip().split(';') ] for l in f.readlines()]

def get_list_k(data, k):
    """returne la k eme liste
    Args:
        data (liste): Liste de toutes les listes
    
    Returns:
      La k-eme liste
    """
    return data[k]

def get_first(l):
    """retourne le premier element de la liste l
    Args:
        l (liste) : une liste
    
    Returns:
       Le 1er elelement de la liste l
    """
    return l[0]

def get_last(l):
    """retourne le dernier element de la liste l
    Args:
        l (liste) : une liste
    
    Returns:
         Le dernier elelement de la liste l
    """
    return l[-1]

def get_max(l):
    """L'élément maximum de l
    Args:
        l (liste)
    
    Returns:
        L'élément maximum
    """
    x = 0
    for j in l:
        x = max(x, j)
    return x


def get_min(l):
    """
    L'élément minimum
    """
    x = 1000000
    for j in l:
        x = min(x, j)
    return x

def get_sum(l):
    """
    La somme des élément de la liste l
    """
    x = 0
    for i in l:
        x +=i
    return x


#### Fonction principale


def main():
    """
    Fonction principale
    """
    #pass

    data = read_data(FILENAME)
    #print (data)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
