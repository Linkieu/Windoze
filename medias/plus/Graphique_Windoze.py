# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 14:40:45 2022

@author: Matthieu
"""

import pygame
from pygame import *

pygame.init()
print("Chargement des graphiques...")
##############################################################################

#Chargement des différents blocs
bloc_horloge = pygame.image.load("medias/img/blocs/bloc_horloge.png")
bloc_install = pygame.image.load("medias/img/blocs/bloc_install.png")
bloc_windows = pygame.image.load("medias/img/blocs/bloc_windows.png")
bloc_msdos = pygame.image.load("medias/img/blocs/bloc_msdos.png")
bloc_paint = pygame.image.load("medias/img/blocs/bloc_paint.png")
bloc_terre = pygame.image.load("medias/img/blocs/bloc_terre.png")
bloc_missingno = pygame.image.load("medias/img/blocs/bloc_missingno.png")

DEFAULT_IMAGE_SIZE=(40,40)
bloc_horloge = pygame.transform.scale(bloc_horloge, DEFAULT_IMAGE_SIZE)
bloc_install = pygame.transform.scale(bloc_install, DEFAULT_IMAGE_SIZE)
bloc_windows = pygame.transform.scale(bloc_windows, DEFAULT_IMAGE_SIZE)
bloc_msdos = pygame.transform.scale(bloc_msdos, DEFAULT_IMAGE_SIZE)
bloc_paint = pygame.transform.scale(bloc_paint, DEFAULT_IMAGE_SIZE)
bloc_terre = pygame.transform.scale(bloc_terre, DEFAULT_IMAGE_SIZE)
bloc_missingno = pygame.transform.scale(bloc_missingno, DEFAULT_IMAGE_SIZE)



##############################################################################
#PREPARATION DU JEU
##############################################################################
taille_x_fenetre=650 #Par défaut: 650
taille_y_fenetre=500


fenetre = pygame.display.set_mode((taille_x_fenetre,taille_y_fenetre)) #Génère une fenêtre vide
pygame.display.set_caption('Windoze')
pygame.display.set_icon(pygame.image.load('medias/img/icon/windoze.png'))

#########################
# CREATION FOND FENETRE #
#########################
fond = pygame.image.load("medias/img/fond/Velvet.jpg").convert() #Importe l'image de fond
pos_x_img_fond,pos_y_img_fond=0,0 #Initialisation de la mosaïque d'images
fond_mosaique=[] #Initialisation de la mosaïque d'images

 #Tant que la fenêtre n'est pas rempli, on rajoute des images à la mosaïque.
while pos_y_img_fond<taille_y_fenetre: #En axe y
    while pos_x_img_fond<taille_x_fenetre: #En axe x
        fond_mosaique.append((fond,(pos_x_img_fond,pos_y_img_fond))) #Ajout de l'image
        pos_x_img_fond+=203
    pos_y_img_fond+=170
    pos_x_img_fond=0





#########################
# CREATION EMPLACEMENTS #
#########################
imgfen_angle_bas_droit = pygame.image.load("medias/img/fenetre/angle_bas_droit.png")
imgfen_angle_bas_gauche = pygame.image.load("medias/img/fenetre/angle_bas_gauche.png")
imgfen_angle_haut_droit = pygame.image.load("medias/img/fenetre/angle_haut_droit.png")
imgfen_angle_haut_gauche = pygame.image.load("medias/img/fenetre/angle_haut_gauche.png")
imgfen_bas = pygame.image.load("medias/img/fenetre/bas.png")
imgfen_droit = pygame.image.load("medias/img/fenetre/droite.png")
imgfen_gauche = pygame.image.load("medias/img/fenetre/gauche.png")
imgfen_haut = pygame.image.load("medias/img/fenetre/haut.png")
imgfen_v2_angle_haut_gauche = pygame.image.load("medias/img/fenetre/v2_angle_haut_gauche.png")
imgfen_v2_angle_haut_droit = pygame.image.load("medias/img/fenetre/v2_angle_haut_droit.png")
imgfen_fond = pygame.image.load("medias/img/fenetre/fond.png")

pygame.font.init()
font = pygame.font.Font('medias/font/windows_command_prompt.ttf', 20) #Paramètre la police

# EMPLACEMENT FOND JEU
#######################
pos_sprite_fond_jeu_x=taille_x_fenetre/3.5
pos_sprite_fond_jeu_y=taille_y_fenetre/20
emplacement_fond_jeu=[(imgfen_angle_haut_gauche,(pos_sprite_fond_jeu_x,pos_sprite_fond_jeu_y)),(imgfen_angle_haut_droit,(pos_sprite_fond_jeu_x+23*9-5,pos_sprite_fond_jeu_y))]

for sprite_haut in range(1,9):
    sprite_haut=pos_sprite_fond_jeu_x+23*sprite_haut
    emplacement_fond_jeu.append((imgfen_haut,(sprite_haut,pos_sprite_fond_jeu_y)))
    emplacement_fond_jeu.append((imgfen_bas,(sprite_haut,pos_sprite_fond_jeu_y+444))) #+437 à l'origine

for sprite_gauche in range(1,20):
    sprite_gauche=pos_sprite_fond_jeu_y+23*sprite_gauche
    emplacement_fond_jeu.append((imgfen_gauche,(pos_sprite_fond_jeu_x,sprite_gauche)))
    emplacement_fond_jeu.append((imgfen_droit,(pos_sprite_fond_jeu_x+23*10-5,sprite_gauche)))



emplacement_fond_jeu.append((imgfen_angle_bas_gauche,(pos_sprite_fond_jeu_x,pos_sprite_fond_jeu_y+444)))
emplacement_fond_jeu.append((imgfen_bas,(pos_sprite_fond_jeu_x+23*9,pos_sprite_fond_jeu_y+444)))
emplacement_fond_jeu.append((imgfen_angle_bas_droit,(pos_sprite_fond_jeu_x+23*10-5,pos_sprite_fond_jeu_y+444)))

def affiche_fd_jeu():
    """
    Assemble les tiles pour former la fenêtre "Windoze".
    Et rajoute la mention "Windoze" par dessus.
    """

    #pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(taille_x_fenetre/3-30, taille_y_fenetre/20+23, 23*11-6, 23*19+5))

    fenetre.blits(emplacement_fond_jeu) #Affiche les tiles

    img = font.render('Windoze', True, (255,255,255)) #Paramètre le texte
    fenetre.blit(img, (taille_x_fenetre/2-60, taille_y_fenetre/20+5)) #Affiche le texte


    return


# EMPLACEMENT SUIVANT
#######################

pos_x_suivant=pos_sprite_fond_jeu_x-137
pos_y_suivant=pos_sprite_fond_jeu_y+20
emplacement_suivant=[]
emplacement_suivant=[(imgfen_v2_angle_haut_gauche,(pos_x_suivant,pos_y_suivant))]
emplacement_suivant.append((imgfen_haut,(pos_x_suivant+23,pos_y_suivant)))
emplacement_suivant.append((imgfen_haut,(pos_x_suivant+23*2,pos_y_suivant)))
emplacement_suivant.append((imgfen_v2_angle_haut_droit,(pos_x_suivant+23*3,pos_y_suivant)))

for sprite in range(1,6):
    emplacement_suivant.append((imgfen_gauche,(pos_x_suivant,pos_y_suivant+23*sprite)))
    emplacement_suivant.append((imgfen_droit,(pos_x_suivant+23*3,pos_y_suivant+23*sprite)))

emplacement_suivant.append((imgfen_angle_bas_gauche,(pos_x_suivant,pos_y_suivant+23*6)))
emplacement_suivant.append((imgfen_bas,(pos_x_suivant+23,pos_y_suivant+23*6)))
emplacement_suivant.append((imgfen_bas,(pos_x_suivant+23*2,pos_y_suivant+23*6)))
emplacement_suivant.append((imgfen_angle_bas_droit,(pos_x_suivant+23*3,pos_y_suivant+23*6)))

def affiche_suivant(blocs_suivants):

    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(pos_x_suivant, pos_y_suivant, 23*4, 23*7))
    fenetre.blits(emplacement_suivant) #Affiche les tiles
    img = font.render('Suivant', True, (255,255,255)) #Paramètre le texte
    fenetre.blit(img, (pos_x_suivant+15, pos_y_suivant+5)) #Affiche le texte

    position=0
    for bloc in blocs_suivants[0]:
        if bloc==1:
            affiche_bloc=[(bloc_horloge,(pos_x_suivant+25,pos_y_suivant+30+40*position))]
        elif bloc==2:
            affiche_bloc=[(bloc_install,(pos_x_suivant+25,pos_y_suivant+30+40*position))]
        elif bloc==3:
            affiche_bloc=[(bloc_windows,(pos_x_suivant+25,pos_y_suivant+30+40*position))]
        elif bloc==4:
            affiche_bloc=[(bloc_msdos,(pos_x_suivant+25,pos_y_suivant+30+40*position))]
        elif bloc==5:
            affiche_bloc=[(bloc_paint,(pos_x_suivant+25,pos_y_suivant+30+40*position))]
        elif bloc==6:
            affiche_bloc=[(bloc_terre,(pos_x_suivant+25,pos_y_suivant+30+40*position))]
        else:
            affiche_bloc=[(bloc_terre,(pos_x_suivant+25,pos_y_suivant+30+40*position))]
        fenetre.blits(affiche_bloc)
        position+=1

# EMPLACEMENT CONTROLES
#######################
pos_x_controles=pos_sprite_fond_jeu_x-160
pos_y_controles=pos_sprite_fond_jeu_y+200
emplacement_controles=[(imgfen_angle_haut_gauche,(pos_x_controles,pos_y_controles))]
emplacement_controles.append((imgfen_angle_haut_droit,(pos_x_controles+23*4,pos_y_controles)))
for sprite in range(1,4): #Haut et bas
    emplacement_controles.append((imgfen_haut,(pos_x_controles+23*sprite,pos_y_controles)))
    emplacement_controles.append((imgfen_bas,(pos_x_controles+23*sprite,pos_y_controles+23*7)))
for sprite in range(1,7): #Gauche et droit
    emplacement_controles.append((imgfen_gauche,(pos_x_controles,pos_y_controles+23*sprite)))
    emplacement_controles.append((imgfen_droit,(pos_x_controles+23*5,pos_y_controles+23*sprite)))
emplacement_controles.append((imgfen_angle_bas_gauche,(pos_x_controles,pos_y_controles+23*7)))
emplacement_controles.append((imgfen_bas,(pos_x_controles+23*4,pos_y_controles+23*7)))
emplacement_controles.append((imgfen_angle_bas_droit,(pos_x_controles+23*5,pos_y_controles+23*7)))


def affiche_controles():
    textes=["Gauche = <-","Droite = ->","Descendre = Bas","Rotation = Espace","Lâcher = Haut","","Pause = P","Sauvegarder = S", "Quitter = Echap"]

    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(pos_x_controles, pos_y_controles, 23*6, 23*8))
    fenetre.blits(emplacement_controles) #Affiche les tiles
    img = font.render('Touches', True, (255,255,255)) #Paramètre le texte
    fenetre.blit(img, (pos_x_controles+28, pos_y_controles+5)) #Affiche le texte

    font_txt = pygame.font.Font('medias/font/windows_command_prompt.ttf', 17) #Paramètre la police
    for id_texte in range(len(textes)):
        txt = font_txt.render(textes[id_texte], True, (0,0,0)) #Paramètre le texte
        fenetre.blit(txt, (pos_x_controles+15, pos_y_controles+35+15*id_texte)) #Affiche le texte

# EMPLACEMENT SCORE
#######################
pos_x_score=pos_sprite_fond_jeu_x+285
pos_y_score=pos_sprite_fond_jeu_y+20
emplacement_score=[(imgfen_angle_haut_gauche,(pos_x_score,pos_y_score))]
emplacement_score.append((imgfen_angle_haut_droit,(pos_x_score+23*4,pos_y_score)))
for sprite in range(1,4): #Haut et bas
    emplacement_score.append((imgfen_haut,(pos_x_score+23*sprite,pos_y_score)))
    emplacement_score.append((imgfen_bas,(pos_x_score+23*sprite,pos_y_score+23*2)))

emplacement_score.append((imgfen_gauche,(pos_x_score,pos_y_score+23)))
emplacement_score.append((imgfen_droit,(pos_x_score+23*5,pos_y_score+23)))
emplacement_score.append((imgfen_angle_bas_gauche,(pos_x_score,pos_y_score+23*2)))
emplacement_score.append((imgfen_bas,(pos_x_score+23*4,pos_y_score+23*2)))
emplacement_score.append((imgfen_angle_bas_droit,(pos_x_score+23*5,pos_y_score+23*2)))

def affiche_score(score):
    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(pos_x_score, pos_y_score, 23*6, 23*3))
    fenetre.blits(emplacement_score) #Affiche les tiles
    img = font.render('Score', True, (255,255,255)) #Paramètre le texte
    fenetre.blit(img, (pos_x_score+37, pos_y_score+5)) #Affiche le texte

    score_affichage = font.render(str(score), True, (0,0,0)) #Paramètre le texte
    fenetre.blit(score_affichage, (pos_x_score+10, pos_y_score+35)) #Affiche le texte

# EMPLACEMENT NIVEAU
#######################
pos_x_niveau=pos_sprite_fond_jeu_x+285
pos_y_niveau=pos_sprite_fond_jeu_y+110
emplacement_niveau=[(imgfen_angle_haut_gauche,(pos_x_niveau,pos_y_niveau))]
emplacement_niveau.append((imgfen_angle_haut_droit,(pos_x_niveau+23*4,pos_y_niveau)))
for sprite in range(1,4): #Haut et bas
    emplacement_niveau.append((imgfen_haut,(pos_x_niveau+23*sprite,pos_y_niveau)))
    emplacement_niveau.append((imgfen_bas,(pos_x_niveau+23*sprite,pos_y_niveau+23*2)))
emplacement_niveau.append((imgfen_gauche,(pos_x_niveau,pos_y_niveau+23)))
emplacement_niveau.append((imgfen_droit,(pos_x_niveau+23*5,pos_y_niveau+23)))
emplacement_niveau.append((imgfen_angle_bas_gauche,(pos_x_niveau,pos_y_niveau+23*2)))
emplacement_niveau.append((imgfen_bas,(pos_x_niveau+23*4,pos_y_niveau+23*2)))
emplacement_niveau.append((imgfen_angle_bas_droit,(pos_x_niveau+23*5,pos_y_niveau+23*2)))

def affiche_niveau(niveau):
    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(pos_x_niveau, pos_y_niveau, 23*6, 23*3))
    fenetre.blits(emplacement_niveau) #Affiche les tiles
    img = font.render('Niveau', True, (255,255,255)) #Paramètre le texte
    fenetre.blit(img, (pos_x_niveau+32, pos_y_niveau+5)) #Affiche le texte

    niveau_affichage = font.render(str(niveau), True, (0,0,0)) #Paramètre le texte
    fenetre.blit(niveau_affichage, (pos_x_score+10, pos_y_score+125)) #Affiche le texte

# EMPLACEMENT HIGH SCORE
#######################
pos_x_highscore=pos_sprite_fond_jeu_x+265
pos_y_highscore=pos_sprite_fond_jeu_y+200
emplacement_highscore=[(imgfen_angle_haut_gauche,(pos_x_highscore,pos_y_highscore))]
emplacement_highscore.append((imgfen_angle_haut_droit,(pos_x_highscore+23*6,pos_y_highscore)))

for sprite in range(1,6): #Haut et bas
    emplacement_highscore.append((imgfen_haut,(pos_x_highscore+23*sprite,pos_y_highscore)))
    emplacement_highscore.append((imgfen_bas,(pos_x_highscore+23*sprite,pos_y_highscore+23*10)))
for sprite in range(1,10): #Gauche et droit
    emplacement_highscore.append((imgfen_gauche,(pos_x_highscore,pos_y_highscore+23*sprite)))
    emplacement_highscore.append((imgfen_droit,(pos_x_highscore+23*7,pos_y_highscore+23*sprite)))
emplacement_highscore.append((imgfen_angle_bas_gauche,(pos_x_highscore,pos_y_highscore+23*10)))
emplacement_highscore.append((imgfen_bas,(pos_x_highscore+23*6,pos_y_highscore+23*10)))
emplacement_highscore.append((imgfen_angle_bas_droit,(pos_x_highscore+23*7,pos_y_highscore+23*10)))

def affiche_highscore(highscore):
    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(pos_x_highscore, pos_y_highscore, 23*8, 23*11))
    fenetre.blits(emplacement_highscore) #Affiche les tiles
    img = font.render('High Score', True, (255,255,255)) #Paramètre le texte
    fenetre.blit(img, (pos_x_highscore+40, pos_y_highscore+5)) #Affiche le texte

    font_txt = pygame.font.Font('medias/font/windows_command_prompt.ttf', 17) #Paramètre la police
    numero_ligne=-1
    for ligne_highscore in highscore:
        numero_ligne+=1

        #Affiche le nom du joueur
        txt = font_txt.render(str(ligne_highscore[0]), True, (0,0,0)) #Paramètre le texte
        fenetre.blit(txt, (pos_x_highscore+10, pos_y_highscore+30+15*numero_ligne)) #Affiche le texte

        #Affiche son score
        txt = font_txt.render(str(ligne_highscore[1]), True, (0,0,0)) #Paramètre le texte

        #https://stackoverflow.com/questions/34013119/pygame-text-anchor-right
        txt_rect = txt.get_rect()
        txt_rect.right = pos_x_highscore+175 # align to right to 150px
        txt_rect.top = pos_y_highscore+30+15*numero_ligne
        fenetre.blit(txt, txt_rect)




#########################
# GENERATION JEU        #
#########################

def affichage_grille_de_jeu(grille):
    for i in range(2,len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j]==1:
                fenetre.blit(bloc_horloge,(j*40+taille_x_fenetre/3.5+4,(i-2)*40+taille_y_fenetre/20+23))
            elif grille[i][j]==2:
                fenetre.blit(bloc_install,(j*40+taille_x_fenetre/3.5+4,(i-2)*40+taille_y_fenetre/20+23))
            elif grille[i][j]==3:
                fenetre.blit(bloc_windows,(j*40+taille_x_fenetre/3.5+4,(i-2)*40+taille_y_fenetre/20+23))
            elif grille[i][j]==4:
                fenetre.blit(bloc_msdos,(j*40+taille_x_fenetre/3.5+4,(i-2)*40+taille_y_fenetre/20+23))
            elif grille[i][j]==5:
                fenetre.blit(bloc_paint,(j*40+taille_x_fenetre/3.5+4,(i-2)*40+taille_y_fenetre/20+23))
            elif grille[i][j]==6:
                fenetre.blit(bloc_terre,(j*40+taille_x_fenetre/3.5+4,(i-2)*40+taille_y_fenetre/20+23))
            '''
            elif grille[i][j]!=0:
                fenetre.blit(bloc_missingno,(j*40+taille_x_fenetre/3.5+4,(i-2)*40+taille_y_fenetre/20+23))
            '''
def affichage_blocs_mobiles(blocs_mobiles):
    """
    Entrée:
            blocs_mobiles: 2 listes en une
                Contient les blocs à afficher + les coordonnées

    On affiche l'ensemble de bloc mobile à l'écran.
    """
    pos_bloc=0
    init_bloc_x,init_bloc_y=blocs_mobiles[1][0],blocs_mobiles[1][1]
    #Les coordonnées correspondent à la grille de jeu.
    #Mais les coordonnées sont différents que ceux pour l'écran.

    #Donc on réaguste pour l'écran, en fonction de la position d'un bloc dans la
    #grille de jeu. En assignant à une nouvelle variable: bloc_?

    bloc_x=taille_x_fenetre/3.5+4+40*init_bloc_x #Position initial + position dans la grille
    for bloc in blocs_mobiles[0]:
        bloc_y=taille_y_fenetre/20+23+40*(init_bloc_y-2)+40*pos_bloc #Position inital + position dans la grille + position dans l'ensemble de blocs

        if bloc_y>=taille_y_fenetre/20: #On n'affiche uniquement ce qui rentre dans la grille de jeu
            if bloc==1:
                affiche_bloc=[(bloc_horloge,(bloc_x,bloc_y))]
            elif bloc==2:
                affiche_bloc=[(bloc_install,(bloc_x,bloc_y))]
            elif bloc==3:
                affiche_bloc=[(bloc_windows,(bloc_x,bloc_y))]
            elif bloc==4:
                affiche_bloc=[(bloc_msdos,(bloc_x,bloc_y))]
            elif bloc==5:
                affiche_bloc=[(bloc_paint,(bloc_x,bloc_y))]
            elif bloc==6:
                affiche_bloc=[(bloc_terre,(bloc_x,bloc_y))]
            else:
                return
                #affiche_bloc=[(bloc_missingno,(bloc_x,bloc_y))]
            fenetre.blits(affiche_bloc)

        pos_bloc+=1


def affichage_disparition_dun_bloc(bloc_x,bloc_y,nom_bloc):
    if bloc_y<=2:
        return
    bloc_y=taille_y_fenetre/20+23+40*(bloc_y-2)
    bloc_x=taille_x_fenetre/3.5+4+40*bloc_x

    if nom_bloc==1:
        affiche_bloc=[(bloc_horloge,(bloc_x,bloc_y))]
    elif nom_bloc==2:
        affiche_bloc=[(bloc_install,(bloc_x,bloc_y))]
    elif nom_bloc==3:
        affiche_bloc=[(bloc_windows,(bloc_x,bloc_y))]
    elif nom_bloc==4:
        affiche_bloc=[(bloc_msdos,(bloc_x,bloc_y))]
    elif nom_bloc==5:
        affiche_bloc=[(bloc_paint,(bloc_x,bloc_y))]
    elif nom_bloc==6:
        affiche_bloc=[(bloc_terre,(bloc_x,bloc_y))]
    else:
        affiche_bloc=[(bloc_missingno,(bloc_x,bloc_y))]


    fenetre.blits(affiche_bloc)
    pygame.display.flip()


def fenetre_message(bon_score,score,input_texte):

    if bon_score==True:
        fond = pygame.Surface((245,232)) #Dimension
        fond.set_alpha(220) #Transparence
        fond.fill((0,0,150)) #Couleur
        fenetre.blit(fond, (taille_x_fenetre/3-30, taille_y_fenetre/20+23*5)) #Génération du rectangle

        titre_bon_score="Félicitation !"
        texte_bon_score="Vous entrez dans le leaderboard."

        texte2_bon_score="Entrez votre nom:"

        texte_touche_bon_score="Appuyez sur Entrée pour continuer."
        texte2_touche_bon_score="Votre score sera sauvegardé."

    else:
        fond = pygame.Surface((245,232)) #Dimension
        fond.set_alpha(220)
        fond.fill((150,0,0))
        fenetre.blit(fond, (taille_x_fenetre/3-30, taille_y_fenetre/20+23*5))

        titre_bon_score="Et non..."
        texte_bon_score="Vous n'atteignez aucune place."

        texte2_bon_score="Peut-être la prochaine fois !"

        texte_touche_bon_score="Appuyez sur Entrée pour continuer."
        texte2_touche_bon_score="Vous allez quitter le jeu."


    pos_sprite_fenetre_message_x=taille_x_fenetre/3.5
    pos_sprite_fenetre_message_y=taille_y_fenetre/20+23*5
    emplacement_fenetre_message=[(imgfen_angle_haut_gauche,(pos_sprite_fenetre_message_x,pos_sprite_fenetre_message_y)),(imgfen_angle_haut_droit,(pos_sprite_fenetre_message_x+23*9-5,pos_sprite_fenetre_message_y))]

    for sprite_haut in range(1,9):
        sprite_haut=pos_sprite_fenetre_message_x+23*sprite_haut
        emplacement_fenetre_message.append((imgfen_haut,(sprite_haut,pos_sprite_fenetre_message_y)))
        emplacement_fenetre_message.append((imgfen_bas,(sprite_haut,pos_sprite_fenetre_message_y+23*9+6)))

    for sprite_gauche in range(1,15):
        sprite_gauche=pos_sprite_fenetre_message_y+23*sprite_gauche
        emplacement_fenetre_message.append((imgfen_gauche,(pos_sprite_fenetre_message_x,sprite_gauche)))
        emplacement_fenetre_message.append((imgfen_droit,(pos_sprite_fenetre_message_x+23*10-5,sprite_gauche)))
    emplacement_fenetre_message.append((imgfen_angle_bas_gauche,(pos_sprite_fenetre_message_x,pos_sprite_fenetre_message_y+23*9+6)))
    emplacement_fenetre_message.append((imgfen_bas,(pos_sprite_fenetre_message_x+23*9,pos_sprite_fenetre_message_y+23*9+6)))
    emplacement_fenetre_message.append((imgfen_angle_bas_droit,(pos_sprite_fenetre_message_x+23*10-5,pos_sprite_fenetre_message_y+23*9+6)))

    fenetre.blits(emplacement_fenetre_message)

    img = font.render('GAME OVER', True, (255,255,255)) #Paramètre le texte
    fenetre.blit(img, (pos_sprite_fenetre_message_x+75, pos_sprite_fenetre_message_y+5)) #Affiche le texte

    font_txt = pygame.font.Font('medias/font/windows_command_prompt.ttf', 17) #Paramètre la police
    img_titre = font_txt.render(titre_bon_score, True, (255,255,255))
    img_texte = font_txt.render(texte_bon_score, True, (255,255,255))
    img_texte2 = font_txt.render(texte2_bon_score, True, (255,255,255))
    fenetre.blit(img_titre, (pos_sprite_fenetre_message_x+10, pos_sprite_fenetre_message_y+25)) #Affiche le texte
    fenetre.blit(img_texte, (pos_sprite_fenetre_message_x+10, pos_sprite_fenetre_message_y+40)) #Affiche le texte
    fenetre.blit(img_texte2, (pos_sprite_fenetre_message_x+10, pos_sprite_fenetre_message_y+80)) #Affiche le texte

    img_touche = font_txt.render(texte_touche_bon_score, True, (200,200,200))
    img_touche2 = font_txt.render(texte2_touche_bon_score, True, (200,200,200))
    fenetre.blit(img_touche, (pos_sprite_fenetre_message_x+10, pos_sprite_fenetre_message_y+150)) #Affiche le texte
    fenetre.blit(img_touche2, (pos_sprite_fenetre_message_x+10, pos_sprite_fenetre_message_y+165)) #Affiche le texte

