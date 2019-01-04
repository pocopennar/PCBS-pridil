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

# fonction de gains
# Prend en paramètre l'action choisie par le joueur, celle du partenaire virtuel et applique en fonction de ces derniers, la matrice des gains pour faire évoluer les scores.       
def gains(ActionJ, ActionPV, GainC, GainT, PerteT, PerteC) : #ActionJ = action du joueur ; ActionPV = action du PV ; GainC = Gains si les deux partenaires coopèrent ; GainT = Gains du partenaire qui a trahi si l'autre à coopérer ; PerteT = Perte si les deux joueurs ont trahi ; PerteC = Perte du partenaire qui a coopéré quand l'autre a trahi. 
    if ActionJ== 'C' and ActionPV== 'C' :
        scoreJ += GainC
        scorePV += GainC
    if ActionJ== 'C' and ActionPV== 'T':
        scoreJ += PerteC
        scorePV += GainT
    if ActionJ== 'T' and ActionPV== 'C' :
        scoreJ += GainT
        scorePV += PerteC
    if ActionJ== 'T' and ActionPV== 'T':
        scoreJ += PerteT
        scorePV += PerteT
