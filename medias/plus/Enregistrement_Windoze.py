# Créé par Matthieu, le 30/06/2022 en Python 3.7

import json
import pygame
from pygame import *

print("Chargement du système de sauvegarde et d'Highscore...")

def lecture_highscore():
    text_file = open("medias/plus/sauvegarde.txt", "r") #Ouvre le document en lecture
    content = json.load(text_file) #Charge en json le contenu du document
    text_file.close() #Referme le document
    return content

def enregistrement_score(score,nom):
    #Enregistre le score en parcourant le Highscore et en déplaçant les listes.
    #Puis remplace l'ancien score par le nouveau.

    #Score -> int (le score)
    #Nom -> str (le nom du joueur)
    highscore=lecture_highscore()

    for selection_score in range(len(highscore)):
        if score>highscore[selection_score][1]:
            for sous_selection in range(len(highscore)-1,selection_score,-1):
                highscore[sous_selection]=highscore[sous_selection-1].copy()
            highscore[selection_score][1]=score
            highscore[selection_score][0]=nom
            break


    text_file = open("medias/plus/sauvegarde.txt", "w")
    json.dump(highscore,text_file)

    text_file.close()

