# -*- coding: utf-8 -*-
#Ce programme vise à créer une interface via expyriment pour jouer au dilemme du prisonnier


import random
import expyriment
from  expyriment.stimuli import Picture

# fonction de gains
# Prend en paramètre l'action choisie par le joueur, celle du partenaire virtuel et applique en fonction de ces derniers, la matrice des gains.       
def gains(ActionJ, ActionPV, GainC, GainT, PerteC, PerteT) : #ActionJ = action du joueur ; ActionPV = action du PV ; GainC = Gains si les deux partenaires coopèrent ; GainT = Gains du partenaire qui a trahi si l'autre à coopérer ; PerteT = Perte si les deux joueurs ont trahi ; PerteC = Perte du partenaire qui a coopéré quand l'autre a trahi. 
    if ActionJ== 'a' and ActionPV== 'a' :
        return (GainC, GainC)
    if ActionJ== 'a' and ActionPV== 'p':
        return (PerteC, GainT)
    if ActionJ== 'p' and ActionPV== 'a' :
        return (GainT, PerteC)
    if ActionJ== 'p' and ActionPV== 'p':
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
exp = expyriment.design.Experiment(name="Prisoner_dilemma")  # create an Experiment object

## Set develop mode. Comment for real experiment
expyriment.control.set_develop_mode(on=True)

expyriment.control.initialize(exp)


## Creation des stimulis et des trials

block = expyriment.design.Block(name="jeu")  # create a block (which will consists in a series of trials)


stim1 = expyriment.stimuli.TextLine(text = "coopérer ou trahir")
stim1.preload()
stim2 = expyriment.stimuli.TextLine(text = "Votre partenaire coopère.")
stim2.preload()
stim3 = expyriment.stimuli.TextLine(text = "Votre partenaire trahie.")
stim3.preload()

for i in range(Nbtours):
    trial = expyriment.design.Trial()
    trial.add_stimulus(stim1)
    trial.add_stimulus(stim2)
    trial.add_stimulus(stim3)
    block.add_trial(trial)

exp.add_block(block)

kb = exp.keyboard  

## Gestion des variables
scoreJ = 0 #Score du Joueur, nul au début du jeu
scorePV = 0 #Score du partenaire Virtuel, nul au début du jeu
n = 0 #indice des tours


# Lancement du jeu
    
## Participant    
expyriment.control.start(skip_ready_screen = True)

expyriment.stimuli.TextScreen("Bienvenue dans le monde du dilemme du prisonnier",
        "Un partenaire de jeu va vous être présenté. Votre objectif sera de maximiser votre score. Vous pouvez presser 'a' pour choisir de coopérer, 'b' pour choisir de trahir").present()
exp.keyboard.wait()

for b in exp.blocks:
    key = 0
    ActionPV = 113 # Initialisation de l'action du PV : coopère au premier
    for t in b.trials :
        stim1.present()
        key = kb.wait([expyriment.misc.constants.K_q,
                                     expyriment.misc.constants.K_p])

        if ActionPV == 113 : # valeur constant q
            stim2.present()
            exp.keyboard.wait() 
        if ActionPV ==  112 : # valeur constant p
            stim3.present() 
            exp.keyboard.wait()
            
        
        ActionPV = key
        
      
expyriment.control.end()   
