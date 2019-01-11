# -*- coding: utf-8 -*-

# Ce programme vise à simuler un dilemme du prisonnier entre deux joueurs.

# fonction de choix
# recueil le choix du joueur entre coopérer et trahir
def choix():
    action = 'r' # action prend une valeur non significative qui permet de débuter la boucle while
    while action != 'a' or action != 'p':
        action = input("Souhaitez vous coopérer (a) ou trahir (p) :") 
        if action == 'a' :
            return 'C' # 'C' pour coopérer
        elif action == 'p' :
            return 'T' # 'T' pour trahir
        else  : # Retour à la première instruction dans tous les autres cas avec rappel.
            print("Merci de n'utiliser que les touche 'a' et 'p' du clavier") 


# fonction de gains
# Prend en paramètre l'action choisie par le joueur, celle du partenaire virtuel et applique en fonction de ces derniers, la matrice des gains.       
def gains(ActionJ, ActionPV, GainC, GainT, PerteC, PerteT) : #ActionJ = action du joueur ; ActionPV = action du PV ; GainC = Gains si les deux partenaires coopèrent ; GainT = Gains du partenaire qui a trahi si l'autre à coopérer ; PerteT = Perte si les deux joueurs ont trahi ; PerteC = Perte du partenaire qui a coopéré quand l'autre a trahi. 
    if ActionJ== 'C' and ActionPV== 'C' :
        return (GainC, GainC)
    if ActionJ== 'C' and ActionPV== 'T':
        return (PerteC, GainT)
    if ActionJ== 'T' and ActionPV== 'C' :
        return (GainT, PerteC)
    if ActionJ== 'T' and ActionPV== 'T':
        return (PerteT, PerteT)
    
# fonction de choix parametrage par defaut
# Demande à l'expérimentateur si il souhaite utiliser les paramètres par défaut ou paramétrer lui-même l'expérience.
def parametrage() :
    parametre = 'r'
    while parametre != 'a' or parametre != 'p':
        parametre = input("Souhaitez vous utilisez les paramètres par défaut (a) ou paramétrer l'expérience (p) :") 
        if parametre == 'a' :
            return 'D' # 'D' pour défaut
        elif parametre == 'p' :
            return 'P' # 'P' pour paramétrer
        else  : # Retour à la première instruction dans tous les autres cas avec rappel.
            print("Merci de n'utiliser que les touche 'a' et 'p' du clavier")       
        
 
# Bloc de paramétrage  
parametre = parametrage()

if parametre == 'D' :
    GainC = 2
    GainT = 3
    PerteC = -2
    PerteT = 0
    Nbtours = 10
    
if parametre == 'P':   
    print("Vous allez maintenant paramétrer le dilemme du prisonnier.")
    GainC = int(input("Choisir le montant du gain de chaque partenaire si les deux partenaires coopérent : " ))
    GainT =int(input("Choisir le montant du gain du partenaire qui trahit si l'autre coopère : " ))
    PerteC =int(input("Choisir le montant de la perte du partenaire qui coopère si l'autre trahit : " ))
    PerteT =int(input("Choisir le montant de la perte de chaque partenaire si les deux partenaires trahisent : " ))
    Nbtours = int(input("Choisir le nombre de tours de jeu : "))

# Initialisation
scoreJ = 0 #Score du Joueur, nul au début du jeu
scorePV = 0 #Score du partenaire Virtuel, nul au début du jeu
n = 0 #indice des tours
ActionPV = 'C' # Initialisation de l'action du PV : coopère au premier tour

# Début du jeu
print("Vous allez jouer avec un partenaire dont vous verez le visage")

while n < Nbtours :
    n+=1
    ActionJ = choix()
    scoreJ+= gains(ActionJ, ActionPV, GainC, GainT, PerteC, PerteT)[0]
    scorePV += gains(ActionJ, ActionPV, GainC, GainT, PerteC, PerteT)[1]
    ActionPV = ActionJ
    print("Score du joueur = ", scoreJ, " Score du partenaire = ", scorePV)

# Fin du jeu
print("Scores finaux : Joueur : ", scoreJ,"  Partenaire : ", scorePV)
print("Merci d'avoir participer. L'expérience est terminée, veuillez appeler l'expérimentateur.")

    
      
