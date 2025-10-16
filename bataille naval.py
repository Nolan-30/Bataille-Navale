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
        print(lettres[i], end="  ") # on affiche la lettre 
        for case in grille[i]:     
            print(case, end="  ")   # on affiche tt les cases
        print()                    
        
        
def placer_bateau(grille):
    
    lettres = ["A","B","C","D","E","F","G","H","I","J"]

    while True: 

        ligne = input("Entrez une lettre (A–J) : ").upper()
        colonne = input("Entrez un numéro (1–10) : ")

        # on vérifie que la ligne est dans la liste des lettres
        if ligne not in lettres:
            print("Cette lettre n'est pas entre A et J.")
            continue

        # vérifier que la colonne est dans la lsite des nbrs
        if colonne not in ["1","2","3","4","5","6","7","8","9","10"]:
            print("Entrez  un nombre entre 1 et 10.")
            continue

        i = lettres.index(ligne)
        j = int(colonne) - 1
        

        # on vérifie si on peut poser un bateau
        if grille[i][j] != "🌊":
            print("Il y a déjà un bateau dans cette case ")
            continue

        # on place le bateau
        grille[i][j] = "🚢" 
        print("Le bateau est en position", ligne, ":", colonne)
        afficher_grille(grille) # On affiche pr voir si ça c bien actualisé
        
        break

def placer_5_bateaux(grille):
    for n in range(5):
        print("\n Placement du bateau n°", n+1)
        placer_bateau(grille)
    print("\n Bravo tu as bien placé tes 5 bateaux")
        

def placer_bateau_ia(grille):
    lettres = ["A","B","C","D","E","F","G","H","I","J"]

    while True:
        # l'IA choisi une case au hasard
        i = random.randint(0, 9)
        j = random.randint(0, 9)

        # on vérifie si l'IA peut poser un bateau
        if grille[i][j] != "🌊":
            continue  # 

        # sinon on met un bateau
        grille[i][j] = "🚢"
        break

        

def placer_5_bateaux_ia(grille):
    n = 0
    while n < 5:
        i = random.randint(0, 9)
        j = random.randint(0, 9)
        if grille[i][j] == "🌊":  # case libre
            grille[i][j] = "🚢"
            n += 1 # on augmente de 1 a chaque fois pr que l'IA se place pas plus de 5 bateaux
    print("\n L’IA a placé ses 5 bateaux")

    
    
def attaquer(grille_adversaire):
    lettres = ["A","B","C","D","E","F","G","H","I","J"]

    while True:
        colonne = input("Entrez la lettre de la case à attaquer (A–J) : ").upper()
        ligne = input("Entrez le numéro de la case (1–10) : ")

        
        if colonne not in lettres:
            print("Choisir entre A et J.")
            continue
        if ligne not in ["1","2","3","4","5","6","7","8","9","10"]:
            print("Choisir entre 1 et 10.")
            continue

        i = int(ligne) - 1
        j = lettres.index(colonne)

        # # on verifie ce qu'il y a dans la case
        if grille_adversaire[i][j] == "🚢":
            print("TOUCHÉ ")
            grille_adversaire[i][j] = "💥"   # ça marque le motif marque une attaque qui a touché un bateau
        elif grille_adversaire[i][j] == "🌊":
            print(" Tir raté")
            grille_adversaire[i][j] = "❌"   # ca marque la case qu'a été raté
        else:
            print("Cette case a déjà été attaquée.")
            continue  

        afficher_grille(grille_adversaire)
        break
    
    
def attaque_ia(grille_joueur):
    lettres = ["A","B","C","D","E","F","G","H","I","J"]

    print("L’IA est entrain d'attaqué")

    while True:
        
        # l'IA choisit une case au hasard
        i = random.randint(0, 9)
        j = random.randint(0, 9)

        # Vérifier le contenu de la case
        if grille_joueur[i][j] == "🚢":
            print(f"L’IA a touché un de tes bateaux ") # On affiche que l'Ia m'a touché et on donne aussi les coordonnées du bateau auquel elle a touchée
            grille_joueur[i][j] = "💥"
        elif grille_joueur[i][j] == "🌊":
            print(f"L’IA a raté son tir ")
            grille_joueur[i][j] = "❌"
        else:
            # ca veut dire que la case a deja ete jouee dcp on recommence
            continue
        break

    afficher_grille(grille_joueur)




# main

grille = creer_grille()
afficher_grille(grille)




#  appl de la fonction grille de l'adversaire
grille_adversaire = creer_grille()


# placement des bateaux pr l'humain et l'IA
placer_5_bateaux(grille)
placer_5_bateaux_ia(grille_adversaire)

afficher_grille(grille_adversaire)

      











