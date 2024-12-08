from PIL import Image


# Negatif de la Joconde en couleurs
joco = Image.open("Joconde_384.jpg")
for l in range(384):
    for c in range(384):
        (R, G, B) = joco.getpixel((c, l))
        nouveaux = (255 - R, 255 - G, 255 - B)
        joco.putpixel((c, l), nouveaux)
joco.save("image.png", "png")
