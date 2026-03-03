import random

def plateau():
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

def afficher_plateau(plateau):
    for ligne in plateau :
        print(ligne)

def choisir_pions():
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

morpion_random()