def decimal_vers_binaire(n):
    if n == 0:
        return "0"
    reste = []
    while n > 0:
        reste.append(str(n % 2))  # Stocke le reste sous forme de chaîne de caractères
        n = n // 2  # Met à jour n

    inverse = reste[::-1]
    return ''.join(inverse)  # Construire une chaine à partir d'un tableau

# Test de la fonction
nombre_decimal = 13
assert decimal_vers_binaire(nombre_decimal) == "1101"