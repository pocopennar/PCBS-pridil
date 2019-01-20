# -*- coding: utf-8 -*-

# Ce programme vise à créer une interface pour paramétrer et jouer au dilemme du prisonnier
import expyriment
from  expyriment.stimuli import Picture, BlankScreen

exp = expyriment.design.Experiment(name="Prisoner dilemma")
expyriment.control.initialize(exp)
 
block_jeu = expyriment.design.Block(name = "jeu")
trial = expyriment.design.Trial()
stim = expyriment.stimuli.TextLine(text = "coop ou trahir")
stim.preload()
trial.add_stimulus(stim)

blankscreen = BlankScreen()

data =[]
expyriment.control.start(skip_ready_screen = True)

expyriment.stimuli.TextScreen("Bienvenue dans le monde du dilemme du prisonnier",
        "Un partenaire de jeu va vous être présenté. Votre objectif sera de maximiser votre score. Vous pouvez presser 'a' pour choisir de coopérer, 'b' pour choisir de trahir").present()

exp.keyboard.wait()

for block in exp.blocks :
    for trial in block.trials :
        nbtour = 0
        while nbtour < 5 :
            nbtour += 1
            trial.stimuli.present()
            key, rt = exp.keyboard.wait([a,p])
            exp.data.add([block.name , trial.id, key, rt])
            

expyriment.control.end()          
