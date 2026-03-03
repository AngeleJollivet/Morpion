def plateau():
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

def afficher_plateau(plateau):
    for ligne in plateau :
        print(ligne)

def choisir_pions():
    pion_j = input('Joueur : Voulez vous jouer les X ou les O ? ') 
    
    if pion_j not in ("X", "x", "O", "o"):  # utiliser .isupper ?? jsp c'est pas hyper clean là
        print("Réponse invalide, veuillez relancer le jeu !")
        return None, None
    
    if pion_j == "X" or pion_j == "x":
        pion_j = "X"
        pion_ia = "O"
    else:
        pion_j = "O"
        pion_ia = "X"
    return pion_j, pion_ia

def jouer(plateau, choix, pion): # Ca pourrait être cool de faire une version avec un while plutot ?
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

def jouer_IA(plateau, pion):
#    choix = CA DEPEND DE L'ALGO MINMAX DU COUP
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == choix:
                if type(plateau[i][j]) == int:
                    plateau[i][j] = pion
                    return plateau
                else:
                    return jouer_IA(plateau, pion) # ca risque de faire BEAUCOUP d'appels recursifs qu'on voit pas ..
    return jouer_IA(plateau, pion) 


def plateau_plein(plateau): #ouais le nom ets un peu bancal ehahahah
    for ligne in plateau:
        for i in ligne:
            if type(i) == int:
                return False
    return True

def victoire(plateau) :
    for i in range(3):
        if plateau[i][0] == plateau[i][1] and plateau[i][0] == plateau[i][2]:
            return True
        if plateau[0][i] == plateau[1][i] and plateau[0][i] == plateau[2][i] :
            return True
        if plateau [0][0] == plateau[1][1] and plateau[0][0] == plateau[2][2]:
            return True
        if plateau [0][2] == plateau[1][1] and plateau[0][2] == plateau[2][0]:
            return True

def morpion_random():
    p = plateau()
    pion_j, pion_ia = choisir_pions()
    if pion_j is None: #là s'ils rentrent une mauvaise lettre c'est ici qu'on check et qu'on arrete tout
        print("Merci de relancer")
        return None
    afficher_plateau(p)
    
    while not plateau_plein(p):
        coup = int(input("Joueur - choisissez une case : "))
        p = jouer(p, coup, pion_j)
        afficher_plateau(p)

        if victoire(p):
            victoire = "joueur"
            print("Victoire du joueur 1 !")
            return 
        
        if plateau_plein(p):
            victoire = "égalité"
            print("Match nul !")
            return

        print("l'IA joue...")
        p = jouer_IA(p, ia)
        afficher_plateau(p)

        if victoire(p):
            victoire = "ia"
            print("Victoire du joueur 2 !")
            return
        if plateau_plein(p):
            print("Match nul !")
            return

morpion_random() 

