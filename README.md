# PCBS-pridil

## Description du projet

Je projette de réaliser un jeu du dilemme du prisonnier avec une interface utilisateur permettant de présenter des images afin de faire varier le visage des partenaires.
Le nombre de tours du dilemme doit pouvoir être fixé par l’expérimentateur. (éventuellement ajouter une option avec nombre de tours aléatoire)
La photo du partenaire  doit pouvoir être changée (il devrait être possible d’en télécharger de nouvelles).
Les paramètres de gains et de pertes du dilemme doivent également pouvoir être programmable.
Le partenaire virtuel (PV) jouera une stratégie élémentaire tit-for-tat.
L'objectif serait d'observer les variations du comportement des utilisateurs en fonction du faciès du partenaire.



## Fonctions

_On a fait le choix de pré-définir des fonctions plutôt que d'utiliser des procédures avec d'éventuelles variables globales. La section présente expose donc l'esprit et la formalisation des fonctions qui serviront de base à un programme permettant de jouer un dilemme du prisonnier face à un PV jouant une stratégie 'Tit-for-Tat'._


### Action du joueur : fonction choix()

La fonction choix() doit demander au joueur de choisir entre les deux options : coopérer ou trahir.
Ce choix déterminera le retour d'une valeur utilisée pour le calcul de l'attribution des points.
Elle pourra eventuellement être utilisée comme variable pour la détermination de l'action future du PV.

<pre><code>
def choix():
    action = input("Souhaitez vous coopérer (a) ou trahir (p) :") 
    if action == 'a' :
        return 'C'
    elif action == 'p' :
        return 'T'
    else  :
        print("Merci de n'utiliser que les touche 'a' et 'p' du clavier") 
 </code></pre>
 
 ### Calcul des gains : fonction gains()
 
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
# bloc de paramétrage     
print("Vous allez maintenant paramétrer le dilemme du prisonnier.")
GainC = input("Choisir le montant du gain de chaque partenaire si les deux partenaires coopérent : " )
GainT =input("Choisir le montant du gain du partenaire qui trahit si l'autre coopère : " )
PerteC =input("Choisir le montant de la perte du partenaire qui coopère si l'autre trahit : " )
PerteT =input("Choisir le montant de la perte de chaque partenaire si les deux partenaires trahisent : " )
Nbtours = input("Choisir le nombre de tours de jeu : "))
scoreJ = 0 #Score du Joueur, nul au début du jeu
scorePV = 0 #Score du partenaire Virtuel, nul au début du jeu
n = 0 #indice des tours

# début du jeu
while n < Nbtours :
    n+=1
    ActionJ = choix()
    scoreJ+= gains(ActionJ, ActionPV, GainC, GainT, PerteC, PerteT)[0]
    scorePV += gains(ActionJ, ActionPV, GainC, GainT, PerteC, PerteT)[1]
    ActionPV = ActionJ
    print("Score du joueur = ", scoreJ, " Score du partenaire = ", scorePV)
print("Scores finaux : Joueur : ", scoreJ,"  Partenaire : ", scorePV)
print("Merci d'avoir participer. L'expérience est terminée, veuillez appeler l'expérimentateur.")


 </code></pre>
