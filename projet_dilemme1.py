# -*- coding: utf-8 -*-

# Ce programme vise à simuler un dilemme du prisonnier entre deux joueurs.

scoreJ = 0 #Score du Joueur, nul au début du jeu
scoreV = 0 #Score du partenaire Virtuel, nul au début du jeu

# fonction choix
# recueil le choix du joueur entre coopérer et trahir
def choix():
    action = input("Souhaitez vous coopérer (a) ou trahir (p) :") 
    if action == 'a' :
        return 'C' # 'C' pour coopérer
    elif action == 'p' :
        return 'T' # 'T' pour trahir
    else  : # Retour à la première instruction dans tous les autres cas avec rappel.
        print("Merci de n'utiliser que les touche 'a' et 'p' du clavier") 
        choix()

