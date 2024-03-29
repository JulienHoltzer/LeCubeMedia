# Suivi du projet 

TAG NFC
* NONO : photo.py - prise d'une photo, publier sur Twitter
* LECTURE : open.py - ouverture et fermeture du SoFAB
* PAUSE : open.py - fermeture temporaire (pour "x" minutes) du SoFAB
* HUB : toshare.py - partage du contenu sur Twitter/Facebook/etc...
* ANDROID : hashtags.py - #Android
* NFC : hashtags.py - #NFC
* Raspberry Pi : hashtags.py - #RaspberryPi
* Achat : activite.py
* Dépense : activite.py
* User1 : adherent.py
* Tool1 : tool.py

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

### Jour 11 : 18/05

Continuation du travail et améliorations des modules permettant de publier des tweets (ouverture et fermeture du SoFAB)

Plusieurs tags pour un fonctionnement!

### Jour 12 : 19/05

Introductions des nouveaux modules.
   * toshare.py = différentiation de plateforme (ex : twitter, facebook) pour les publications de contenu à partager
   * timedur.py = un compteur défini par des tags ayant des valuers différentes

Completion du Module n°2 (intermédiare...)

### Jour 13 : 20/05

Mise à jour des configs réseaux

Etudes sur les modules suivants (sauvegarde de données "achat, dépense" dans un fichier excel)

### Jour 14 : 21/05

Un nouveau module pour ajouter des hashtags pour la publication d'une photo sur Twitter

### Jour 15 : 22/05

Des nouveaux modules pour sauvegarder des données concernant les activités faites au sein du lab (dépense/achat) dans des fichiers simples.
* activite.py
* adherent.py
* tool.py

## SEMAINE 5

TODO : affichage sur l'écran de chaque tag + l'interprétation du tag (quel module le traite) + état du processus (lecture, validation, attente)

TODO : gestion de fichier (upload/modification) sur Google Drive grace à API

TODO : side project - documentation d'un nouveau Cube sur makake (http://www.makake.co/)

TODO : travail sur la documentation de l'utilisation de Git

TODO : voir http://linuxfr.org/news/rpi-monitor-un-outil-de-supervision-a-personnaliser

### Jour 16 : 26/05

Créer un nouveau projet sur Google pour avoir des clès (Google API)

Introduction et installation de PyDrive (http://pythonhosted.org/PyDrive/) pour pouvoir mettre en ligne des fichiers sur Google Drive via Python

Ajout d'un nouveau module "updrive.py" permettant de mettre en ligne des fichiers sur Google Drive

### Jour 17 : 27/05

Introduction de 2 nouveaux tags pour lancer le module "updrive.py" et des petites adaptations pour son fonctionnement

Amélioration du module en y ajoutant un option de mettre en ligne des photos à partir d'un répertoire défini

Etudes/découvert de la notion de Comet pour ce qui concerne l'IHM

### Jour 18 : 28/05

Tutoriels sur le Comet et introduction à Cometd 

Installation de CherryPy qui semble adapté au projet, introduction à ses fonctionnements

### Jour 19 : 29/05

Continuation du travail sur CherryPy

## SEMAINE 6

### Jour 20 : 01/06

Quelques petites mises à jour des modules existants (timedur.py, photo.py)

Ajout des nouveaux tags pour le compteur (timedur.py) et les activités (activite.py)

### Jour 21 : 02/06

Amélioration du module updrive.py - possibilité de définir le répertoire dans lequel on veut uploader une photo en introduisant un tag NFC correspondant.

Ajout du module reset.py pour remettre à zéro les données temporaires

Des petites adaptations (toshare.py)

### Jour 22 : 03/06

Configuration audio pour le microphone sur le Raspberry Pi, non-réussi

Documentation des fonctionnements du Cube (ResumeFonc.odt)

### Jour 23 : 04/06

Continuation de la documentation

Petite adaptation du module updrive (upload vers le bon repertoire)

### Jour 24 : 05/06

Configuration audio et microphone pour l'enregistrement audio à utiliser avec le SpeechRecognition

## SEMAINE 7

### Jour 25 : 08/06

Installation du SpeechRecognition et du PyAudio pour la réconnaissance vocale

Tests de module pour ce fonctionnement

### Jour 26 : 09/06

Tests du SpeechRecognition réussis

### Jour 27 : 10/06

### Jour 28 : 11/06

### Jour 29 : 12/06

## SEMAINE 8

### Jour 30 : 15/06

Rédaction du rapport du projet

### Jour 31 : 16/06

### Jour 32 : 17/06

### Jour 33 : 18/06

### Jour 34 : 19/06

## SEMAINE 9

### Jour 35 : 22/06




