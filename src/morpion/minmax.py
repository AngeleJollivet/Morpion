from morpion_pvp import victoire, plateau_plein

def minmax(plateau, profondeur, IA, pion_ia, pion_j):
    """Algorithme récursif qui permet à l'IA de voir (calculer) en profondeur et d'analyser les différents coups possibles
    Args:
        plateau (list) : le plateau de jeu, matrice 3x3
        profondeur (int) : la profondeur du coup dans l'arbre des possibilités
        pion_ia (str) : le pion de l'IA
        pion _j(str) : le pion du joueur 
    Returns:
        int : les scores associés aux différents chemins"""
    if victoire(plateau):
        """ Si c'est a l'ia de jouer ça veut dire que le joueur a gagné au tour précédent"""
        if IA:
            return -1000 + profondeur
        else:
            return 1000 - profondeur
    if plateau_plein(plateau):
        return 0
    
    if IA:
        score_max = -10000
        for i in range(3):
            for j in range(3):
                if type(plateau[i][j]) == int: 
                    """ permet de vérifier si la case contient un nombre entier donc vide ou si elle contient une lettre donc pleine"""
                    temp = plateau[i][j]
                    plateau[i][j] = pion_ia
                    score = minmax(plateau, profondeur + 1, False, pion_ia, pion_j)
                    plateau[i][j] = temp
                    if score > score_max:
                        score_max = score
        return score_max

    else:
        score_min = +10000
        for i in range(3):
            for j in range(3):
                if type(plateau[i][j]) == int:
                    temp = plateau[i][j]
                    plateau[i][j] = pion_j
                    score = minmax(plateau, profondeur + 1, True, pion_ia, pion_j)
                    plateau[i][j] = temp
                    if score < score_min:
                        score_min  = score
        return score_min

def meilleur_coup(plateau, pion_ia, pion_j):
    """Fonction qui permet à l'IA de pouvoir choisir la meilleure case possible via la fonction minmax
    Args:
        plateau (list) : le plateau de jeu, matrice 3x3
        pion_ia (str) : le pion de l'IA
        pion_j(str) : le pion du joueur 
    Returns:
        int : le numéro de la case qui correspond au meilleur cours selon le plateau actuel"""
    score_max = -10000
    coup = None
    for i in range(3):
        for j in range(3):
            if type(plateau[i][j]) == int:
                temp = plateau[i][j]
                plateau[i][j] = pion_ia
                """ on lance la simulation pour trouver le meilleur coup possible """
                score = minmax(plateau, 0, False, pion_ia, pion_j)
                plateau[i][j] = temp
                if score > score_max:
                    score_max = score
                    coup = temp 
                    """ sert a renvoyer le numero de la meilleure case possible """
    return coup

