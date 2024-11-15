def binaire_vers_decimal(binaire):
    decimal = 0
    puissance = len(binaire) - 1
    for bit in binaire:
        decimal += int(bit) * (2 ** puissance)
        puissance = puissance - 1
    return decimal

# Test de la fonction
nombre_binaire = "1101"
assert binaire_vers_decimal(nombre_binaire) == 13
