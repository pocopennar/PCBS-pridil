# -*- coding: utf-8 -*-
###Ce programme vise à créer une interface pour paramétrer et jouer au dilemme du prisonnier

### Import et path
import expyriment, os
from  expyriment.stimuli import Picture

STIMDIR = "stimuli"

### Définition des fonctions 
# fonction de gains
# Prend en paramètre l'action choisie par le joueur, celle du partenaire virtuel et applique en fonction de ces derniers, la matrice des gains.       
def gains(ActionJ, ActionPV, GainC, GainT, PerteC, PerteT) : #ActionJ = action du joueur ; ActionPV = action du PV ; GainC = Gains si les deux partenaires coopèrent ; GainT = Gains du partenaire qui a trahi si l'autre à coopérer ; PerteT = Perte si les deux joueurs ont trahi ; PerteC = Perte du partenaire qui a coopéré quand l'autre a trahi. 
    if ActionJ == expyriment.misc.constants.K_q and ActionPV == expyriment.misc.constants.K_q :
        return (GainC, GainC)
    if ActionJ == expyriment.misc.constants.K_q and ActionPV == expyriment.misc.constants.K_p :
        return (PerteC, GainT)
    if ActionJ == expyriment.misc.constants.K_p and ActionPV == expyriment.misc.constants.K_q :
        return (GainT, PerteC)
    if ActionJ == expyriment.misc.constants.K_p and ActionPV == expyriment.misc.constants.K_p :
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
            
            
### Paramétrage  
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


### Initialisation de l'expérience
exp = expyriment.design.Experiment(name="Prisoner_dilemma")  

expyriment.control.set_develop_mode(on=True)

expyriment.control.initialize(exp)


### Creation des stimulis et des trials
block = expyriment.design.Block(name = "jeu")  


stim1 = expyriment.stimuli.TextLine(text = "Désirez vous coopérer (a)  ou  trahir (p)")
stim1.preload()
stim2 = expyriment.stimuli.TextLine(text = "Votre partenaire coopère.")
stim2.preload()
stim3 = expyriment.stimuli.TextLine(text = "Votre partenaire trahie.")
stim3.preload()

imagefile = 'stimuli1.jpg'
stim = os.path.join(STIMDIR, imagefile)
if not os.path.isfile(stim):
    print(f'{stim} introuvable' )
    assert False
    
stimphoto = expyriment.stimuli.Picture(stim)
stimphoto.preload()


for i in range(Nbtours):
    trial = expyriment.design.Trial()
    trial.add_stimulus(stim1)
    trial.add_stimulus(stim2)
    trial.add_stimulus(stim3)
    trial.add_stimulus(stimphoto)
    block.add_trial(trial)

exp.add_block(block)

kb = exp.keyboard  


### Initialisation des variables
scoreJ = 0  #Score du Joueur, nul au début du jeu
scorePV = 0  #Score du partenaire Virtuel, nul au début du jeu

exp.add_data_variable_names(['key', 'rt'])

### Lancement du jeu
expyriment.control.start(skip_ready_screen = True)

expyriment.stimuli.TextScreen("Bienvenue dans le monde du dilemme du prisonnier",
        "Un partenaire de jeu va vous être présenté. Votre objectif sera de maximiser votre score. Vous pouvez presser 'a' pour choisir de coopérer, 'b' pour choisir de trahir").present()
kb.wait()

for b in exp.blocks :
    ActionPV = expyriment.misc.constants.K_q  # Initialisation de l'action du PV : coopère au premier
    for t in b.trials :
        stimphoto.present()
        kb.wait()
        
        stim1.present()
        key, rt = kb.wait([expyriment.misc.constants.K_q,
                                     expyriment.misc.constants.K_p])

        if ActionPV == expyriment.misc.constants.K_q : # Cas de coopération 
            stim2.present()
            kb.wait()
           
        if ActionPV ==  expyriment.misc.constants.K_p : # Cas de trahison
            stim3.present() 
            kb.wait()
            
        scoreJ+= gains(key, ActionPV, GainC, GainT, PerteC, PerteT)[0] # on traite 'key' comme 'ActionJ'
        scorePV += gains(key, ActionPV, GainC, GainT, PerteC, PerteT)[1]
        
        ActionPV = key
        
        exp.data.add([key, rt])  
        
         
# expyriment.stimuli.TextScreen("Scores Finaux", "Joueur : ", scoreJ, "Partenaire : ", scorePV).present()
# kb.wait()    
#expyriment.stimuli.TextScreen("Le jeu est terminé, merci d'avoir participer. Vous pouvez appelez l'expérimentateur.").present()   
     
expyriment.control.end()
