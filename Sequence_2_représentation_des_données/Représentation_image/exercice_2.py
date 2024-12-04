from PIL import Image


# Les dimensions de l'image
largeur = 7
hauteur = 5

# Création d'une image en mode RGB de 7x5 en blanc
img = Image.new("RGB", (largeur, hauteur), (255, 255, 255))


for x in range(largeur):  # boucle sur les colonnes de l’image
    img.putpixel((x, 1), (255, 0, 0))
    img.putpixel((x, 3), (0, 255, 0))  # Ligne verte

for y in range(hauteur):  # boucle sur les lignes de l’image
    img.putpixel((5, y), (0, 0, 255))
    img.putpixel((1, y), (255, 0, 255))  # une colonne de magenta (255, 0, 255)

img.putpixel((0, 0), (0, 0, 0))  # Pixel noir

img.show()
