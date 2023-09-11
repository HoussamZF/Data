import folium
import json
from collections import defaultdict
import dtmaplib as maplib

with open('data/Transferts.json', 'r', encoding='utf-8') as jsonfile:
    transferts = json.load(jsonfile)

dictTRANSFERTS = defaultdict(dict)


#METHODES

#1. PERMET DE SUPPRIMER LA REDONDANCE DUE A L'ABBREVIATION DES NOMS DE CLUBS PAR LE SITE
#PAR EXEMPLE: UN TRANSFERT QUI CONCERNE BORUSSIA DORTMUND POURRAIT APPARAITRE UNE 2EME FOIS
#AVEC COMME NOM DE CLUB (ACHETUER OU VENDEUR) = Bor. DORTMUND
def redondanceCleaner():
    for t in transferts:
        if(t["nomJoueur"] in dictTRANSFERTS):
            if(t["nomClubAcheteur"] > dictTRANSFERTS[t["nomJoueur"]]["nomClubAcheteur"] or t["nomClubVendeur"] > dictTRANSFERTS[t["nomJoueur"]]["nomClubVendeur"]):
                dictTRANSFERTS[t["nomJoueur"]].update(t)
        else:
            dictTRANSFERTS[t["nomJoueur"]].update(t)
    return dictTRANSFERTS

#2. TRAITEMENT DE LA DONNEE PRIX, QUI VIENT SOUS FORME DE STRING CE QUI NE PERMET PAS
#DE FAIRE UNE VRAIE COMPARAISON AFIN DE DETERMINER LA TAILLE DE LA FLECHE, ICI L'IDEE
#C'EST DE DONNER UNE CERTAINE TAILLE A LA FLECHE POUR ARIVER A DETERMINER SON POIDS PAR
#RAPPORTS AUX AUTRES TRANSACTIONS PREALISES PAR LE CLUB
def prixConverter():
    for player in dictTRANSFERTS:
        prixTransfert = dictTRANSFERTS[player]["prix"]
        
        #Ventes/Achats
        if(prixTransfert not in ["Transfert libre", "-", "?", "Prêt"] and not prixTransfert.startswith("Montant du prêt")):
            dictTRANSFERTS[player].update({"prixFloat" : extractPrix(prixTransfert)})
        
        if(prixTransfert == "Transfert libre" or prixTransfert == "-" or prixTransfert == "?"):
            dictTRANSFERTS[player].update({"prixFloat" : 0})

        
        #Prêts
        if(prixTransfert == "Prêt"):
            #ajouter une clé pret qui nous permet de déterminer le type d'affichage
            dictTRANSFERTS[player].update({"prixFloat" : 0, "pret" : 1})
        
        if(prixTransfert.startswith("Montant du prêt")):
            justeLePrix = prixTransfert.split("Montant du prêt")[1]
            #ajouter une clé pret qui nous permet de déterminer le type d'affichage
            dictTRANSFERTS[player].update({"prixFloat" : extractPrix(justeLePrix), "pret" : 1})
    return dictTRANSFERTS


#3. EXTRAIRE LE PRIX D'UNE TRANSACTION ET LE RETOURNER SOUS FORME D'UN INTEGER
def extractPrix(prixStr):
    #cas des millions
    if(len(prixStr.split(" mio. €")) == 2):
        if(not prixStr.split(" mio. €")[0].startswith("Montant du prêt")):
            prixComparable = float(prixStr.split(" mio. €")[0].replace(',','.')) * 1000

            #ici afin d'optimiser le tri, on multiplie par 1000 au lieu de 10^6
            #la multiplication par million consomme beaucoup de ressources
            #et en effer la multiplication par 1000 nous assure toujours que
            #le prix sera plus grand que le cas des milliers
            #exemple: 1,00 m * 1000 > 999 (k $)

    #cas des milliers
    if(len(prixStr.split(" K €")) == 2):
        if(not prixStr.split(" K €")[0].startswith("Montant du prêt")):
            prixComparable = float(prixStr.split(" K €")[0].replace(',','.'))
    
    return prixComparable


#4. RETOURNE LES INFOS EN HTML  D'UN JOUEUR POUR L'AFFICHER DANS LA BULLE DU TRANSFERT
def joueurToHtml(dictPlayer):
    infos = maplib.recupJoueurInfos(dictPlayer["nomJoueur"])
    txt = '<div style="font-family : arial">'

    if(infos != {}): #SI C'EST LE PREMIER JOUEUR DANS LA LISTE (ENTRE 2 CLUBS A & B)
        txt += '<img src="'+infos["photo"]+'" height="55" width="50"><br>'
        txt += infos["age"] + ' | '
        txt += '<a href="#" style="text-decoration : none">' + infos["nom"] + '</a> | '
        txt += infos["valeurMarchande"] + '<br>'
        txt += infos["position"] + '<br>'
        txt += infos["nationalite"] + '<br>'
        txt += '> ' + dictPlayer["nomClubAcheteur"]+'<br>'
        txt += '<b>' + dictPlayer["prix"]+'</b><br>'
        txt += '<b>Fin de contrat : </b>' + infos["finContrat"]
        
        return txt

    #SI C'EST UN NIEME JOUEUR (PAS LE PREMIER)
    txt += '<a href="#" style="text-decoration : none">'+dictPlayer["nomJoueur"]+'</a>'+'<br>'
    txt += '> ' + dictPlayer["nomClubAcheteur"]+'<br>'
    txt += '<b>' + dictPlayer["prix"]+'</b><br>'

    txt += '</div>'
    return txt

#5. RETOURNE LES DEPENSES(-) & BENEFICES(+) D'UN CLUB
def dep_benef_clubs(transferts, nomClub):
    dep = 0
    benef = 0
    for player in transferts:
        if(transferts[player]["nomClubAcheteur"] == nomClub or transferts[player]["nomClubVendeur"] == nomClub):

            if(transferts[player]["nomClubAcheteur"] == nomClub):
                dep += transferts[player]["prixFloat"]

            else:
                benef += transferts[player]["prixFloat"] 

    
    return [dep, benef]

def allTransfertsAetV(ach, vend):
    text = ''
    for joueur in dictTRANSFERTS:
        if((dictTRANSFERTS[joueur]["nomClubAcheteur"] == ach) and (dictTRANSFERTS[joueur]["nomClubVendeur"] == vend)):
           text += joueurToHtml(dictTRANSFERTS[joueur])
           text += '<hr>'
        if((dictTRANSFERTS[joueur]["nomClubAcheteur"] == vend) and (dictTRANSFERTS[joueur]["nomClubVendeur"] == ach)):
           text += joueurToHtml(dictTRANSFERTS[joueur])
           text += '<hr>'
    return text

#Initialisation des maps
def initDefaultMap() :
    start_coords = (51.484206,-2.202812)
    folium_map = folium.Map(location=start_coords,zoom_start=4)
    folium_map.save('templates/transferts.html')
    return 0


def init_map_club(requestedClub) :
    #Créer une carte par club
    club_coords = maplib.getCoordonnees(requestedClub)
    mp = folium.Map(location=club_coords,zoom_start=4.5)

    #Preparer les transferts
    redondanceCleaner() #supprimer les redondances liées aux noms abrégés des clubs
    prixConverter() #ajouter une donnée prix de type float afin de comparer les differentes transactions (str->float avec toutes  les       
    #exceptions dérrière)
    
    #Récuperer les dépenses & le bénefice du club
    depBen = dep_benef_clubs(dictTRANSFERTS, requestedClub)
    sommeDepBen = depBen[0] + depBen[1] #permettra de déterminer la taille d'une flèche

    for player in dictTRANSFERTS:
        
        if(dictTRANSFERTS[player]["nomClubAcheteur"] == requestedClub or dictTRANSFERTS[player]["nomClubVendeur"] == requestedClub):
        
            acheteurXY = maplib.getCoordonnees(dictTRANSFERTS[player]["nomClubAcheteur"])
            vendeurXY = maplib.getCoordonnees(dictTRANSFERTS[player]["nomClubAcheteur"], dictTRANSFERTS[player]["nomClubVendeur"])
            acheteurImg = maplib.getClubImg(dictTRANSFERTS[player]["nomClubAcheteur"])
            vendeurImg = maplib.getClubImg(dictTRANSFERTS[player]["nomClubAcheteur"], dictTRANSFERTS[player]["nomClubVendeur"])
            
            #Tous les transferts entre ClubA et B
            text = allTransfertsAetV(dictTRANSFERTS[player]["nomClubAcheteur"], dictTRANSFERTS[player]["nomClubVendeur"])

            points = [vendeurXY, acheteurXY]

            #Vendeur
            logo = folium.features.CustomIcon(vendeurImg, icon_size=(18.9,23.1))
            folium.Marker(location=vendeurXY, tooltip=dictTRANSFERTS[player]["nomClubVendeur"], icon=logo).add_to(mp)

            #Flèche
            iframe = folium.IFrame(text)
            popup = folium.Popup(iframe, min_width = 310,max_width = 310)

            #Si un prêt -> en pointillé
            dashed = '0'
            if("pret" in dictTRANSFERTS[player]):
                dashed = '10'

            #Achat en vert, vente en rouge
            if(dictTRANSFERTS[player]["nomClubAcheteur"] == requestedClub):
                lineColor = "green"
            else:
                lineColor = "crimson"

            #Taille de la flèche par rapport à la somme depenses+benf (choix personnel d'affichage)
            tailleFleche = (dictTRANSFERTS[player]["prixFloat"]*8) / sommeDepBen

            #Ajout de la flèche
            folium.PolyLine(points, weight=2 + tailleFleche, color=lineColor, popup=popup, dash_array=dashed).add_to(mp)

            #Acheteur
            logo = folium.features.CustomIcon(acheteurImg, icon_size=(18.9,23.1))
            folium.Marker(location=acheteurXY, tooltip=dictTRANSFERTS[player]["nomClubAcheteur"], icon=logo).add_to(mp)
            
            #mp
            mp.save(outfile="templates/transferts.html")
    return mp