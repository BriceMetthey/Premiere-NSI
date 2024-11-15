def hexadecimal_vers_binaire(hexadecimal):
    # Dictionnaire de correspondance hexadécimal -> binaire
    hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    
    # Conversion
    binaire = ''
    for char in hexadecimal:
        binaire += hex_to_bin[char]  # Convertit chaque chiffre en binaire et ajoute au résultat
    
    return binaire

# Test de la fonction
nombre_hexadecimal = "2F"
print(f"Le nombre hexadécimal {nombre_hexadecimal} en binaire est : {hexadecimal_vers_binaire(nombre_hexadecimal)}")
