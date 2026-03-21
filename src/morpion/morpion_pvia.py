from morpion_pvp import plateau, afficher_plateau, victoire, plateau_plein, jouer
from minmax import meilleur_coup

def partie_contre_ia():
    """Jouer au morpion contre un algorithme minmax dans le terminal"""
    p = plateau()
    pion_joueur = "X" # contrairement aux autres modes de jeu, le joueur ne choisit ici pas son pion, piste d'amélioration ?
    pion_ia = "O"
    
    print("--- BIENVENUE CONTRE L'IA ---")
    afficher_plateau(p)

    while True:
        """ tour du joueur """
        try:
            choix = int(input(f"À toi ({pion_joueur}), choisis une case (1-9) : "))
            p = jouer(p, choix, pion_joueur)
        except:
            print("Entrée invalide, réessaie.")
            continue
        #Dans les autres modes de jeux, nous passons plutot par des if/else pour vérifier la validité de l'entrée saisie par l'utilisateur, ce qui laisse place à beaucoup d'autres erreurs que nous n'aurions pas prévues.
        # Les "try/Except" ne sont techniquement pas de notre niveau puisque nous ne les avons pas etudiés en cours, mais c'est le moyen le plus correct et efficace d'analyser les entrées, nous avons donc décidé de l'implémenter 

        afficher_plateau(p)
        
        if victoire(p):
            print("Bravo, tu as battu l'IA ! (C'est normalement impossible...)")
            break
        if plateau_plein(p):
            print("Match nul !")
            break

        """ tour de l'ia """
        print("\nL'IA réfléchit...")
        coup_ia = meilleur_coup(p, pion_ia, pion_joueur)
        if coup_ia is not None:
            p = jouer(p, coup_ia, pion_ia)
            print(f"L'IA a joué en case {coup_ia}")
        
        afficher_plateau(p)

        if victoire(p):
            print("L'IA a gagné ! Entraîne-toi encore.")
            break
        if plateau_plein(p):
            print("Match nul !")
            break
