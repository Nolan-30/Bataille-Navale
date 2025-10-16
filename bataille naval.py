import random

def creer_grille():
    
    """
    
    fonction qui retourne la grille de jeu 10x10 initialisée avec des vagues 🌊.
    aucun parametres
    elle retourne la grille
    
    """

    grille = []
    for i in range(10):
        ligne = []
        for j in range(10):
            ligne.append("🌊")
        grille.append(ligne)
    return grille

def afficher_grille(grille):
    """
    
    la fonction affiche av les lettres (A–J) en haut et les numéros (1–10) à gauche.

    parametres :
    grille : c'est une liste de liste
    aucun retour
    """
    
    lettres = ["A","B","C","D","E","F","G","H","I","J"]

    # Affiche les lettres en haut
    print("  ", end=" ")
    for lettre in lettres:
        print(lettre, end="  ")
    print()

    # affiche les num a gauche
    for i in range(10):
        
        # condition ici pr que ts les numéros des lignes  soient alignés 
        if i + 1 < 10:
            print(" " + str(i + 1), end=" ")
        else:
            print(str(i + 1), end=" ")
  
        for j in range(10): 
            print(grille[i][j], end=" ")  
        print()


                   
        
        
def placer_bateau(grille):
    """
    cette fonction permet au joueur de placer un bateau sur une case précise de la grille.
    parametres : grille
    aucun retour
    """
    lettres = ["A","B","C","D","E","F","G","H","I","J"]

    while True: 

        colonne = input("Entrez une lettre (A–J) : ").upper()
        ligne = input("Entrez un numéro (1–10) : ")

        if colonne not in lettres:
            print("Cette lettre n'est pas entre A et J.")
            continue

        if ligne not in ["1","2","3","4","5","6","7","8","9","10"]:
            print("Entrez un nombre entre 1 et 10.")
            continue

        # pr transformer les lettres et les numeros en indice
        
        j = lettres.index(colonne)  
        i = int(ligne) - 1          

        if grille[i][j] != "🌊":
            print("Impossible de placer un bateau dans cette case")
            continue

        grille[i][j] = "🚢" 
        print("Le bateau est en position", colonne, ":", ligne)
        afficher_grille(grille)
        break

def placer_5_bateaux(grille):
    """
    cette fonction permet  a l'humain de placer 5 bateaux d'affilés  sur sa grille.
    parametres : grille
    aucun retour
    """
    for n in range(5):
        print("\n Placement du bateau n°", n+1)
        placer_bateau(grille)
    print("\n Bravo tu as bien placé tes 5 bateaux")
        

def placer_bateau_ia(grille):
    """
    cette fonct° sert a placer un bateau  aléatoirement sur la grille de l’IA.
    paramètres : grile
    aucun retour
    """
    lettres = ["A","B","C","D","E","F","G","H","I","J"]

    while True:
        # l'IA choisi une case au hasard
        i = random.randint(0, 9)
        j = random.randint(0, 9)

        # on vérifie si l'IA peut poser un bateau
        if grille[i][j] != "🌊":
            print("Impossible de placer un bateau dans cette case")
            continue  

        # sinon on met un bateau
        grille[i][j] = "🚢"
        break

        

def placer_5_bateaux_ia(grille):
    """
    Place 5 bateaux  aléatoirement sur la grille de l’IA
    parametres : grille 
    aucun return
    """
    
    n = 0
    while n < 5:
        i = random.randint(0, 9)
        j = random.randint(0, 9)
        if grille[i][j] == "🌊":  # case libre
            grille[i][j] = "🚢"
            n += 1 # on augmente de 1 a chaque fois pr que l'IA ne place pas plus de 5 bateaux grace a la condition mise dans while
    print("\n L’IA a placé ses 5 bateaux")

    
    
def attaquer(grille_adversaire):
    """
    la fonction permet au joueur d’effectuer une attaque sur la grille de l’adversaire
    a un endroit précis
    La fonction met ensuite à jour la grille selon le résultat du tir et affiche le motif a la place de la case en qst
    
    Parametres :
    grille_adversaire
    aucun return
    
    """
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
            print("Tu viens de touché un bateau ! ")
            grille_adversaire[i][j] = "💥"   # ce motif marque qu'un bateau a été touché 
        elif grille_adversaire[i][j] == "🌊":
            print(" Tir raté")
            grille_adversaire[i][j] = "❌"   # ca marque la case qu'a été raté
        else:
            print("Cette case a déjà été attaquée.")
            continue  

        afficher_grille(grille_adversaire)
        break
    
    
def attaque_ia(grille_joueur):
    """
    Cette fonction permet a l'IA d'attaquer de maniere aleatoire la grille du joueur humain
    
    comme pr la fonct° "attaquer" elle met a jour la grille selon le resultat dur tir c'est a dire "💥" ou "❌"
    et elle affiche la grille du joueur apres l'attaque
    
    Parametres :
    grille_joueur
    
    aucun return
    """
    lettres = ["A","B","C","D","E","F","G","H","I","J"]

    while True:
        
        # l'IA choisit une case au hasard
        i = random.randint(0, 9)
        j = random.randint(0, 9)

        # on verifie  le contenu de la case
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


def tous_bateaux_coules(grille):
    """
    Cette fonction vérifie si tous les bateaux d'une grille ont coulés
    
    parametres : grille
    return True si tous les bateaux sont détruits
    sinon False
    """
    for ligne in grille:
        if "🚢" in ligne:
            return False
    return True

def verifier_victoire(grille_joueur, grille_ia):
    """
    Cette derniere fonct°
    vérifie l'etat de la partie et annonce le vainqueur du jeu
    
    parametres :
    grille_joueur
    grille_ia
    
    return True si un joueur a gagné
    False
    """
    if tous_bateaux_coules(grille_ia):
        print("\n Bravo ! Tu as coulé tous les bateaux de l'IA")
        return True
    elif tous_bateaux_coules(grille_joueur):
        print("\n Tous tes bateaux ont été coulés. L'IA a gagne !")
        return True
    return False



# main

grille = creer_grille()
grille_adversaire = creer_grille()

print(" Place tes 5 bateaux :")
placer_5_bateaux(grille)

print("\n L’IA place ses bateaux...")
placer_5_bateaux_ia(grille_adversaire)

# Affiche la grille de l'IA pour voir ses bateaux
print("\n Voici la grille de l’IA :")
afficher_grille(grille_adversaire)



print("\n Que le jeu commence !")





jeu_en_cours = True

while jeu_en_cours:

    print("\n A Ton tour d’attaquer :")
    attaquer(grille_adversaire)

    # on verifie si apres mon attaque j'ai gagner 
    if verifier_victoire(grille, grille_adversaire):
        jeu_en_cours = False
        continue # pr arrt le tour mm si qlq a gagné.


    print("\n Tour de l’IA :")
    attaque_ia(grille)

    # idem que pr l'IA
    if verifier_victoire(grille, grille_adversaire):
        jeu_en_cours = False

    
      












