# Projet
## Description
Ce projet permet de simuler une grande quantité de chasses aux trésors, mini-jeu issu d'Idle Slayer, afin d'observer les performances (taux de victoire et autres) de différents algorithmes.

### Présentation du mini jeu simulé
- 30 coffres sont présentés au joueur, à ouvrir 1 par 1.
- 4 de ces coffres sont des mimiques, qui font perdre la partie.
- 1 de ces coffre est le bouclier, et est indiqué. Permet de tuer un mimique.
- 1 de ces coffres est le X2, qui double le prochain coffre ouvert

Enfin, Le joueur dispose de deux boucliers de cristal, qui protègent le joueur pour ses deux premiers coffres ouverts.

Le but est d'arriver à la fin de la chasse aux trésors avec seulement des coffres contenant des mimiques ou plus aucun coffre, cela correspond à une victoire. 

### Algorithmes comparés
- "_full gamble_" :
Choisit toujours un coffre aléatoire peu importe le résultat, jusqu'à la fin de la partie.
- "_shield direct_"
Ouvre toujours deux coffres aléatoires puis ouvre le coffre contenant le bouclier, puis ouvre des coffres jusqu'à la fin de la chasse.
- "_double shield_"
Ouvre des coffres jusqu'à trouver le X2, puis double le bouclier, avant d'ouvrir des coffres jusqu'à la fin.
- "_raisonnable_"
Ouvre deux coffres grâce aux boucliers de cristal.

  - Si un mimique a été trouvé (et donc tué), l'algorithme se comporte comme "_double shield_".
  - Si un X2 a été trouvé, l'algorithme se comporte comme "_double shield_".
  - Sinon, l'algorithme se comporte comme "_shield direct_".

## Auteur

- ChickenInKFCgit.

# Exemple d'utilisation :
Demande : 5000 générations et 3 simulations

Résultat :
```
--------------------------------------------------------------------------------------
# RESULTATS FINAUX POUR **5 SIMULATIONS** DE **50000 GENRATIONS**
--------------------------------------------------------------------------------------
### algo_FULL_GAMBLE 
Moyenne Mimics : 0.543 | Moyenne Coffres : 9.663 | Winrate : 0.094% | wins : 47.2/50000
### algo_SHIELD_DIRECT 
Moyenne Mimics : 1.343 | Moyenne Coffres : 15.372 | Winrate : 0.163% | wins : 81.6/50000
### algo_DOUBLE_SHIELD 
Moyenne Mimics : 0.82 | Moyenne Coffres : 11.037 | Winrate : 1.464% | wins : 732.2/50000
### algo_RAISONNABLE 
Moyenne Mimics : 0.692 | Moyenne Coffres : 10.649 | Winrate : 1.958% | wins : 979.0/50000
```
Le format markdown, une fois interprété, ressemble à :

--------------------------------------------------------------------------------------
# RESULTATS FINAUX POUR **5 SIMULATIONS** DE **50000 GENRATIONS**
--------------------------------------------------------------------------------------
### algo_FULL_GAMBLE 
Moyenne Mimics : 0.543 | Moyenne Coffres : 9.663 | Winrate : 0.094% | wins : 47.2/50000
### algo_SHIELD_DIRECT 
Moyenne Mimics : 1.343 | Moyenne Coffres : 15.372 | Winrate : 0.163% | wins : 81.6/50000
### algo_DOUBLE_SHIELD 
Moyenne Mimics : 0.82 | Moyenne Coffres : 11.037 | Winrate : 1.464% | wins : 732.2/50000
### algo_RAISONNABLE 
Moyenne Mimics : 0.692 | Moyenne Coffres : 10.649 | Winrate : 1.958% | wins : 979.0/50000

