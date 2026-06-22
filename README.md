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

```

