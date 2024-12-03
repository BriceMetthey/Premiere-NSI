# 0.Appel d'un module exterieur
from PIL import Image



# 1.Définition de la fonction
def filtreVert(NomFichier):
    img = Image.open(NomFichier) 
    largeur, hauteur = img.size 

    for x in range(largeur) : 
        
        for y in range(hauteur): 
            r,v,b = img.getpixel((x,y))
            img.putpixel((x,y),(0,v,0)) # occulte complètement les composantes rouges et bleues
    
    # En sortie de boucle pour voir le résultat définitif
    img.show() 
        

# 2.Appel de la fonction
filtreVert("Joconde.jpg")