import random

def creer_grille():
    grille = []
    for i in range(10):
        ligne = []
        for j in range(10):
            ligne.append("🌊")
        grille.append(ligne)
    return grille

def afficher_grille(grille):

    lettres = ["A","B","C","D","E","F","G","H","I","J"]

    # On commence par afficher les num des colonnes (1 à 10)
    print("   ", end="")            
    for n in range(1, 11):          
        print(n, end="   ")          # on affiche ts les num 
    print()                         # Retour à la ligne une fois que ts les num sont affichés

    # Ensuite on affiche chaque ligne de la grille
    for i in range(10):             
        print(lettres[i], end="  ") # on affiche la lettre qui correspond a la 
        for case in grille[i]:     
            print(case, end="  ")   # on affiche tt les cases
        print()                     # Retour à la ligne après avoir affiché tt la ligne
        
        
def placer_bateau(grille):
    
    lettres = ["A","B","C","D","E","F","G","H","I","J"]

    while True: 

        ligne = input("Entrez une lettre (A–J) : ").upper()
        colonne = input("Entrez un numéro (1–10) : ")

        # on vérifie que la ligne est dans la liste des lettres
        if ligne not in lettres:
            print("Cette lettre n'est pas entre A et J.")
            continue

        # Vérifier que la colonne est un nombre valide 
        if colonne not in ["1","2","3","4","5","6","7","8","9","10"]:
            print("Entrez  un nombre entre 1 et 10.")
            continue

        i = lettres.index(ligne)
        j = int(colonne) - 1
        

        # on vérifie si la case
        if grille[i][j] != "🌊":
            print("Il y a déjà un bateau dans cette case ")
            continue

        # on place le bateau
        grille[i][j] = "🚢" # B signfie qu'un bateau est placé dans la grille
        print("Le bateau est en position", ligne, ":", colonne)
        afficher_grille(grille) # On affiche pr voir si ça c bien actualisé
        
        break
    
def attaquer(grille_adversaire):
    lettres = ["A","B","C","D","E","F","G","H","I","J"]

    while True:
        colonne = input("Entrez la lettre de la case à attaquer (A–J) : ").upper()
        ligne = input("Entrez le numéro de la case (1–10) : ")

        # Vérifier les entrées
        if colonne not in lettres:
            print("❌ Lettre invalide. Choisissez entre A et J.")
            continue
        if ligne not in ["1","2","3","4","5","6","7","8","9","10"]:
            print("❌ Numéro invalide. Choisissez entre 1 et 10.")
            continue

        i = int(ligne) - 1
        j = lettres.index(colonne)

        # Vérifier le contenu de la case
        if grille_adversaire[i][j] == "🚢":
            print("💥 TOUCHÉ !")
            grille_adversaire[i][j] = "💥"   # marque la case touchée
        elif grille_adversaire[i][j] == "🌊":
            print("💧 Tir raté !")
            grille_adversaire[i][j] = "☠️"   # marque la case manquée
        else:
            print("⚠️ Cette case a déjà été attaquée.")
            continue  # redemande une nouvelle case

        afficher_grille(grille_adversaire)
        break



# main

grille = creer_grille()
afficher_grille(grille)
placer_bateau(grille)



#  appl de la fonction Grille de l'adversaire
grille_adversaire = creer_grille()
grille_adversaire[5][5] = "🚢"  # On place un bateau pour tester

afficher_grille(grille_adversaire)
attaquer(grille_adversaire)







