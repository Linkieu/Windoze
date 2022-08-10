# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 16:02:29 2022

@author: Matthieu

Source: https://www.youtube.com/watch?v=oT92MVBPMAY
Jeu Original: Windoze (1984 MS-DOS)
Auteur original: Loren Blaney

Ceci est une recréation Python avec le module Pygame de ce jeu.
Linkieu, le créateur de cette version, n'est pas à l'origine de ce jeu.
Linkieu n'était pas né en 1984.

Ne republier pas ailleurs cette version !
Partager uniquement le lien promulguer par le créateur, Linkieu.


"""
##############################################################################


#import pygame
#from pygame import *
from random import *
from medias.plus.Graphique_Windoze import *
from medias.plus.Enregistrement_Windoze import *
from time import *
##############################################################################
#JEU
print("Démarrage du jeu...")
##############################################################################
clock = pygame.time.Clock()

##On génère une grille vierge.
################
grille=[]
for i in range(13):
    grille.append([0 for i in range(1,7)])

def nouveaux_blocs():
    #Génère un ensemble de 3 blocs
    blocs_suivants=[[randint(1,6) for i in range(3)],[0,-0.7]]
    return blocs_suivants

def changement_blocs():
    global blocs_suivants
    global blocs_mobiles
    global arreter_boucle_while_fait_tomber_ensemble
    blocs_mobiles=blocs_suivants
    blocs_suivants=nouveaux_blocs()
    arreter_boucle_while_fait_tomber_ensemble=False


def deplace_blocs(blocs_mobiles,direction,grille):
    """
    Entrée:
        blocs_mobiles: list
            Une liste qui contient l'ensemble de blocs + ses coords
        direction: str
            Indique la direction pour déplacer le bloc

    Instruction:
        Déplace si c'est possible, l'ensemble de bloc.
    """
    bloc_x=int(blocs_mobiles[1][0])

    if blocs_mobiles[1][1]>int(blocs_mobiles[1][1]):
        #Si on se trouve sur l'affichage dans la case suivante. Alors on
        #considère le bloc comme étant dans la case suivante.
        #Et si à sa gauche, il y a un bloc, alors on ne peut pas aller à
        #gauche.
        bloc_y=int(blocs_mobiles[1][1])+1
    else:
        bloc_y=int(blocs_mobiles[1][1])

    if direction=="BAS":
        if blocs_mobiles[1][1]<=9 and grille[bloc_y+3][bloc_x]==0:
            #Si on est au dessus de la dernière ligne de la grille et
            #si la case juste en dessous est bien vide.
            blocs_mobiles[1][1]+=1

        elif blocs_mobiles[1][1]<=9 and blocs_mobiles[1][1]>9 and grille[bloc_y+3][bloc_x]==0:
            #Si on est sur la dernière ligne, et que la case est vide, alors on
            #la place directement tout en bas.
            blocs_mobiles[1][1]=10
            test_bloc(blocs_mobiles,grille)
        elif blocs_mobiles[1][1]<=9 and grille[bloc_y+3][bloc_x]==0:
            #Si la case juste en dessous est vide.
            test_bloc(blocs_mobiles,grille)

    elif direction=="GAUCHE" and blocs_mobiles[1][0]>0:
        #Si on est pas dans la colonne tout à gauche
        if grille[bloc_y][bloc_x-1]==0 and grille[bloc_y+1][bloc_x-1]==0 and grille[bloc_y+2][bloc_x-1]==0:
            #Si aucun bloc occupe la colonne à gauche, c'est à dire à
            #l'emplacement qu'on souhaite atteindre
            blocs_mobiles[1][0]-=1

    elif direction=="DROITE" and blocs_mobiles[1][0]<=4:
        #Si on est pas dans la colonne tout à droite
        if grille[bloc_y][bloc_x+1]==0 and grille[bloc_y+1][bloc_x+1]==0 and grille[bloc_y+2][bloc_x+1]==0:
            #Si aucun bloc occupe la colonne à droite, c'est à dire à
            #l'emplacement qu'on souhaite atteindre
            blocs_mobiles[1][0]+=1

    elif direction=="HAUT":
        blocs_mobiles[1][1]-=1

def rotation_blocs(blocs_mobiles):
    """
    Entrée:
        blocs_mobiles: list
            Une liste qui contient l'ensemble de blocs + ses coords
    Instruction:
        Change de place les blocs
    """

    blocs_mobiles[0][0],blocs_mobiles[0][1],blocs_mobiles[0][2]=blocs_mobiles[0][2],blocs_mobiles[0][0],blocs_mobiles[0][1]


def ancre_blocs(blocs_mobiles,grille):
    """
    Entrée:
        blocs_mobiles: list
            Une liste qui contient l'ensemble de blocs + ses coords
            Remarque: coordonnée pour le bloc tout en haut
        grille: list
            Contient l'ensemble des blocs ancréers

    Instruction:
        Ancre définitivement le bloc dans la grille
    """
    pose_bloc_x=int(blocs_mobiles[1][0])
    pose_bloc_y=int(blocs_mobiles[1][1])

    if pose_bloc_y+2>=len(grille):
        return
    grille[pose_bloc_y][pose_bloc_x]=blocs_mobiles[0][0]   #1er bloc
    grille[pose_bloc_y+1][pose_bloc_x]=blocs_mobiles[0][1] #2e bloc
    grille[pose_bloc_y+2][pose_bloc_x]=blocs_mobiles[0][2] #3e bloc

def test_bloc(blocs_mobiles,grille):
    """
    Entrée:
        blocs_mobiles: list
            Une liste qui contient l'ensemble de blocs + ses coords
            Remarque: coordonnée pour le bloc tout en haut
        grille: list
            Contient l'ensemble des blocs ancréers

    Instruction:
        Test si le bloc s'est poser sur quelque chose.
        Si oui, ancre le bloc.
    """
    bloc_x=int(blocs_mobiles[1][0])
    bloc_y=int(blocs_mobiles[1][1])+2 #+2 correspond à la position y du bloc tout en bas

    if bloc_y>=len(grille):
        return
    if grille[bloc_y-2][bloc_x]==0 and grille[bloc_y-1][bloc_x]==0 and grille[bloc_y][bloc_x]==0:
        if bloc_y+2>=14:
            ancre_blocs(blocs_mobiles,grille)
            #elimination_blocs(blocs_mobiles,grille)
            delete_blocs()
            changement_blocs()
        elif grille[bloc_y+1][bloc_x]!=0:
            ancre_blocs(blocs_mobiles,grille)
            #elimination_blocs(blocs_mobiles,grille)
            delete_blocs()
            changement_blocs()
    else:
        #print("bonswar",grille[bloc_y-2][bloc_x],grille[bloc_y-1][bloc_x],grille[bloc_y][bloc_x])
        global jeu_en_cours
        jeu_en_cours=False



def mise_a_jour_blocs(grille):
    """
    Entrée:
        grille: list
        Grille de jeu avec les blocs ancrés

    Instruction:
        Si une case est vide sous un bloc, fait tomber le bloc.
        --> Remplace la case par un "-1", signifiant que la case est occupé par
            le bloc tombant, mais qu'il ne soit pas s'afficher. En revanche, les
            collisions avec cette case existent.
        --> Transforme le bloc ancré en un bloc spécial mobile.
            Il va ainsi animer sa descente jusqu'à sa case spécifier.


        Parcours la grille de jeu de la ligne tout en bas à tout en haut
    """
    for ligne in range(0,len(grille)-1):
        for colonne in range(len(grille[ligne])):
            if grille[ligne][colonne]!=0 and grille[ligne+1][colonne]==0:
                grille_mobile.append([[grille[ligne][colonne]],[colonne,ligne,ligne]])
                grille[ligne][colonne]=0
                grille[ligne+1][colonne]=-1

                #grille[ligne][colonne],grille[ligne-1][colonne]=grille[ligne-1][colonne],grille[ligne][colonne]


def gestion_bloc_tombant(bloc_tombant):
    if bloc_tombant[0][0]<=0:
        return
    #Format [[grille[ligne][colonne]],[colonne,ligne,ligne]]
    #Le deuxième ligne représente les coordonnées y dans la grille

    if bloc_tombant[1][1]<12 and grille[int(bloc_tombant[1][1])+1][bloc_tombant[1][0]]<=0:
        bloc_tombant[1][1]+=0.43+0.01*niveau
        affichage_blocs_mobiles(bloc_tombant)
        return bloc_tombant
    else:
        grille[int(bloc_tombant[1][1])][bloc_tombant[1][0]]=bloc_tombant[0][0]
        affichage_blocs_mobiles(bloc_tombant)
        #elimination_blocs(bloc_tombant,grille)
        delete_blocs()


def delete_blocs():
    #Horizontal

    for ligne in range(len(grille)):
        if grille[ligne][0]>0:
            valeur=grille[ligne][0]
            position_des_valeurs=[0]
        else:
            valeur=-9
            position_des_valeurs=[0]


        for colonne in range(len(grille[0])):
            if valeur==grille[ligne][colonne] and position_des_valeurs[-1]==colonne-1 and valeur>0:
                position_des_valeurs.append(colonne)
            else:
                if len(position_des_valeurs)>=3:
                    for colonne_a_suppr in position_des_valeurs:
                        anim,grille[ligne][colonne_a_suppr]=grille[ligne][colonne_a_suppr],0
                        animation_suppr_bloc(ligne,colonne_a_suppr,anim)
                valeur=grille[ligne][colonne]
                position_des_valeurs=[colonne]
        if len(position_des_valeurs)>=3:
            for colonne_a_suppr in position_des_valeurs:
                anim,grille[ligne][colonne_a_suppr]=grille[ligne][colonne_a_suppr],0
                animation_suppr_bloc(ligne,colonne_a_suppr,anim)
    #Verticale
    for colonne in range(len(grille[0])):
        if grille[0][colonne]>0:
            valeur=grille[0][colonne]
            position_des_valeurs=[0]
        else:
            valeur=-9
            position_des_valeurs=[0]

        for ligne in range(len(grille)):
            if valeur==grille[ligne][colonne] and position_des_valeurs[-1]==ligne-1 and valeur>0:
                position_des_valeurs.append(ligne)
            else:
                if len(position_des_valeurs)>=3:
                    for ligne_a_suppr in position_des_valeurs:
                        #print("delete bloc verticale",position_des_valeurs,colonne)
                        anim,grille[ligne_a_suppr][colonne]=grille[ligne_a_suppr][colonne],0
                        animation_suppr_bloc(ligne_a_suppr,colonne,anim)
                valeur=grille[ligne][colonne]
                position_des_valeurs=[ligne]
        if len(position_des_valeurs)>=3:
            for ligne_a_suppr in position_des_valeurs:
                anim,grille[ligne_a_suppr][colonne]=grille[ligne_a_suppr][colonne],0
                animation_suppr_bloc(ligne_a_suppr,colonne,anim)
                #print("delete bloc verticale")



    #Diagonal: Haut droit vers bas gauche

    for ligne in range(11):
        for colonne in range(2,6):
            if grille[ligne][colonne]>0:
                valeur,position_des_valeurs=grille[ligne][colonne],[[ligne,colonne]]
            else:
                valeur,position_des_valeurs=-9,[[-1,-1]]


            test_colonne,test_ligne=colonne,ligne
            while test_colonne>-1 and test_ligne<13:
                if grille[test_ligne][test_colonne]==valeur and position_des_valeurs[-1]==[test_ligne-1,test_colonne+1] and valeur>0:
                    position_des_valeurs.append([test_ligne,test_colonne])
                else:
                    if len(position_des_valeurs)>=3:
                        for bloc_a_suppr in position_des_valeurs:
                            anim,grille[bloc_a_suppr[0]][bloc_a_suppr[1]]=grille[bloc_a_suppr[0]][bloc_a_suppr[1]],0
                            animation_suppr_bloc(bloc_a_suppr[0],bloc_a_suppr[1],anim)

                    if grille[test_ligne][test_colonne]>0:
                        position_des_valeurs,valeur=[[test_ligne,test_colonne]],grille[test_ligne][test_colonne]
                test_ligne+=1
                test_colonne-=1
            if len(position_des_valeurs)>=3:
                for bloc_a_suppr in position_des_valeurs:
                    anim,grille[bloc_a_suppr[0]][bloc_a_suppr[1]]=grille[bloc_a_suppr[0]][bloc_a_suppr[1]],0
                    animation_suppr_bloc(bloc_a_suppr[0],bloc_a_suppr[1],anim)

    #Diagonal: Haut gauche vers bas droite

    for ligne in range(11):
        for colonne in range(0,4):
            if grille[ligne][colonne]>0:
                valeur,position_des_valeurs=grille[ligne][colonne],[[ligne,colonne]]
            else:
                valeur,position_des_valeurs=-9,[[-1,-1]]


            test_colonne,test_ligne=colonne,ligne
            while test_colonne<6 and test_ligne<13:
                if grille[test_ligne][test_colonne]==valeur and position_des_valeurs[-1]==[test_ligne-1,test_colonne-1] and valeur>0:
                    position_des_valeurs.append([test_ligne,test_colonne])
                else:
                    if len(position_des_valeurs)>=3:
                        for bloc_a_suppr in position_des_valeurs:
                            anim,grille[bloc_a_suppr[0]][bloc_a_suppr[1]]=grille[bloc_a_suppr[0]][bloc_a_suppr[1]],0
                            animation_suppr_bloc(bloc_a_suppr[0],bloc_a_suppr[1],anim)

                    if grille[test_ligne][test_colonne]>0:
                        position_des_valeurs,valeur=[[test_ligne,test_colonne]],grille[test_ligne][test_colonne]
                test_ligne+=1
                test_colonne+=1
            if len(position_des_valeurs)>=3:
                for bloc_a_suppr in position_des_valeurs:
                    anim,grille[bloc_a_suppr[0]][bloc_a_suppr[1]]=grille[bloc_a_suppr[0]][bloc_a_suppr[1]],0
                    animation_suppr_bloc(bloc_a_suppr[0],bloc_a_suppr[1],anim)


def suppressions_bloc(a_suppr_position_x,a_suppr_position_y):
    """
    Entrée:
        a_suppr_position_x,a_suppr_position_y: lists
            Contiennent coordonnées x et y dans chaque liste distincte

    Instruction:
        Supprime les blocs aux coordonnées dans les listtes

    """

    if len(a_suppr_position_x)!=len(a_suppr_position_y):
        return

    for bloc in range(len(a_suppr_position_x)):
        pos_x=a_suppr_position_x[bloc]
        pos_y=a_suppr_position_y[bloc]

        bloc_pour_animation,grille[pos_y][pos_x]=grille[pos_y][pos_x],0
        animation_suppr_bloc(pos_y,pos_x,bloc_pour_animation)


def animation_suppr_bloc(coord_ligne,coord_colonne,id_bloc):
    #grille[coord_ligne][coord_colonne]=0
    global score
    score+=10
    affichage_disparition_dun_bloc(coord_colonne,coord_ligne,id_bloc)
    pygame.time.delay(200)
    affichage_disparition_dun_bloc(coord_colonne,coord_ligne,"bloc_missingno")
    pygame.time.delay(200)
    affichage_disparition_dun_bloc(coord_colonne,coord_ligne,id_bloc)
    pygame.time.delay(200)
    affichage_disparition_dun_bloc(coord_colonne,coord_ligne,"bloc_missingno")



def compteur_niveau(score,niveau):
    if niveau*1000<=score:
        niveau+=1
    return niveau


def fait_tomber_ensemble(blocs_mobiles,grille):
    global arreter_boucle_while_fait_tomber_ensemble


    arreter_boucle_while_fait_tomber_ensemble=True
    """
    Fait tomber l'ensemble tout en bas
    """
    coordx=blocs_mobiles[1][0]
    coordy=int(blocs_mobiles[1][1])+2 #Position y du dernier bloc de l'ensemble
    blocs_mobiles[1][1]=int(blocs_mobiles[1][1])
    while grille[coordy+1][coordx]==0 and grille[coordy-1][coordx]==0 and coordy<=10 and arreter_boucle_while_fait_tomber_ensemble==True:
        blocs_mobiles[1][1]+=1
        coordy=int(blocs_mobiles[1][1])+1 #Position y du dernier bloc de l'ensemble
        test_bloc(blocs_mobiles,grille)




jeu_en_cours=True
pause=False #Le jeu n'est pas en pause

blocs_suivants=nouveaux_blocs()
blocs_mobiles=nouveaux_blocs()
grille_mobile=[]

score=0
niveau=1
highscore=lecture_highscore()


temps_dattente_avant_input_keyboard=15
temps_dattente_avant_input_haut_keyboard=15

print("Chargement terminé. Lancement du jeu dans un instant...")

while jeu_en_cours==True: #Tant que le jeu est en cours de fonctionnement.

    if temps_dattente_avant_input_keyboard<=1:
        #Compte le temps avant de redonner la possibilité d'utiliser les touches
        temps_dattente_avant_input_keyboard+=1
    if temps_dattente_avant_input_haut_keyboard<=15:
        #Compteur spécial pour la touche ↑.
        #Afin d'éviter d'éviter un bug en plus de ne pas poser trop rapidement
        #d'affiler les ensembles.
        temps_dattente_avant_input_haut_keyboard+=1


    if pause==False:
        delete_blocs()
        niveau=compteur_niveau(score,niveau)


        if blocs_mobiles[1][1]<10:
            if niveau<=4:
                blocs_mobiles[1][1]+=0.01+0.01*niveau
            else:
                blocs_mobiles[1][1]+=0.05

        test_bloc(blocs_mobiles,grille)
        mise_a_jour_blocs(grille)

        for event in pygame.event.get(): #
            if event.type==QUIT:
                jeu_en_cours=False
                fin_de_jeu=False
                pygame.quit()
            if event.type == pygame.KEYDOWN and temps_dattente_avant_input_keyboard>=1:
                temps_dattente_avant_input_keyboard=-1
                #touche_activent permet d'éviter que l'utilisateur manipule l'ensemble
                #ou un prochain ensemble, quand le jeu n'est pas prêt.
                #Si c'est True, alors le joueur peut manipuler le jeu.
                #Sinon, il doit patienter un instant.
                if event.key==K_DOWN:
                    deplace_blocs(blocs_mobiles,"BAS",grille)
                elif event.key==K_LEFT:
                    deplace_blocs(blocs_mobiles,"GAUCHE",grille)
                elif event.key==K_RIGHT:
                    deplace_blocs(blocs_mobiles,"DROITE",grille)
                elif event.key==K_UP and temps_dattente_avant_input_haut_keyboard>=5:
                    temps_dattente_avant_input_haut_keyboard=-1
                    fait_tomber_ensemble(blocs_mobiles,grille)
                elif event.key==K_SPACE:
                    rotation_blocs(blocs_mobiles)
                elif event.key==K_ESCAPE:
                    jeu_en_cours=False
                    fin_de_jeu=False
                    pygame.quit()
                elif event.key==K_s:
                    #Affiche l'écran de sauvegarde s'il a atteint le Highscore
                    jeu_en_cours=False
                elif event.key==K_p:
                    #Met en pause le jeu
                    pause=True


        fenetre.blits(fond_mosaique) #Affiche la mosaïque d'image de fon de fenêtre.
        affiche_controles()
        affiche_highscore(highscore)
        affiche_suivant(blocs_suivants)
        affiche_score(score)
        affiche_niveau(niveau)


        #Fond blanc de jeu
        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(taille_x_fenetre/3-30, taille_y_fenetre/20+23, 23*11-6, 23*19+5))

        affichage_grille_de_jeu(grille)
        affichage_blocs_mobiles(blocs_mobiles)
        affiche_fd_jeu()

        bloc_tombant=len(grille_mobile)-1
        while bloc_tombant>=0:
            """
            Ici on s'occupe de chaque bloc de la grille qui tombe
            """
            #print(grille_mobile[bloc_tombant])

            #On le fait tomber.
            #Si on s'aperçoit qu'il est arriver à sa nouvelle position graphiquement
            #Alors bloc_tombant_modif==None.
            #Sinon, on aura la même liste mais avec les coordonnées y modifiés.
            bloc_tombant_modif=gestion_bloc_tombant(grille_mobile[bloc_tombant])

            if bloc_tombant_modif==None: #Si le bloc a été ancré
                del grille_mobile[bloc_tombant] #Il ne fait plus parti de la liste des blocs tombant
            bloc_tombant-=1

    else:
        #Le jeu est en pause
        pygame.draw.rect(fenetre, (50,50,50), pygame.Rect(taille_x_fenetre/3-30, taille_y_fenetre/20+23, 23*11-6, 23*19+5))
        affiche_fd_jeu()

        font_txt = pygame.font.Font('medias/font/windows_command_prompt.ttf', 40) #Paramètre la police
        text_surface = font_txt.render("En Pause",True,(255,255,255))
        fenetre.blit(text_surface,(taille_x_fenetre/3+20,taille_y_fenetre/20+225))

        for event in pygame.event.get(): #
            if event.type==QUIT:
                jeu_en_cours=False
                fin_de_jeu=False
                pygame.quit()
            if event.type == pygame.KEYDOWN and temps_dattente_avant_input_keyboard>=1:
                temps_dattente_avant_input_keyboard=-1
                if event.key==K_ESCAPE:
                    jeu_en_cours=False
                    fin_de_jeu=False
                    pygame.quit()
                elif event.key==K_s:
                    #Affiche l'écran de sauvegarde s'il a atteint le Highscore
                    jeu_en_cours=False
                elif event.key==K_p:
                    #Met en pause le jeu
                    pause=False

    pygame.display.flip()
    clock.tick(15)

fin_de_jeu=True
input_texte=0
bon_score=False

highscore=lecture_highscore() #Importe le highscore

if score>highscore[len(highscore)-1][1]:
    #Si le score du joueur est plus grand que le plus petit score enregistré,
    #alors il rentre dans le Hall of Fame.

    #On affiche l'écran de réussite:
    bon_score=True

fenetre_message(bon_score,score,input_texte)

user_text=""

compte_seconde=0

while fin_de_jeu==True:
    if compte_seconde<10:
        compte_seconde+=1
    else:
        compte_seconde=0
    for event in pygame.event.get(): #Si on veut quitter par la croix Windows
        if event.type==QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                #Touche pour sauvegarder et quitter le jeu.
                #Ou uniquement quitter le jeu si le joueur a perdu.
                if bon_score==False:
                    print("Fermeture du jeu Windoze...")
                    pygame.quit()


                elif bon_score==True:
                    print("Sauvegarde du score...")
                    if user_text=="":
                        user_text="Inconnu"
                    enregistrement_score(score,user_text)

                    print("Fermeture du jeu Windoze...")
                    pygame.quit()


            #On récupère les entrées textuels afin de l'afficher à l'écran.
            #https://www.youtube.com/watch?v=Rvcyf4HsWiw&ab_channel=ClearCode
            if event.key == pygame.K_BACKSPACE and bon_score==True:
                user_text = user_text[:-1]
            elif len(user_text)<=15 and bon_score==True:
                user_text += event.unicode



    if bon_score==True:
        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(taille_x_fenetre/3-15, taille_y_fenetre/20+220, 23*9+10, 23*1))

        font_txt = pygame.font.Font('medias/font/windows_command_prompt.ttf', 17) #Paramètre la police
        text_surface = font_txt.render(user_text,True,(0,0,0))
        fenetre.blit(text_surface,(taille_x_fenetre/3-6,taille_y_fenetre/20+225))

        #On affiche un curseur

        if len(user_text)>15:
            couleur_txt=(255,0,0)
        else:
            couleur_txt=(0,0,0)

        if compte_seconde<=5:
            curseur_txt = font_txt.render(user_text+"_",True,couleur_txt)
        else:
            curseur_txt = font_txt.render(user_text,True,couleur_txt)

        fenetre.blit(curseur_txt,(taille_x_fenetre/3-6,taille_y_fenetre/20+225))



    pygame.display.flip()
    clock.tick(10)
'''
enregistrement_score(score)
pygame.quit()
'''