from morpion_pvp import victoire, plateau_plein

def minmax(plateau, profondeur, IA):
    if victoire:
        if IA==True:
            return 1000
        else:
            return -1000
    if plateau_plein:
        return 0
    
    if IA:
        score_max = -10000
        for i in range(3):
            for j in range(3):
                if type(plateau[i][j]) == int:
                    temp = plateau[i][j]
                    plateau[i][j] = pion_ia
                    score = minmax(plateau, profondeur + 1, False)
                    plateau[i][j] = temp
                    score_max = max(score, score_max)
                return score_max

    else:
        score_max = +10000
        for i in range(3):
            for j in range(3):
                if type(plateau[i][j]) == int:
                    temp = plateau[i][j]
                    plateau[i][j] = pion_j
                    score = minmax(plateau, profondeur + 1, False)
                    plateau[i][j] = temp
                    score_max = max(score, score_max)
                return score_max


