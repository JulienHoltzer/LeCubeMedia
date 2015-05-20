# Suivi du projet 


## SEMAINE 1

### Jour 1 : 27/04

Découverte du Cube

Liste du matériel

Mise à jour du repository GitHub

### Jour 2 : 28/04

Principes et usages

Lecture des codes sources du Cube

## SEMAINE 2

TODO : serveur web sur la Raspberry Pi avec page de sélection d'un nouveau SSID + saisie du mot de passe

TODO : compléter le saisie sur PHP pour ajouter un nouveau réseau

TODO : supression d'un réseau du fichier wpa-roam.conf

TODO : documentation en anglais (traduction des docs existants)

### Jour 3 : 04/05

Installation du serveur web "lighttpd" et du PHP sur la Raspberry Pi.

Charger et afficher les réseaux déjà connus (dans le fichier wpa-roam.conf) et ceux disponibles sur le Wifi sur une page

### Jour 4 : 05/05

Affichage des réseaux connus et disponibles sur PHP

Sélectionner un réseau, mettre son password et enregistrer le fichier wpa-roam.conf via PHP

### Jour 5 : 06/05

Supression de réseau dans le fichier wpa-roam.conf via PHP

Traduction de la documentation en anglais

### Jour 6 : 07/05

Modification du fonctionnement de la suppression et de l'ajout de réseaux (SSID)

Continuation de la traduction en anglais

## SEMAINE 3

TODO : écriture de nouveaux modules Python (répertoire /mod) et envoyer des messages depuis des tags NFC à ces modules :

TODO : module n°1 = mettre à jour la liste des réseaux connus par recherche wifi (ce qui permettra ensuite d'en sélectionner un via interface php)

TODO : module n°2 = tweeter l'ouverture de SoFAB / la fermeture de SoFAB / envoyer un tweet "fermeture pour X minutes" avec deux tags (le second permet de définir le nombre de minutes)

TODO : amélioration du module n°2 = faire la somme de N tags pour définir un nombre de minutes précis (48 = 30 + 10 + 5 + 2 + 1)

### Jour 7 : 11/05

Reprendre l'ajout et la suppression de réseaux (SSID)
* Sur PHP, récupérer la liste des SSID depuis un fichier intermédiaire, et l'afficher
* Action + saisie via PHP, mettre à jour la liste, la stocker dans un autre fichier (') et l'afficher
* NFC tag : lancer le programme network-update (module) en fonction des configurations faites, et stocker la nouvelle liste dans le fichier wpa-roam.conf

### Jour 8 : 12/05

Etudes des codes sources et les fonctionnements du NFC via Python

### Jour 9 : 13/05

TODO : pas de chemin en dur!

Presentation en détail du déroulement du fonctionnemet NFC en ce qui concerne les codes sources

Un nouveau module permettant de publier un tweet avec photo sur Twitter

### Jour 10 : 15/05

Travail sur la notification "InsecurePlatformWarning"

Introduction de deux nouveaux modules dans le service Twitter pour annoncer l'ouverture et la fermeture du SoFAB et durée d'une fermeture temporaire

## SEMAINE 4

TODO : module n°3 = passer un tag "dépense" puis un tag "adhérent n°XXX" (numéro unique) puis un tag "laser" ou "imp3D" puis une somme de minutes

TODO : module n°4 = passer un tag "achat" puis un tag "adhérent n°XXX" puis un nombre d'écrous

TODO : affichage sur l'écran de chaque tag + l'interprétation du tag (quel module le traite) + état du processus (lecture, validation, attente)

TODO : side project - documentation d'un nouveau Cube sur makake (http://www.makake.co/)

TODO : travail sur la documentation de l'utilisation de Git

### Jour 11 : 18/05

Continuation du travail et améliorations des modules permettant de publier des tweets (ouverture et fermeture du SoFAB)

Plusieurs tags pour un fonctionnement!

### Jour 12 : 19/05

Introductions des nouveaux modules.
   * toshare.py = différentiation de plateforme (ex : twitter, facebook) pour les publications de contenu à partager
   * timedur.py = un compteur défini par des tags ayant des valuers différentes

Completion du Module n°2 (intermédiare...)

### Jour 13 : 20/05

## SEMAINE 5

TODO : voir http://linuxfr.org/news/rpi-monitor-un-outil-de-supervision-a-personnaliser

## SEMAINE 6

## SEMAINE 7

## Semaine 8

## Semaine 9
