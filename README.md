# PCBS-pridil

https://pocopennar.github.io/PCBS-pridil/

## Description du projet

Je projette de réaliser un jeu du dilemme du prisonnier avec une interface utilisateur permettant de présenter des images afin de faire varier le visage des partenaires. L'objectif serait d'observer les variations du comportement des joueurs en fonction du faciès du partenaire.

Le programme doit répondre à un certain nombre d'éxigences :
- Le nombre de tours du dilemme et les paramètres de gains et de pertes du dilemme doivent également pouvoir être fixés par l'expérimentateur au début du programme.
- Le partenaire virtuel (PV) jouera une stratégie élémentaire 'Tit-for-Tat'.
- Les données sur les actions des joueurs doivent pouvoir être collectées.


<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
__Sommaire__

- [Un dilemme du prisonnier classique](#un-dilemme-du-prisonnier-classique)
    - [Paramétrage ou paramètre par défaut](#paramétrage-ou-paramètre-par-défaut)
    - [Action du joueur](#action-du-joueur)
    - [Calcul des gains](#calcul-des-gains)
    - [Déroulement du jeu 1](#déroulement-du-jeu-1)
- [Version expyriment du dilemme du prisonnier](#version-expyriment-du-dilemme-du-prisonnier)
    - [Fonctions utilisées](#fonctions-utilisées)
    - [Paramétrage](#paramétrage)
    - [Initialisation et préparation des stimulis](#initialisation-et-préparation-des-stimulis)
    - [Création des trials et du block](#création-des-trials-et-du-block)
    - [Déroulement du jeu 2](#déroulement-du-jeu-2)
- [CONCLUSION](#conclusion)
    - [Mon niveau initial](#mon-niveau-initial)
    - [Apprentissages lors du cours](#apprentissages-lors-du-cours)
    - [Regard sur le cours](#regard-sur-le-cours)

<!-- markdown-toc end -->



## Un dilemme du prisonnier classique

_La section présente propose un programme basique permettant de jouer un dilemme du prisonnier sur plusieurs tours contre un partenaire virtuel jouant une stratégie "Tit-for-Tat". Elle commence par l'exposition des fonctions qui seront utilisées puis présente le déroulement du jeu._

### Paramétrage ou paramètre par défaut

Le fonction parametrage demande à l'expérimentateur s'il souhaite paramètrer lui-même l'expérience ou utiliser les paramètres par défaut.

<pre><code>
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
 </code></pre>


### Action du joueur

La fonction choix() demande au joueur de choisir entre les deux options : coopérer ou trahir.
Ce choix déterminera le retour d'une valeur utilisée pour le calcul de l'attribution des points.
Elle est utilisée comme variable pour la détermination de l'action future du PV.

<pre><code>
def choix():
    action = 'r' # action prend une valeur non significative qui permet de débuter la boucle while
    while action != 'a' or action != 'p':
        action = input("Souhaitez vous coopérer (a) ou trahir (p) :") 
        if action == 'a' :
            return 'C' # 'C' pour coopérer
        elif action == 'p' :
            return 'T' # 'T' pour trahir
        else  : # Retour à la première instruction avec avertissement
            print("Merci de n'utiliser que les touche 'a' et 'p' du clavier") 
 </code></pre>
 
 
### Calcul des gains
 
 Prend en paramètre l'action choisie par le joueur, celle du PV et applique en fonction de ces derniers, la matrice des gains pour faire évoluer les scores.
 
 <pre><code>
def gains(ActionJ, ActionPV, GainC, GainT, PerteT, PerteC) : 
     if ActionJ== 'C' and ActionPV== 'C' :
        return (GainC, GainC)
    if ActionJ== 'C' and ActionPV== 'T':
        return (PerteC, GainT)
    if ActionJ== 'T' and ActionPV== 'C' :
        return (GainT, PerteC)
    if ActionJ== 'T' and ActionPV== 'T':
        return (PerteT, PerteT)
 </code></pre>
 
 
### Déroulement du jeu 1
 
 <pre><code>
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
print("Bienvenue dans le monde du dilemme du prisonnier",
        "Un partenaire de jeu va vous être présenté. Votre objectif sera de maximiser votre score. Vous pouvez presser 'a' pour choisir de coopérer, 'b' pour choisir de trahir")

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


 </code></pre>


## Version expyriment du dilemme du prisonnier

_Nous allons adapter le code pour utiliser la bibliothèque __expyriment__. Cela devrait nous permettre de générer une interface utilisateur plus attrayante. Nous devons également mettre en place l'affichage de photos et la collecte de données._

### Fonctions utilisées 

On modifie à la marge la fonction gain() du dilemme du prisonnier classique pour l'adapter à expyriment. 

 <pre><code>
#fonction de gains
# Prend en paramètre l'action choisie par le joueur, celle du partenaire virtuel et applique en fonction de ces derniers, la matrice des gains.       
def gains(ActionJ, ActionPV, GainC, GainT, PerteC, PerteT) : 
    if ActionJ== expyriment.misc.constants.K_q and ActionPV== expyriment.misc.constants.K_q :
        return (GainC, GainC)
    if ActionJ== expyriment.misc.constants.K_q and ActionPV== expyriment.misc.constants.K_p:
        return (PerteC, GainT)
    if ActionJ== expyriment.misc.constants.K_p and ActionPV== expyriment.misc.constants.K_q :
        return (GainT, PerteC)
    if ActionJ== expyriment.misc.constants.K_p and ActionPV== expyriment.misc.constants.K_p:
        return (PerteT, PerteT)    
  </code></pre>
  
  On réutilisera également la fonction parametrage() du dilemme du prisonnier classique.
            
### Paramétrage

Le paramétrage prend la même forme que dans le dilemme du prisonnier classique. 
Il a lieu dès le début du programme car le nombre de tour de jeu doit être connu pour créer les trials.

### Initialisation et préparation des stimulis

On commence par créer  une expérience avec expyriment. On créer les différents stimulus dont nous avons besoin. La demande de choix entre coopérer et trahir, les deux résultats possibles du comportement du partenaire et la photo du partenaire. On vérifie que le lien vers la photo est correcte, sans quoi on renvoit un message d'erreur.


<pre><code>
### Initialisation de l'expérience
exp = expyriment.design.Experiment(name="Prisoner_dilemma")  

expyriment.control.set_develop_mode(on=True)

expyriment.control.initialize(exp)


### Creation des stimulis

stim1 = expyriment.stimuli.TextLine("Désirez vous coopérer (a)  ou  trahir (p)")
stim1.preload()

imagefile = 'stimuli1.jpg'
stim = os.path.join(STIMDIR, imagefile)
if not os.path.isfile(stim):
    print(f'{stim} introuvable' )
    assert False
    
stimphoto = expyriment.stimuli.Picture(stim)
stimphoto.preload()

</code></pre>


### Création des trials et du block

En utilisant expyriment on créer le block de jeu. On va créer un nombre de 'trials' équivalent au nombre de tour grâce à une boucle 'for'. Chaque 'trial' contiendra les trois stimulus quatre stimulus précédents. On ajoute l'ensemble des 'trials' au block 'jeu'.

<pre><code>
block = expyriment.design.Block(name="jeu")

for i in range(Nbtours):
    trial = expyriment.design.Trial()
    trial.add_stimulus(stim1)
    trial.add_stimulus(stimphoto)
    block.add_trial(trial)

exp.add_block(block)

</code></pre>

### Déroulement du jeu 2

<pre><code>
### Initialisation des variables
scoreJ = 0  #Score du Joueur, nul au début du jeu
scorePV = 0  #Score du partenaire Virtuel, nul au début du jeu

exp.add_data_variable_names(['key', 'rt'])

### Lancement du jeu
expyriment.control.start(skip_ready_screen = True)

expyriment.stimuli.TextScreen("Bienvenue dans le monde du dilemme du prisonnier",
        "Un partenaire de jeu va vous être présenté. Votre objectif sera de maximiser votre score. Vous pouvez presser 'a' pour choisir de coopérer, 'b' pour choisir de trahir").present()
exp.keyboard.wait()

for b in exp.blocks:
    ActionPV = expyriment.misc.constants.K_q  # Initialisation de l'action du PV : coopère au premier
    for t in b.trials :
        stimphoto.present()
        kb.wait()
        
        stim1.present()
        key, rt = kb.wait([expyriment.misc.constants.K_q,
                                     expyriment.misc.constants.K_p])

         if ActionPV == expyriment.misc.constants.K_q : # Cas de coopération 
            expyriment.stimuli.TextScreen("Votre partenaire coopère.", "Votre score : %s    Score de votre partenaire : %s"%(scoreJ, scorePV) ).present()
            kb.wait()
           
        if ActionPV ==  expyriment.misc.constants.K_p : # Cas de trahison
            expyriment.stimuli.TextScreen("Votre partenaire trahie.", "Votre score : %s    Score de votre partenaire : %s"%(scoreJ, scorePV) ).present()
            kb.wait()
            
        scoreJ+= gains(key, ActionPV, GainC, GainT, PerteC, PerteT)[0] # on traite 'key' comme 'ActionJ'
        scorePV += gains(key, ActionPV, GainC, GainT, PerteC, PerteT)[1]
        
        ActionPV = key
        
        exp.data.add([key, rt])  
        
expyriment.stimuli.TextScreen("Votre score final : %s    Score de votre partenaire : %s" %(scoreJ, scorePV), "Le jeu est terminé. Merci d'avoir participer. Vous pouvez appelez l'expérimentateur.").present()   
kb.wait()

expyriment.control.end()

</code></pre>

### Perspective de développement

Plusieurs pistes de développement et d'amélioration du programme sont envisageables : 
 - Il faudrait faire évoluer l'interface pour que le visage du partenaire persiste malgré l'évolution des autres stimulis.
 - La matrice des gains pourrait être présentée au joueur au début de l'expérience.
 - Les scores pourraient être présents en permanence à l'écran.
 - Il faudrait faire évoluer le programme pour changer facilement le visage du partenaire à partir d'une bibliothèque de photos.
 
## CONCLUSION

### Mon niveau initial

Je n'avais jamais utilisé python avant le début de l'année. 
Je savais faire des boucles et des fonctions simples sur Scilab en classe préparatoire (ECS).


### Apprentissages lors du cours

La première partie de mon apprentissage s'est concentrée sur la manipulation basique de Python : l'apprentissage des commandes (+=, boucle for, def de fonction) et de l'organisation sur python (définition préalable des fonctions, leur utilisation dans le programme).

La deuxième partie a été centrée autour de la compréhension et de l'utilisation de la bibliothèque _expyriment_. J'ai appris à créer des trials et des blocks en comprennant leur imbrication. J'ai aussi appris à gérer les images sur python et à utiliser markdown.

J'ai passé un temps incroyable face à des blocages simplement dûs à un manque de rigueur dans la gestion des variables ou une mauvaise écriture : je pense y avoir gagné en rigueur. J'ai finalement réaliser deux programmes qui constituent deux étapes dans mon apprentissage, j'ai jugé bon de laisser le premier ('dilemme du prisonnier classique') car c'est en le programmant que j'ai acquis les bases et le second programme utilisant _expyriment_ en découle largement. 


### Regard sur le cours

L'équilibre est bon entre les exercices à faire chez soi et le retour sur ces exercices en cours. Néanmoins au moins l'un d'entre eux pourrait être obligatoire chaque semaine. Face à l'hétérogénéité du niveau de la classe, les exercices pourrait être de différents niveau, chacun rendant celui qui correspond le mieux à son niveau. 

