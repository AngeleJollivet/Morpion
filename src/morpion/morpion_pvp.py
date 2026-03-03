#Bon c'est du PVP donc pas du tout ce qu'on est censés faire mais c'est une bonne base je pense !

def plateau():
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

def afficher_plateau(plateau):
    for ligne in plateau :
        print(ligne)

def choisir_pions():
    j1 = input('Joueur 1 : Voulez vous jouer les X ou les O ? ') 
    
    if j1 not in ("X", "x", "O", "o"):  # utiliser .isupper ?? jsp c'est pas hyper clean là
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

def morpion():
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

morpion()