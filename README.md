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
Ce choix détemrinera le retour d'une valeur utilisée pour le calcul de l'attribution des points.
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
        choix()
 </code></pre>
 
 ### Calcul des gains : fonction gains()
 
 Prend en paramètre l'action choisie par le joueur, celle du PV et applique en fonction de ces derniers, la matrice des gains pour faire évoluer les scores.
 
 <pre><code>
def gains(ActionJ, ActionPV, GainC, GainT, PerteT, PerteC) : 
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
 </code></pre>
