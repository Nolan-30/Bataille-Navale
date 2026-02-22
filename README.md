# ⚓ Bataille Navale 🌊
Bienvenue dans ce jeu de Bataille Navale classique développé en Python ! Affronte une intelligence artificielle dans un duel stratégique en haute mer. 🚢

📝 Description du projet
ce programme simule une partie de bataille navale sur une grille de 10x10. Le but est simple : couler tous les navires ennemis avant que les tiens ne finissent au fond de l'océan.

Symbole	    |    Signification
💧	Eau     |    Case inexplorée
⛵️	Bateau  |    Ta flotte
💥	Touché  |    Cible atteinte 
❌	Manqué  |    Plouf... dans l'eau

## 🚀 Comment jouer ?
Préparation de la flotte 🛠️ : Place tes 5 bateaux stratégiquement en entrant les coordonnées (ex: A 5).

Déploiement de l'IA 🤖 : L'ordinateur place ses 5 bateaux de manière aléatoire et secrète.

Combat au tour par tour ⚔️ :

Choisis une coordonnée pour attaquer la grille adverse.

L'IA réplique immédiatement après ton tir.

Victoire 🏆 : Le premier à couler les 5 navires adverses remporte la partie !

## ⚙️ Fonctionnalités techniques
Le code est découpé en modules logiques pour une meilleure lisibilité :

Gestion de la Mer : creer_grille() et afficher_grille() pour générer et dessiner l'espace de jeu avec les coordonnées A-J et 1-10.

Logistique de Placement : Fonctions dédiées pour le placement manuel (placer_5_bateaux) et le placement aléatoire de l'IA (placer_5_bateaux_ia).

Système de Tir : attaquer() et attaque_ia() gèrent les impacts et mettent à jour les grilles en temps réel.

Arbitrage : tous_bateaux_coules() et verifier_victoire() analysent l'état de la partie pour annoncer le gagnant.

## 🛠️ Installation et Lancement
Assure-toi d'avoir Python 3 installé sur ton ordinateur.

Télécharge le fichier bataille_navale.py, puis lancer le .


