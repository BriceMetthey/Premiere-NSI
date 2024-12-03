from PIL import Image


# Les dimensions de l'image
largeur = 7
hauteur = 5

# Création d'une image en mode RGB de 7x5 en blanc
img = Image.new("RGB", (largeur, hauteur) , (255,255,255) )


# On saute de ligne en ligne PUIS on change de colonne
for x in range (largeur) : # boucle sur les colonnes de l’image
    
    for y in range (hauteur): # boucle sur les lignes de l’image
        
        print(f"Trace - colonne:{x} ligne:{y}")
        
        img.putpixel ((x,y),(255,0,0))
        


for x in range (largeur) : 
    
    for y in range (hauteur): 
        
        if x == 2 :
            img.putpixel ((x,y),(255,255,255))
        if y == 2 :
            img.putpixel ((x,y),(255,255,255))
        
        
img.show() # affiche l’image


#############################
# AUTRE SOLUTION            #
#############################

largeur = 7
hauteur = 5

img = Image.new("RGB", (largeur, hauteur) , (255,255,255) )

# on se 'déplace' autrement dans la grille
# on fait varié nos colonnes puis on saute de ligne
# for y in range (hauteur) : 
#     
#     for x in range (largeur): 
#         
#         print(f"Trace - colonne:{x} ligne:{y}")

