def plateau():
    """Créer un plateau à cases numérotées

    Returns:
        plateau (list) : le plateau de jeu, matrice 3x3
    """
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

def afficher_plateau(plateau):
    """Afficher le plateau
    
    Args:
        plateau (list) : le plateau de jeu, matrice 3x3
    """
    for ligne in plateau :
        print(ligne)

def choisir_pions():
    """Attribuer un pion (X ou O) à chaque joueur 

    Returns:
        str : les pions des deux joueurs dans un tuple
    """
    j1 = input('Joueur 1 : Voulez vous jouer les X ou les O ? ') 
    
    if j1 not in ("X", "x", "O", "o"):  
        print("Réponse invalide, veuillez relancer le jeu !")
        return None, None
    
    if j1 == "X" or j1 == "x":
        j1 = "X"
        j2 = "O"
    else:
        j1 = "O"
        j2 = "X"
    return j1, j2

def jouer(plateau, choix, pion):
    """Placer un pion sur une case libre du plateau selon le joueur dont c'est le tour
    Args:
        plateau (list) : le plateau de jeu, matrice 3x3
        choix (int) : la case choisie par le joueur
        pion (str) : le pion du joueur dont c'est le tour
    Returns:
        list : le plateau mis à jour"""
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == choix:
                if type(plateau[i][j]) == int:
                    plateau[i][j] = pion
                    return plateau
                else:
                    print("Case déjà prise !")
                    coup = int(input("Merci de choisir une case libre : "))
                    return jouer(plateau, coup, pion)
    print("Case invalide !")
    coup = int(input("Merci de choisir une case valide : "))
    return jouer(plateau, coup, pion)

def plateau_plein(plateau): 
    """Permet de vérifier si le plateau est rempli ou non
    Args:
        plateau (list) : le plateau de jeu, matrice 3x3
    Returns:
        bool : True s'il est plein, False s'il reste au moins une case de vide"""
    for ligne in plateau:
        for i in ligne:
            if type(i) == int:
                return False
    return True

def victoire(plateau) :
    """Parcours le plateau pour vérifier si 3 pions sont alignés et si l'un des joueurs à gagné
    Args:
        plateau (list) : le plateau de jeu, matrice 3x3
    Returns:
        list : True si un joueur a gagné, False par défaut sinon"""
    for i in range(3):
        if plateau[i][0] == plateau[i][1] and plateau[i][0] == plateau[i][2]:
            return True
        if plateau[0][i] == plateau[1][i] and plateau[0][i] == plateau[2][i] :
            return True
        if plateau [0][0] == plateau[1][1] and plateau[0][0] == plateau[2][2]:
            return True
        if plateau [0][2] == plateau[1][1] and plateau[0][2] == plateau[2][0]:
            return True

def morpion():
    """Jouer au morpion contre un autre utilisateur dans le même terminal"""
    p = plateau()
    j1, j2 = choisir_pions()
    if j1 is None: #là s'ils rentrent une mauvaise lettre c'est ici qu'on check et qu'on arrete tout
        print("Merci de relancer")
        return None
    afficher_plateau(p)
    
    while not plateau_plein(p):
        coup1 = int(input("Joueur 1 - choisissez une case : "))
        p = jouer(p, coup1, j1)
        afficher_plateau(p)

        if victoire(p):
            print("Victoire du joueur 1 !")
            return 
        
        if plateau_plein(p):
            print("Match nul !")
            return

        coup2 = int(input("Joueur 2 - choisissez une case : "))
        p = jouer(p, coup2, j2)
        afficher_plateau(p)

        if victoire(p):
            print("Victoire du joueur 2 !")
            return
        if plateau_plein(p):
            print("Match nul !")
            return
