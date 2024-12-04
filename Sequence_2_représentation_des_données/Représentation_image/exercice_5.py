from PIL import Image

im = Image.new("RGB", (800, 800), ("grey"))

# Modifier le programme pour que l’image contienne un pixel noir, un bleu, un rouge, un vert et un blanc.
# Modifier votre programme pour que votre image contienne un pixel de couleur « skyblue ».

im.putpixel((1, 1), (0, 0, 0))  # un pixel noir
im.putpixel((2, 2), (0, 0, 255))  # un pixel bleu
im.putpixel((3, 3), (255, 0, 0))  # un pixel rouge
im.putpixel((4, 4), (0, 0, 255))  # un pixel vert
im.putpixel((5, 5), (255, 255, 255))  # un pixel blanc
im.putpixel((6, 6), (135, 206, 235))  # un pixel skyblue

im.save("premiere_image.png", "PNG")
im.save("premiere_image.jpg", "jpeg")
