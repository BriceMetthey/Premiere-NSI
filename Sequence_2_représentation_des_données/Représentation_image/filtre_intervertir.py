# 0.Appel d'un module exterieur
from PIL import Image



# 1.Définition de la fonction
def filtreBleu(NomFichier):
    img = Image.open(NomFichier) 
    largeur, hauteur = img.size 

    for x in range(largeur) : 
        
        for y in range(hauteur): 
            r,v,b = img.getpixel((x,y))
            img.putpixel((x,y),(b,v,r)) # intervertir les quantités de rouge et de bleu
    
    # En sortie de boucle pour voir le résultat définitif
    img.show() 
        

# 2.Appel de la fonction
filtreBleu("Joconde.jpg")