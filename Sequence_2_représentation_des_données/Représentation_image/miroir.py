from PIL import Image


# miroir du papillon
pap = Image.open("papillon.png")
pap2 = pap.copy()
for l in range(10):
    for c in range(10):
        valeur = pap.getpixel((c, l))
        pap2.putpixel((9 - c, l), valeur)
pap2.save("image.png", "png")


# miroir Joconde noir et blanc
joco = Image.open("Joconde_gris.png")
joco2 = joco.copy()
for l in range(384):
    for c in range(384):
        valeur = joco.getpixel((c, l))
        joco2.putpixel((383 - c, l), valeur)
joco2.save("image.png", "png")


# miroir Joconde couleur
joco = Image.open("Joconde_384.jpg")
joco2 = joco.copy()
for l in range(384):
    for c in range(384):
        valeurs = joco.getpixel((c, l))
        joco2.putpixel((383 - c, l), valeurs)
joco2.save("image.png", "png")
