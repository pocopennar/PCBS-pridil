# PCBS-pridil

## Description du projet

Je projette de réaliser un jeu du dilemme du prisonnier avec une interface utilisateur permettant de présenter des images afin de faire varier le visage des partenaires.
Le nombre de tours du dilemme doit pouvoir être fixé par l’expérimentateur. (éventuellement ajouter une option avec nombre de tours aléatoire)
La photo du partenaire  doit pouvoir être changée (il devrait être possible d’en télécharger de nouvelles).
Les paramètres de gains et de pertes du dilemme doivent également pouvoir être programmable.
Le partenaire virtuel (PV) jouera une stratégie élémentaire tit-for-tat.
Les données sur les actions des joueurs doivent être collecté.
L'objectif serait d'observer les variations du comportement des utilisateurs en fonction du faciès du partenaire.

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
__Sommaire__

- [Un dilemme du prisonnier classique](#un-dilemme-du-prisonnier-classique)
    - [Paramétrage ou paramètre par défaut](#paramétrage-ou-paramètre-par-défaut)
    - [Action du joueur](#action-du-joueur)
    - [Calcul des gains](#calcul-des-gains)
    - [Déroulement du jeu](#déroulement-du-jeu)
- [Version expyriment du dilemme du prisonnier](#version-expyriment-du-dilemme-du-prisonnier)
- [CONCLUSION](#conclusion)
    
 Version expyriment du dilemme du prisonnier

<!-- markdown-toc end -->



## Un dilemme du prisonnier classique

_La section présente propose un programme basique permettant de jouer un dilemme du prisonnier contre un partenaire virtuelle jouant une stratégie "Tit-for-Tat". Elle commence par l'exposition des fonctions qui seront utilisés puis présente le déroulement du jeu._

### Paramétrage ou paramètre par défaut

Le fonction parametrage demande  à l'expérimentateur s'il souhaite paramètrer lui-même l'expérience ou utiliser les paramètres par défaut.

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

La fonction choix() doit demander au joueur de choisir entre les deux options : coopérer ou trahir.
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
 
 ## Déroulement du jeu
 
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


 </code></pre>


## Version expyriment du dilemme du prisonnier

_Nous allons adapté le code pour utiliser la bibliothèque __expyriment__. Cela devrait nous permettre de générer une interface utilisateur plus attrayante. Nous devons également mettre en place l'affichage de photos et la collecte de données._

### 


## CONCLUSION
