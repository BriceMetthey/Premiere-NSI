from PIL import Image


# renvoie le négatif du papillon
pap = Image.open("papillon.png")
print("Taille:", pap.size)
print("Mode :", pap.mode)
for l in range(10):
    for c in range(10):
        valeur = pap.getpixel((c, l))
        if valeur == 0:
            pap.putpixel((c, l), 255)
        else:
            pap.putpixel((c, l), 0)
pap.save("image1.png", "png")


# renvoie le négatif de Joconde_10.png
joco = Image.open("Joconde_10.png")
for l in range(10):
    for c in range(10):
        valeur = joco.getpixel((c, l))
        nouvelle_valeur = 255 - valeur
        joco.putpixel((c, l), nouvelle_valeur)
joco.save("image2.png", "png")


# renvoie le négatif de Joconde_gris.png
joco = Image.open("Joconde_gris.png")
for l in range(384):
    for c in range(384):
        valeur = joco.getpixel((c, l))
        nouvelle_valeur = 255 - valeur
        joco.putpixel((c, l), nouvelle_valeur)
joco.save("image3.png", "png")
