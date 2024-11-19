def addition_binaire(bin1, bin2):
    """
    Additionne deux nombres binaires sous forme de chaînes de caractères.
    
    Paramètres:
    - bin1 : le premier nombre binaire sous forme de chaîne de caractères
    - bin2 : le second nombre binaire sous forme de chaîne de caractères
    
    Retourne:
    - Une chaîne de caractères représentant le résultat de l'addition en binaire.
    """
    # Assurer que les chaînes ont la même longueur en remplissant de 0 à gauche
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)
    
    resultat = ""
    retenue = 0

    # Additionner de droite à gauche
    for i in range(max_len - 1, -1, -1):
        # Calculer la somme des bits à la position i, avec la retenue
        bit_sum = int(bin1[i]) + int(bin2[i]) + retenue
        # Le bit du résultat est le bit de poids faible de la somme (0 ou 1)
        resultat = str(bit_sum % 2) + resultat
        # La nouvelle retenue est le bit de poids fort de la somme (0 ou 1)
        retenue = bit_sum // 2

    # Si la dernière retenue est 1, on l'ajoute au résultat
    if retenue == 1:
        resultat = '1' + resultat

    return resultat

# Exemple d'utilisation
print(addition_binaire("1101", "1011"))  # Donne 11000
print(addition_binaire("1010", "1101"))  # Donne 10111
