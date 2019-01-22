# -*- coding: utf-8 -*-
#Ce programme vise à créer une interface pour paramétrer et jouer au dilemme du prisonnier

import expyriment
from  expyriment.stimuli import Picture



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

# Set develop mode. Comment for real experiment
expyriment.control.set_develop_mode(on=True)

expyriment.control.initialize(exp)


# Creation du stimuli et des trials

instructions = expyriment.stimuli.TextScreen("Bienvenue dans le monde du dilemme du prisonnier",
        "Un partenaire de jeu va vous être présenté. Votre objectif sera de maximiser votre score. Vous pouvez presser 'a' pour choisir de coopérer, 'b' pour choisir de trahir")

block = expyriment.design.Block(name="jeu")  # create a block (which will consists in a series of trials)


stim = expyriment.stimuli.TextLine(text="coopérer ou trahir")
stim.preload()


for i in range(Nbtours):
    trial = expyriment.design.Trial()
    trial.add_stimulus(stim)
    block.add_trial(trial)

exp.add_block(block)

kb = exp.keyboard  # response device
exp.data_variable_names(['key', 'rt'])

# Lancement du jeu
expyriment.control.start()

for b in exp.blocks:
    for t in b.trials :
        for s in t.stimuli:
            s.present()
        key, rt =kb.wait([expyriment.misc.constants.K_a,
                                     expyriment.misc.constants.K_p]
        exp.data.add([key, rt])

expyriment.control.end()   
