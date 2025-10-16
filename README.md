# Jeu de Bataille Navale en Python

## Descript°

Un jeu de **Bataille Navale** où le joueur affronte une IA sur une grille 10x10.

## Symboles :

- 🌊 : eau
- 🚢 : bateau
- 💥 : bateau touché
- ❌ : tir manqué

Le joueur place 5 bateaux et l'IA aussi mais de maniere aleatoire
Les 2 s'attaque chacun leur tour jusqu'à ce que tous les bateaux d'un coule

## Comment jouer

1. Placer vos 5 bateaux sur la grille en choisissant une lettre (colonne) et un chiffre (ligne).
2. Attaquer la grille de l'IA à chaque tour.
3. L'IA attaque votre grille après votre tour.
4. Le jeu se termine quand tous les bateaux d'un joueur sont détruits.

## Fonctionnalités principales

- Créer et afficher la grille (`creer_grille`, `afficher_grille`)
- Placer les bateaux du joueur et de l'IA (`placer_bateau`, `placer_5_bateaux`, `placer_bateau_ia`, `placer_5_bateaux_ia`)
- Attaquer (`attaquer`, `attaque_ia`)
- Vérifier si tous les bateaux sont coulés et déterminer le vainqueur (`tous_bateaux_coules`, `verifier_victoire`)

# Lancement du projet

Il suffit de lancer le fichier "bataille naval.py"
