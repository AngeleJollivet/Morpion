from morpion_pvp import plateau, afficher_plateau, jouer, plateau_plein,victoire
import random

def choisir_pions():
    """Attribuer un pion (X ou O) au joueur, et l'autre à l'algorithme

    Returns:
        str : les pions du joueur et de l'algorithme
    """
    j = input('Joueur : Voulez vous jouer les X ou les O ? ') 
    
    if j not in ("X", "x", "O", "o"):  # utiliser .isupper ?? jsp c'est pas hyper clean là
        print("Réponse invalide, veuillez relancer le jeu !")
        return None, None
    
    if j == "X" or j == "x":
        j = "X"
        ia = "O"
    else:
        j = "O"
        ia = "X"
    return j, ia

def jouer_IA(plateau, pion):
    """Placer un pion sur une case libre du plateau selon un chiffre aléatoire entre 1 et 9
    Args:
        plateau (list) : le plateau de jeu, matrice 3x3
        pion (str) : le pion du joueur dont c'est le tour
    Returns:
        list : le plateau mis à jour"""
    choix = random.randint(1,9)
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == choix:
                if type(plateau[i][j]) == int:
                    plateau[i][j] = pion
                    return plateau
                else:
                    return jouer_IA(plateau, pion) # ca risque de faire BEAUCOUP d'appels recursifs qu'on voit pas ..
    return jouer_IA(plateau, pion) 

def morpion_random():
    """Jouer au morpion contre un algorithme aléatoire dans le terminal"""
    p = plateau()
    j, ia = choisir_pions()
    if j is None: #là s'ils rentrent une mauvaise lettre c'est ici qu'on check et qu'on arrete tout
        print("Merci de relancer")
        return None
    afficher_plateau(p)
    
    while not plateau_plein(p):
        coup1 = int(input("Joueur - choisissez une case : "))
        p = jouer(p, coup1, j)
        afficher_plateau(p)

        if victoire(p):
            print("Victoire du joueur 1 !")
            return 
        
        if plateau_plein(p):
            print("Match nul !")
            return

        print("l'IA joue...")
        p = jouer_IA(p, ia)
        afficher_plateau(p)

        if victoire(p):
            print("Victoire du joueur 2 !")
            return
        if plateau_plein(p):
            print("Match nul !")
            return
