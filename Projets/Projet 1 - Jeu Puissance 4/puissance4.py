def creer_grille()->list:
    grille = []
    for _ in range(6):  # 6 rangées
        ligne = []
        for _ in range(7):  # 7 colonnes
            ligne.append('*')
        grille.append(ligne)
    return grille

def afficher_grille(grille:list, joueur_actuel:str, jetons_restants:list)->None:
    for ligne in grille:
        ligne_affichee = "| "
        for case in ligne:
            ligne_affichee += case + " | "
        print(ligne_affichee)
    print("  0   1   2   3   4   5   6")  # Numéros des colonnes
    print(f"Joueur {joueur_actuel} doit jouer. Jetons restants : X = {jetons_restants[0]}, O = {jetons_restants[1]}.")

def ajouter_jeton(grille:list, colonne:int, jeton:str)->bool:
    for ligne in range(5, -1, -1):  # Parcourt de la dernière rangée (5) à la première (0)
        if grille[ligne][colonne] == '*':
            grille[ligne][colonne] = jeton
            return True
    return False  # Colonne pleine

def verifier_victoire(grille:list, jeton:str)->bool:
    # Vérification horizontale
    for ligne in range(6):
        for col in range(4):  # Max colonne 3 pour 4 alignés
            if grille[ligne][col] == grille[ligne][col + 1] == grille[ligne][col + 2] == grille[ligne][col + 3] == jeton:
                return True
    # Vérification verticale
    for col in range(7):
        for ligne in range(3):  # Max ligne 2 pour 4 alignés
            if grille[ligne][col] == grille[ligne + 1][col] == grille[ligne + 2][col] == grille[ligne + 3][col] == jeton:
                return True
    # Vérification diagonale (\)
    for ligne in range(3):
        for col in range(4):
            if grille[ligne][col] == grille[ligne + 1][col + 1] == grille[ligne + 2][col + 2] == grille[ligne + 3][col + 3] == jeton:
                return True
    # Vérification diagonale (/)
    for ligne in range(3):
        for col in range(3, 7):
            if grille[ligne][col] == grille[ligne + 1][col - 1] == grille[ligne + 2][col - 2] == grille[ligne + 3][col - 3] == jeton:
                return True
    return False

def est_pleine(grille:list)->bool:
    for ligne in grille:
        if '*' in ligne:
            return False
    return True

def reinitialiser_grille(grille:list)->None:
    for ligne in grille:
        for col in range(len(ligne)):
            ligne[col] = '*'

def jouer()->None:
    grille = creer_grille()
    jetons_restants = [21, 21]  # Index 0 : Joueur X, Index 1 : Joueur O
    joueur_actuel = "X"
    index_joueur = 0  # Index 0 pour "X", 1 pour "O"
    partie_terminee = False

    while not partie_terminee:
        afficher_grille(grille, joueur_actuel, jetons_restants)
        # Pas de validation, saisie directe
        colonne = int(input(f"Joueur {joueur_actuel}, choisissez une colonne (0-6) : "))

        # Placement du jeton
        if ajouter_jeton(grille, colonne, joueur_actuel):
            jetons_restants[index_joueur] -= 1

            # Vérification de la victoire
            if verifier_victoire(grille, joueur_actuel):
                afficher_grille(grille, joueur_actuel, jetons_restants)
                print(f"Félicitations, Joueur {joueur_actuel} a gagné !")
                partie_terminee = True
                continue

            # Si la grille est pleine, on réinitialise et continue
            if est_pleine(grille):
                print("La grille est pleine, mais aucun joueur n'a gagné. Réinitialisation de la partie.")
                reinitialiser_grille(grille)
                continue

            # Alternance des joueurs
            index_joueur = 1 - index_joueur  # Alterne entre O et X
            if index_joueur == 0 :
                joueur_actuel = "X" 
            else :
                joueur_actuel = "O"

        else:
            print("La colonne est pleine. Veuillez en choisir une autre.")

# Lancer le jeu
jouer()
