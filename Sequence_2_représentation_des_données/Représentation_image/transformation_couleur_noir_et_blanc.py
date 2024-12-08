from PIL import Image


# transforme la Joconde couleur en noir et blanc par moyenne des pixels
joco = Image.open("Joconde_384.jpg")
for l in range(384):
    for c in range(384):
        valeurs = joco.getpixel((c, l))
        nouveaux = (valeurs[0] + valeurs[1] + valeurs[2]) // 3
        joco.putpixel((c, l), (nouveaux, nouveaux, nouveaux))
joco.save("image1.png", "png")


# transforme la jonconde couleur en noir et blanc avec 0 , 21 R + 0 , 71 G + 0 , 07 B
joco = Image.open("Joconde_384.jpg")
for l in range(384):
    for c in range(384):
        valeurs = joco.getpixel((c, l))
        nouveaux = 0.21 * valeurs[0] + 0.71 * valeurs[1] + 0.07 * valeurs[2]
        nouveaux = int(nouveaux)
        joco.putpixel((c, l), (nouveaux, nouveaux, nouveaux))
joco.save("image2.png", "png")


# transforme la Joconde couleur en noir et blanc avec 0 , 299 R + 0 ,587 G + 0 ,114 B
joco = Image.open("Joconde_384.jpg")
for l in range(384):
    for c in range(384):
        (R, G, B) = joco.getpixel((c, l))
        nouveaux = 0.299 * R + 0.587 * G + 0.114 * B
        nouveaux = int(nouveaux)
        joco.putpixel((c, l), (nouveaux, nouveaux, nouveaux))
joco.save("image3.png", "png")
