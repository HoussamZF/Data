import json
from collections import defaultdict
import numpy as np

#fichiers .JSON
with open('data/Clubs.json', 'r', encoding='utf-8') as jsonfile:
    clubs = json.load(jsonfile)
with open('data/Joueurs.json', 'r', encoding='utf-8') as jsonfile:
    joueurs = json.load(jsonfile)


#ENREGISTREMENT DE LA LISTE DES CLUBS & JOUEURS DANS DES VARIBLES DICTIONNAIRE
dictCLUBS = defaultdict(dict)
for club in clubs:
    dictCLUBS[club["nomClub"]].update(club)

dictPLAYERS = defaultdict(dict)
for joueur in joueurs:
    nomJoueur = joueur["dataJoueur"]["nom"]
    if(nomJoueur != "-"):
        dictPLAYERS[nomJoueur].update(joueur["dataJoueur"])


#lES METHODES UTILISEES QUI SONT NECESSAIRES AU TRAITEMENT DES DONNEES POUR LA BONNE GENERATION DES MAPS
#1.RECUPERATION DES COORDONNES GPS D'UN (OU 2) CLUB, ICI CE SONT LES COORDONNEES DU STADE QUI EST UTILISE
#CE CHOIX POSERAI UN PROBLEME SI 2 CLUBS PARTAGENT LE MEME STADE, ET QU'ILS ONT EUDES TRASACTIONS DURANT
#CE MARCHE, QUELLE ALTERNATIVE ?
def getCoordonnees(acheteur, vendeur=0):
    #si on va récupérer les x,y du vendeur
    if(vendeur != 0):
        if(clubInexistant(vendeur)):
            return [39, 35]
        #cas a => b
        if(vendeur != "Sans club"):
            xy = listerXY(dictCLUBS[vendeur].get("localisation"))
            xy.reverse()
            return xy
        #transfert libre
        else:
            xy = listerXY(dictCLUBS[acheteur].get("localisation"))
            xy.reverse()
            return xy
    #si on va récupérer les x,y de l'acheteur
    else:
        #sans club (quitte le club) ou club qui n'est pas dans la BD
        if(acheteur == "Sans Club" or clubInexistant(acheteur) == True):
            return [39, 35]
        #club dans la BD
        else:
            xy = listerXY((dictCLUBS[acheteur].get("localisation")))
            xy.reverse()
            return xy

#2. RETOURNE LES COORDONNES X,Y SOUS LA FORME D'UNE LISTE
def listerXY(strXY):
    lat, lng = map(float, strXY.strip('[]').split(','))
    return [lat, lng]

#3. RECUPERE LE LOGO D'UN CLUB, CETTE FONCTION EST UTILE DANS LE CAS OU
#LE CLUB NE FAIT PAS PARTIE DES 5 GRANDS CHAMPIONNATS TRAITES, OU UN
#LOGO GENERIQUE (CARTE DU MONDE) EST RETOURNE
def getClubImg(acheteur, vendeur=0):
    #vendeur
    if(vendeur != 0):
        if(vendeur != "Sans club"):
            if(clubInexistant(vendeur)):
                return ".\imgs\world.png"
            return dictCLUBS[vendeur].get("photo")
        else:
            return dictCLUBS[acheteur].get("photo")
    #acheteur
    else:
        if(clubInexistant(acheteur)):
                return ".\imgs\world.png"
        return dictCLUBS[acheteur].get("photo")

#4.VERIFIE SI UN CLUB EXISTE DANS LA BD (5 GRANDS CHAMPIONNATS)
def clubInexistant(nomClub):
    if(dictCLUBS[nomClub] == {}):
        return True
    return False

#5. RECUPERE LES INFOS D'UN JOUEUR SUITE A UNE REQUETE
def recupJoueurInfos(name):
    if(dictPLAYERS[name] == {}):
        return {}
    else:
        return dictPLAYERS[name]