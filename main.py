from random import randint
import pygame
import pygame.freetype
from pygame.locals import *  #sert seulement pour le FULLSCREEN
import os.path
import time

#Base
#os.chdir('C:/Users/bouch/Documents/Last Hope Expedition') #Pour changer de dossier de travail si sa marche pas
pygame.init()
pygame.display.set_caption('Last Hope Expedition')
GAME_FONT = pygame.freetype.Font("FoundationTwo.ttf", 15)
GAME_FONT_SIZE = pygame.font.Font(None, 24)
screen = pygame.display.set_mode((400, 300), FULLSCREEN)
color = pygame.Color(87, 87, 87, 87)
pygame.mixer.init()

#Pseudo
input_rect = pygame.Rect(110, 200, 140, 32)

#Variables
fond = pygame.image.load("MainMenuBG.png").convert()
fond = pygame.transform.scale(fond, (640, 480))
user_name = ''

# Main Menu

# Music Menu
if os.path.isfile(
        "sounds/MainMenu.mp3"
):  # joue un son ,si le fichier existe pour eviter de retourner une erreur si le fichier n'est pas là.
    pygame.mixer.music.load("sounds/MainMenu.mp3")
    pygame.mixer.music.play(-1)
    print("Music from Honkai Star rail")

stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_name = user_name[:-1]
            else:
                user_name += event.unicode

    screen.blit(fond, (0, 0))

    pygame.draw.rect(screen, color, input_rect)
    zonepseudo = GAME_FONT_SIZE.render(user_name, True, (255, 255, 255, 25))
    screen.blit(zonepseudo, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(100, zonepseudo.get_width() + 10)

    textintro, rect = GAME_FONT.render(
        "Bienvenue jeune heros dans Last Hope Expedition", (0, 0, 0))
    textintro2, rect = GAME_FONT.render(
        "un jeu de role numerique ou vous pourrez, aux files des choix",
        (0, 0, 0))
    textintro3, rect = GAME_FONT.render("vivre une aventure unique !",
                                        (0, 0, 0))
    textHans, rect = GAME_FONT.render(
        "Je serai votre maitre du jeu, Hans Der Schwartz.", (0, 0, 0))
    textpseudo, rect = GAME_FONT.render("Choisissez votre pseudo :")

    screen.blit(textpseudo, (50, 170))
    screen.blit(textintro, (40, 25))
    screen.blit(textintro2, (40, 50))
    screen.blit(textintro3, (40, 75))
    screen.blit(textHans, (40, 320))

    image_start = pygame.image.load("start.png").convert_alpha()
    image_start = pygame.transform.scale(image_start, (128, 128))
    clickable_area_start = pygame.Rect((350, 140), (128, 128))
    screen.blit(image_start, clickable_area_start)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  #quand je relache le bouton
            if clickable_area_start.collidepoint(event.pos):
                stop = True
                if user_name == '':
                    user_name = "Player"

    pygame.display.update()

class Fusil_Precision:

    def __init__(self):
        self.nom = "fusil_precision"
        self.attaque = randint(25, 30)
        self.precision = randint(80, 85)


class Arbalete:

    def __init__(self):
        self.nom = "arbalete"
        self.attaque = randint(30, 35)
        self.precision = randint(75, 80)


class Pistolet_laser:

    def __init__(self):
        self.nom = "pistolet_laser"
        self.attaque = randint(20, 25)
        self.precision = randint(50, 70)


class Fusil_assaut:

    def __init__(self):
        self.nom = "fusil_assaut"
        self.attaque = randint(45, 50)
        self.precision = randint(50, 55)




fusil_precision = Fusil_Precision()
arbalete = Arbalete()
pistolet_laser = Pistolet_laser()
fusil_assaut = Fusil_assaut()

armes = []

# Sélection sexe

stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    texteintro, rect = GAME_FONT.render(
        "Bienvenue " + user_name + ", maintenant choisissez votre sexe :",
        (0, 0, 0))

    fond = pygame.image.load(
        "MainMenuBG.png").convert()  #Pour retirer l'ancien affichage
    fond = pygame.transform.scale(fond, (640, 480))

    screen.blit(fond, (0, 0))
    screen.blit(texteintro, (40, 25))

    image_homme = pygame.image.load("Homme.png").convert_alpha()
    image_homme = pygame.transform.scale(image_homme, (128, 128))
    image_femme = pygame.image.load("Femme.png").convert_alpha()
    image_femme = pygame.transform.scale(image_femme, (128, 128))

    clickable_area_homme = pygame.Rect((100, 100), (128, 128))
    clickable_area_femme = pygame.Rect((300, 100), (128, 128))
    screen.blit(image_homme, clickable_area_homme)
    screen.blit(image_femme, clickable_area_femme)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  #quand je relache le bouton
            if clickable_area_homme.collidepoint(event.pos):
                sexe_perso = "homme"
                stop = True
            elif clickable_area_femme.collidepoint(event.pos):
                sexe_perso = "femme"
                stop = True

    pygame.display.flip()

# Sélection Classe


def test():
    stop = False
    
    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True

        if sexe_perso == "homme":
            textconfirmation, rect = GAME_FONT.render(
                f"Parfait {user_name}, vous etes un Homme", (0, 0, 0))
        else:
            textconfirmation, rect = GAME_FONT.render(
                f"Parfait {user_name}, vous etes une Femme", (0, 0, 0))
        textintro, rect = GAME_FONT.render("Maintenant, choisissez votre classe :",
                                           (0, 0, 0))
        textarme, rect = GAME_FONT.render("arme :", (0, 0, 0))
        textinforole1, rect = GAME_FONT.render("passez sur un role pour avoir")
        textinforole2, rect = GAME_FONT.render("le descriptif de ses competences.")
        fond = pygame.image.load(
            "MainMenuBG.png").convert()  #Pour retirer l'ancien affichage
        fond = pygame.transform.scale(fond, (640, 480))
    
        screen.blit(fond, (0, 0))
        screen.blit(textconfirmation, (40, 25))
        screen.blit(textintro, (40, 50))
        screen.blit(textarme, (450, 350))
        screen.blit(textinforole1, (350, 300))
        screen.blit(textinforole2, (350, 320))
        # Affichage des images pour les classes
        image_ingenieur = pygame.image.load("perso/ingenieur.png").convert_alpha()
        image_ingenieur = pygame.transform.scale(image_ingenieur, (128, 128))
        image_medecin = pygame.image.load("perso/medecin.png").convert_alpha()
        image_medecin = pygame.transform.scale(image_medecin, (128, 128))
        image_scout = pygame.image.load("perso/scout.png").convert_alpha()
        image_scout = pygame.transform.scale(image_scout, (128, 128))
        image_soldat = pygame.image.load("perso/soldat.png").convert_alpha()
        image_soldat = pygame.transform.scale(image_soldat, (128, 128))
        image_info = pygame.image.load("info.png").convert_alpha()
        image_info= pygame.transform.scale(image_info, (64, 64))
        
        clickable_area_ingenieur = pygame.Rect((50, 150), (128, 128))
        clickable_area_medecin = pygame.Rect((200, 150), (128, 128))
        clickable_area_scout = pygame.Rect((50, 300), (128, 128))
        clickable_area_soldat = pygame.Rect((200, 300), (128, 128))
        clickable_area_info = pygame.Rect((450, 200), (64, 64))
        
        screen.blit(image_ingenieur, clickable_area_ingenieur)
        screen.blit(image_medecin, clickable_area_medecin)
        screen.blit(image_scout, clickable_area_scout)
        screen.blit(image_soldat, clickable_area_soldat)
        screen.blit(image_info,clickable_area_info)
    
        # Affichage de la description de chaque classe
        if sexe_perso == "homme":
            text_ingenieur, rect_ingenieur = GAME_FONT.render(
                "Ingenieur : Fort en informatique, peut facilement brouiller l'enemie",
                (0, 0, 0))
            text_medecin, rect_medecin = GAME_FONT.render(
                "Medecin : Maitrise la medecine pour eviter les infections et se soigner",
                (0, 0, 0))
            text_scout, rect_scout = GAME_FONT.render(
                "Scout : Agile et rapide, Toujours le premier a tirer mais a moins de vie",
                (0, 0, 0))
            text_soldat, rect_soldat = GAME_FONT.render(
                "Soldat : Expert en combat pour faire disparaitre son enemie",
                (0, 0, 0))
        else:
            text_ingenieur, rect_ingenieur = GAME_FONT.render(
                "Ingenieure : Forte en informatique, peut facilement brouiller l'enemie",
                (0, 0, 0))
            text_medecin, rect_medecin = GAME_FONT.render(
                "Medecin : Maitrise la medecine pour eviter les infections et se soigner",
                (0, 0, 0))
            text_scout, rect_scout = GAME_FONT.render(
                "Scoute : Agile et rapide, Toujours le premier a tirer mais a moins de vie",
                (0, 0, 0))
            text_soldat, rect_soldat = GAME_FONT.render(
                "Soldate : Experte en combat pour faire disparaitre son ennemie",
                (0, 0, 0))
    
        #armes
    
        textarmeingenieur, rect_ingenieur = GAME_FONT.render(
            "Pistolet laser", (0, 0, 0))
        textarmemedecin, rect_medecin = GAME_FONT.render(
            "arbalete tranquillisante", (0, 0, 0))
        textarmescout, rect_scout = GAME_FONT.render("fusil de precision",
                                                     (0, 0, 0))
        textarmesoldat, rect_soldat = GAME_FONT.render(
            "fusil d'assaut automatique", (0, 0, 0))
    
        # Si la souris est sur une des classes, affichage de la description de cette classe
    
        if clickable_area_ingenieur.collidepoint(pygame.mouse.get_pos()):
            screen.blit(text_ingenieur, (30, 130))
            screen.blit(textarmeingenieur, (400, 375))
        elif clickable_area_medecin.collidepoint(pygame.mouse.get_pos()):
            screen.blit(text_medecin, (30, 130))
            screen.blit(textarmemedecin, (400, 375))
        elif clickable_area_scout.collidepoint(pygame.mouse.get_pos()):
            screen.blit(text_scout, (30, 130))
            screen.blit(textarmescout, (400, 375))
        elif clickable_area_soldat.collidepoint(pygame.mouse.get_pos()):
            screen.blit(text_soldat, (30, 130))
            screen.blit(textarmesoldat, (400, 375))
    

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:  #quand je relache le bouton
                if clickable_area_ingenieur.collidepoint(event.pos):
                    stop = True
                    if sexe_perso == "homme" :
                        role ="Ingenieur"
                    else:
                        role ="Ingenieure"
                if clickable_area_medecin.collidepoint(event.pos):
                    stop = True
                    role = "Medecin"
                if clickable_area_scout.collidepoint(event.pos):
                    stop = True
                    if sexe_perso == "homme" :
                        role ="Scout"
                    else:
                        role ="Scoute"
                if clickable_area_soldat.collidepoint(event.pos):
                    stop = True
                    if sexe_perso == "homme":
                        role = "Soldat"
                    else :
                        role = "Soldate"
                if clickable_area_info.collidepoint(event.pos):
                    stop = True
                    role = "info"
                    
        pygame.display.flip()        
    
        pygame.display.flip()
    back=pygame.image.load('retour.png').convert_alpha()
    back= pygame.transform.scale(back, (80, 80))
    image_start = pygame.image.load('start.png').convert_alpha()
    image_start = pygame.transform.scale(image_start, (128, 128))
    clickable_area_start = pygame.Rect((450,320), (128, 128))
    clickable_area_back = pygame.Rect((50,350), (80, 80))
    desst1, rect1 = GAME_FONT.render("6 ou moins : Handicapant. Cet attribut est si mauvais ", (0, 0, 0))
    desst12, rect12 = GAME_FONT.render("qu'il vous gene enormement dans votre vie.", (0, 0, 0))
    desst2,rect2 = GAME_FONT.render("7 : Faible. Vos lacunes sont visibles."
, (0, 0, 0))
    desst22,rect22 = GAME_FONT.render(" de tous ceux qui vous rencontrent."
, (0, 0, 0))
    desst4,rect4= GAME_FONT.render( "8 ou 9 : Sous la moyenne. Ces scores sont limitants", (0, 0, 0))
    desst42,rect42= GAME_FONT.render( " mais dans la norme humaine.", (0, 0, 0))
    desst5,rect5= GAME_FONT.render("10: Moyen. La plupart des personnes dans le monde ", (0, 0, 0))
    desst52,rect52= GAME_FONT.render("ont une vie satisfaisante avec un score de 10.", (0, 0, 0))
    desst6,rect6= GAME_FONT.render("11 ou 12 : Au-dessus de la moyenne. Ces scores", (0, 0, 0))
    desst62,rect62= GAME_FONT.render("sont superieurs,mais dans la norme humaine.", (0, 0, 0))
    desst7,rect7= GAME_FONT.render( "13 ou 14 : Exceptionnel. De tels attributs sont immediatement apparents", (0, 0, 0))
    desst72,rect72= GAME_FONT.render("des muscles saillants, une grâce feline, un discours astucieux ou une vitalite eclatante", (0, 0, 0))
    desst8,rect8= GAME_FONT.render(
"15 ou plus : Incroyable. Un tel niveau attire constamment commentaires de la part des autres et guident vos choix de vie", (0, 0, 0))


    roledef = ""
    
    stop = False
    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True

        screen.blit(fond, (0, 0))
       
        if role == "Soldat" or role == "Soldate":
            screen.blit(text_soldat, (30, 130))
            screen.blit(back, (50,350))
            screen.blit(image_start,(450,320))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if clickable_area_start.collidepoint(event.pos):
                        stop = True
                        roledef = role
                    elif clickable_area_back.collidepoint(event.pos):
                        stop = True
                        test()
        elif role == "Scout" or role =="Scoute":
            screen.blit(text_scout, (30, 130))
            screen.blit(back, (50,350))
            screen.blit(image_start,(450,320))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if clickable_area_start.collidepoint(event.pos):
                        stop = True
                        roledef = role
                    elif clickable_area_back.collidepoint(event.pos):
                        stop = True
                        test()
        elif role == "Medecin":
            screen.blit(text_medecin, (30, 130))
            screen.blit(back, (50,350))
            screen.blit(image_start,(450,320))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if clickable_area_start.collidepoint(event.pos):
                        stop = True
                        roledef = role
                    elif clickable_area_back.collidepoint(event.pos):
                        stop = True
                        test()
        elif role == "Ingenieure" or role == "Ingenieur":
            screen.blit(text_ingenieur, (30, 130))
            screen.blit(back, (50,350))
            screen.blit(image_start,(450,320))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if clickable_area_start.collidepoint(event.pos):
                        stop = True
                        roledef = role
                    elif clickable_area_back.collidepoint(event.pos):
                        stop = True
                        test()
        elif role == "info":
            screen.blit(desst1, (30, 60))
            screen.blit(desst12, (30, 80))
            screen.blit(desst2, (30, 100))
            screen.blit(desst22, (30, 120))
            screen.blit(desst4, (30, 140))
            screen.blit(desst42, (30, 160))
            screen.blit(desst5, (30, 180))
            screen.blit(desst52, (30, 200))
            screen.blit(desst6, (30, 220))
            screen.blit(desst62, (30, 240))
            screen.blit(desst7, (30, 260))
            screen.blit(desst72, (30, 280))
            screen.blit(desst8, (30, 300))
            screen.blit(back, (50,350))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if clickable_area_back.collidepoint(event.pos):
                        stop = True 
                        test()
       
        pygame.display.flip()
    return (roledef)
role = test()

if role == "Soldat" or role == "Soldate":
    armes.append(fusil_assaut)
    joueur_img = "perso/soldat_img.png"
if role == "Medecin":
    armes.append(arbalete)
    joueur_img = "perso/medecin_img.png"
if role == "Ingenieure" or role == "Ingenieur":
    armes.append(pistolet_laser)
    joueur_img = "perso/ingenieur_img.png"
if role == "Scoute" or role == "Scout":
    armes.append(fusil_precision)
    joueur_img = "perso/scout_img.png"
# Sélection objets

# Définition des 6 objets
class Fumigene:

    def __init__(self, nombre):
        self.nom = "fumigene"
        self.nombre = nombre
        self.nombre_de_tour = 2


class Grenade:

    def __init__(self, degat, nombre):
        self.nom = "grenade"
        self.nombre = nombre
        self.degat = degat


class Soin:

    def __init__(self, soin, nombre):
        self.nom = "soin"
        self.nombre = nombre
        self.soin = soin


class Bouclier:
    """1 seul maximum"""

    def __init__(self):
        self.nom = "bouclier"
        self.nombre = 1
        self.durabilite = 80


class Piege:
    """1 seul Maximum"""

    def __init__(self, degat, durabilite):
        self.nom = "piege"
        self.nombre = 1
        self.degat = degat
        self.durabilite = durabilite


class Phone:

    def __init__(self, nb_appel):
        self.nom = "phone"
        self.nombre = nb_appel
        self.ami_nb_obj_soin = 2
        self.ami_obj_soin = 20
        self.ami_degat = 10


# Initialiser les objets selon le role
bouclier = Bouclier()
fumigene = Fumigene(1)
if role == "Scoute" or role == "Scoute":
    piege = Piege(20, 70)
else:
    piege = Piege(15, 50)
if role == "Soldat" or role == "Soldate":
    grenade = Grenade(50, 1)
else:
    grenade = Grenade(30, 1)
if role == "Medecin" :
    soin = Soin(80, 1)
else:
    soin = Soin(40, 1)
if role == "Ingenieur" or role == "Ingenieure":
    phone = Phone(2)
else:
    phone = Phone(1)

# Initialisation hors de la boucle
inventaire = set()


stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    fond = pygame.image.load("MainMenuBG.png").convert()
    fond = pygame.transform.scale(fond, (640, 480))

    screen.blit(fond, (0, 0))

    if sexe_perso == "homme":
        textconfirmation, rect = GAME_FONT.render(
            f"Parfait {user_name}, vous etes un {role}", (0, 0, 0))
    else:
        textconfirmation, rect = GAME_FONT.render(
            f"Parfait {user_name}, vous etes une {role}", (0, 0, 0))
    textintro, rect = GAME_FONT.render("Maintenant choisissez 4 objets :",
                                       (0, 0, 0))
    textintro2, rect = GAME_FONT.render(
        "Vous pouvez recliquer sur l'objet pour le retirer", (0, 0, 0))

    screen.blit(textconfirmation, (40, 15))
    screen.blit(textintro, (40, 40))
    screen.blit(textintro2, (40, 65))

    image_grenade = pygame.image.load("objets/grenade.png").convert_alpha()
    image_grenade = pygame.transform.scale(image_grenade, (128, 128))
    image_soin = pygame.image.load("objets/soin.png").convert_alpha()
    image_soin = pygame.transform.scale(image_soin, (128, 128))
    image_piege = pygame.image.load("objets/piege.png").convert_alpha()
    image_piege = pygame.transform.scale(image_piege, (128, 128))
    image_phone = pygame.image.load("objets/phone.png").convert_alpha()
    image_phone = pygame.transform.scale(image_phone, (128, 128))
    image_bouclier = pygame.image.load("objets/bouclier.png").convert_alpha()
    image_bouclier = pygame.transform.scale(image_bouclier, (128, 128))
    image_fumigene = pygame.image.load("objets/fumigene.png").convert_alpha()
    image_fumigene = pygame.transform.scale(image_fumigene, (128, 128))

    clickable_area_grenade = pygame.Rect((50, 150), (128, 128))
    clickable_area_soin = pygame.Rect((200, 150), (128, 128))
    clickable_area_piege = pygame.Rect((50, 300), (128, 128))
    clickable_area_phone = pygame.Rect((200, 300), (128, 128))
    clickable_area_bouclier = pygame.Rect((350, 150), (128, 128))
    clickable_area_fumigene = pygame.Rect((350, 300), (128, 128))

    screen.blit(image_grenade, clickable_area_grenade)
    screen.blit(image_soin, clickable_area_soin)
    screen.blit(image_piege, clickable_area_piege)
    screen.blit(image_phone, clickable_area_phone)
    screen.blit(image_bouclier, clickable_area_bouclier)
    screen.blit(image_fumigene, clickable_area_fumigene)

    textgrenade, rect_grenade = GAME_FONT.render(
        f"Grenade : inflige {grenade.degat} pv", (0, 0, 0))
    textsoin, rect_soin = GAME_FONT.render(f"Soin : Soigne {soin.soin}pv",
                                           (0, 0, 0))
    textpiege, rect_piege = GAME_FONT.render(
        f"Piege : Inflige {piege.degat}pv/tour", (0, 0, 0))
    if phone.nombre >= 2:
        textphone, rect_phone = GAME_FONT.render(
            f"Phone : Appelle {phone.nombre} personnes pour t'aider",
            (0, 0, 0))
    else:
        textphone, rect_phone = GAME_FONT.render(
            f"Phone : Appelle {phone.nombre} personne pour t'aider", (0, 0, 0))
    textbouclier, rect_bouclier = GAME_FONT.render(
        "Bouclier : bloque les attaques mais perd en durabilite", (0, 0, 0))
    textfumigene, rect_fumigene = GAME_FONT.render(
        f"Fumigene : Retire {fumigene.nombre_de_tour} tours a l'enemie",
        (0, 0, 0))

    if inventaire == set():
        textinventairetemp = "0 objet"
    else:
        noms_objets = [objet.nom for objet in inventaire]
        textinventairetemp = ", ".join(noms_objets)

    textinventaire, rect = GAME_FONT.render(
        f"Vous avez selectionne : {textinventairetemp}", (0, 0, 0))

    if clickable_area_grenade.collidepoint(pygame.mouse.get_pos()):
        screen.blit(textgrenade, (30, 130))
    if clickable_area_soin.collidepoint(pygame.mouse.get_pos()):
        screen.blit(textsoin, (30, 130))
    if clickable_area_piege.collidepoint(pygame.mouse.get_pos()):
        screen.blit(textpiege, (30, 130))
    if clickable_area_phone.collidepoint(pygame.mouse.get_pos()):
        screen.blit(textphone, (30, 130))
    if clickable_area_bouclier.collidepoint(pygame.mouse.get_pos()):
        screen.blit(textbouclier, (30, 130))
    if clickable_area_fumigene.collidepoint(pygame.mouse.get_pos()):
        screen.blit(textfumigene, (30, 130))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  #quand je relache le bouton
            if clickable_area_grenade.collidepoint(event.pos):
                if not grenade in inventaire:
                    inventaire.add(grenade)
                else:
                    inventaire.remove(grenade)
            if clickable_area_soin.collidepoint(event.pos):
                if not soin in inventaire:
                    inventaire.add(soin)
                else:
                    inventaire.remove(soin)
            if clickable_area_piege.collidepoint(event.pos):
                if not piege in inventaire:
                    inventaire.add(piege)
                else:
                    inventaire.remove(piege)
            if clickable_area_phone.collidepoint(event.pos):
                if not phone in inventaire:
                    inventaire.add(phone)
                else:
                    inventaire.remove(phone)
            if clickable_area_bouclier.collidepoint(event.pos):
                if not bouclier in inventaire:
                    inventaire.add(bouclier)
                else:
                    inventaire.remove(bouclier)
            if clickable_area_fumigene.collidepoint(event.pos):
                if not fumigene in inventaire:
                    inventaire.add(fumigene)
                else:
                    inventaire.remove(fumigene)
            if len(inventaire) >= 4:
                stop = True

    screen.blit(textinventaire, (50, 90))

    pygame.display.flip()

# Conclusion des caractéristiques

#Init variable randint en dehors de la boucle
if role == "Scout" or role == "Scoute":
    vie = randint(85, 90)
    vitesse = 100
else:
    vie = 100
    vitesse = 50

textinventairetemp = ""
noms_objets = [objet.nom for objet in inventaire]
textinventairetemp = ", ".join(noms_objets)

# Définition du Joueur


class Joueur:

    def __init__(self, role, name, sexe, joueur_img, vie, vitesse, attaques,
                 objets):
        self.nom = name
        self.sexe = sexe
        self.role = role
        self.image = pygame.image.load(joueur_img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (128, 200))
        self.vie = vie
        self.vitesse = vitesse
        self.attaque = attaques
        self.objets = objets
        self.objets_en_list = list(self.objets)


joueur = Joueur(role, user_name, sexe_perso, joueur_img, vie, vitesse, armes,
                inventaire)

stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    fond = pygame.image.load(
        "MainMenuBG.png").convert()  #Pour retirer l'ancien affichage si besoin
    fond = pygame.transform.scale(fond, (640, 480))

    screen.blit(fond, (0, 0))

    textintro, rect = GAME_FONT.render(
        "Bien, voici toutes vos caracteristiques :", (0, 0, 0))
    textintro1, rect = GAME_FONT.render(sexe_perso, (0, 0, 0))
    textintro2, rect = GAME_FONT.render(role, (0, 0, 0))

    textpv, rect = GAME_FONT.render(f"{vie} PV", (0, 0, 0))

    textobjet, rect = GAME_FONT.render(f"Objets : {textinventairetemp}",
                                       (0, 0, 0))

    screen.blit(textintro, (40, 25))
    screen.blit(textintro1, (80, 50))
    screen.blit(textintro2, (80, 75))
    screen.blit(textpv, (80, 100))
    screen.blit(textobjet, (80, 125))

    image_start = pygame.image.load("start.png").convert_alpha()
    image_start = pygame.transform.scale(image_start, (128, 128))
    clickable_area_start = pygame.Rect((300, 150), (128, 128))
    screen.blit(image_start, clickable_area_start)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  #quand je relache le bouton
            if clickable_area_start.collidepoint(event.pos):
                stop = True
                if os.path.isfile(
                        "sounds/MainTheme.mp3"
                ):  # joue un son ,si le fichier existe pour eviter de retourner une erreur si le fichier n'est pas là.
                    pygame.mixer.init()
                    pygame.mixer.music.load("sounds/MainTheme.mp3")
                    pygame.mixer.music.play(-1)
                    print("Music from Stray")

    pygame.display.flip()

#definition PNJ


class PNJ :
    def __init__(self, nom, pv, force, IQ, vitalite, dexterite):
        self.nom = nom  
        self.pv = pv
        self.force = force
        self.IQ = IQ
        self.vitalite = vitalite
#Intro au jeu

stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    fond = pygame.image.load("GameBG.png").convert()
    fond = pygame.transform.scale(fond, (640, 480))

    screen.blit(fond, (0, 0))

    textintro1, rect = GAME_FONT.render(
        "Le 4 septembre 2037 la Terre s'ecroule a cause du climat ")
    textintro2, rect = GAME_FONT.render("et de la pollution.")
    textintro3, rect = GAME_FONT.render(
        "Lors d'une enieme mission les scientifiques ramenerent une bacterie")
    textintro4, rect = GAME_FONT.render(
        "pour l'etudier, malheureusement elle muta rapidement et dans le secret."
    )
    textintro5, rect = GAME_FONT.render(
        "En quelques mois elle transformat tous les humains en cadavres ")
    textintro6, rect = GAME_FONT.render(
        "deambulants, des Rodeurs .14 annees plus tard, seul quelques")
    textintro7, rect = GAME_FONT.render(
        "millions d'humains vivants en communaute sont encore en vie.")

    screen.blit(textintro1, (20, 25))
    screen.blit(textintro2, (20, 50))
    screen.blit(textintro3, (20, 75))
    screen.blit(textintro4, (20, 100))
    screen.blit(textintro5, (20, 125))
    screen.blit(textintro6, (20, 150))
    screen.blit(textintro7, (20, 175))

    image_continuer = pygame.image.load("boutoncontinuer.png").convert_alpha()
    image_continuer = pygame.transform.scale(image_continuer, (64, 64))

    clickable_area_continuer = pygame.Rect((525, 350), (64, 64))

    screen.blit(image_continuer, clickable_area_continuer)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  #quand je relache le bouton
            if clickable_area_continuer.collidepoint(event.pos):
                stop = True

    pygame.display.flip()

#Intro au jeu 2

#init hors de la boucle

noms = [
    "Bob", "David", "Henri", "Benoit", "Jack", "Tom", "Albert", "Andre",
    "Nicolas", "Georges", "Layton", "Karl Tastroff"
]
idnom = randint(0, len(noms) - 1)
nomscientifique = noms[idnom]

noms_ville = [
    "Nova Terra", "Ironhaven", "Phoenix Ridge", "New Dawn City", "Haven's End"
]
idnom_ville = randint(0, len(noms_ville) - 1)
nom_ville = noms_ville[idnom_ville]

stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    fond = pygame.image.load("GameBG.png").convert()
    fond = pygame.transform.scale(fond, (640, 480))

    screen.blit(fond, (0, 0))

    imagescientifique = pygame.image.load("scientifique.png").convert_alpha()
    imagescientifique = pygame.transform.scale(imagescientifique, (256, 280))

    screen.blit(imagescientifique, (200, 200))

    textintro1, rect = GAME_FONT.render(
        f"Voici le scientifique {nomscientifique}, qui faut accompagner",
        (0, 0, 0))
    textintro2, rect = GAME_FONT.render(f"vers {nom_ville} !", (0, 0, 0))
    textintro3, rect = GAME_FONT.render(
        "Seul lui a le vaccin contre cette bacterie !", (0, 0, 0))
    textnomscientifique, rect = GAME_FONT.render("Dr." + nomscientifique,
                                                 (0, 0, 0))

    screen.blit(textintro1, (20, 25))
    screen.blit(textintro2, (20, 50))
    screen.blit(textintro3, (20, 75))
    screen.blit(textnomscientifique, (300, 225))

    image_continuer = pygame.image.load("boutoncontinuer.png").convert_alpha()
    image_continuer = pygame.transform.scale(image_continuer, (64, 64))

    clickable_area_continuer = pygame.Rect((525, 350), (64, 64))

    screen.blit(image_continuer, clickable_area_continuer)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  #quand je relache le bouton
            if clickable_area_continuer.collidepoint(event.pos):
                stop = True

    pygame.display.flip()

# Classe Combat tour par tour et ce qui va avec

# Import images
attaque_image = pygame.image.load("bouton_armes.png").convert_alpha()
attaque_image = pygame.transform.scale(attaque_image, (128, 128))
objets_image = pygame.image.load("bouton_objets.png").convert_alpha()
objets_image = pygame.transform.scale(objets_image, (128, 128))
retour_image = pygame.image.load("retour.png").convert_alpha()
retour_image = pygame.transform.scale(retour_image, (64, 64))
victoire_image = pygame.image.load("victoire.png").convert_alpha()
victoire_image = pygame.transform.scale(victoire_image, (450, 256))
defaite_image = pygame.image.load("defaite.png").convert_alpha()
defaite_image = pygame.transform.scale(defaite_image, (450, 256))

# Import Sons
gunsound = pygame.mixer.Sound("sounds/gunshot.mp3")
success = pygame.mixer.Sound("sounds/Success.mp3")
failure = pygame.mixer.Sound("sounds/Failure.mp3")
soin_sound = pygame.mixer.Sound("sounds/soin.mp3")
grenade_sound = pygame.mixer.Sound("sounds/grenade.mp3")
piege_sound = pygame.mixer.Sound("sounds/piege.mp3")
bouclier_sound = pygame.mixer.Sound("sounds/bouclier.mp3")
phone_sound = pygame.mixer.Sound("sounds/phone.mp3")
fumigene_sound = pygame.mixer.Sound("sounds/fumigene.mp3")
casse_sound = pygame.mixer.Sound("sounds/casse.mp3")


class Combat:

    def __init__(self, joueur, adversaire):
        self.joueur = joueur
        self.adversaire = adversaire
        self.attaque_selectionnee = None
        self.objet_selectionne = None
        self.bouton_selectionne = None
        self.tour = 1
        self.tour_enemi_en_moins = 0
        self.piege_active = False
        self.piege_vie = None
        self.bouclier_vie = None
        self.phone_active = False
        self.phone_ami_nb_soin = 0
        self.phone_ami_soin = 0
        self.phone_ami_degat = 0
        self.phone_nombre = None
        self.victoire = None

    def afficher(self, surface):
        screen.blit(fond, (0, 0))

        # Affichage des images des personnages
        surface.blit(self.joueur.image, (50, 100))
        surface.blit(self.adversaire.image, (500, 100))

        # Affichage des Noms des personnages
        textjoueur, rectjoueur = GAME_FONT.render(self.joueur.nom)
        textadversaire, rectadversaire = GAME_FONT.render(self.adversaire.nom)

        surface.blit(textjoueur, (50, 20))
        surface.blit(textadversaire, (500, 20))

        # Affichage des barres de vie
        pygame.draw.rect(surface, (255, 0, 0),
                         (50, 50, self.joueur.vie * 2, 20))
        pygame.draw.rect(surface, (255, 0, 0),
                         (400, 50, self.adversaire.vie * 2, 20))

        # Affichage de la liste d'attaques si une attaque est sélectionnée
        if self.bouton_selectionne == "attaque":
            for i, attaque in enumerate(self.joueur.attaque):
                image = pygame.image.load(
                    f"armes/{self.joueur.attaque[i].nom}.png").convert_alpha()
                image = pygame.transform.scale(image, (128, 128))
                surface.blit(image, (50 + i * 150, 320))

        # Affichage de la liste d'objets si un objet est sélectionné
        if self.bouton_selectionne == "objets":
            k = 0
            list_obj = list(self.joueur.objets)
            for i, objets in enumerate(self.joueur.objets):
                image = pygame.image.load(
                    f"objets/{list_obj[i].nom}.png").convert_alpha()
                image = pygame.transform.scale(image, (64, 64))
                if list_obj[i].nombre > 1:
                    textimage, rect = GAME_FONT.render(
                        f"x {list_obj[i].nombre}", (0, 0, 0))
                if i < 3:
                    surface.blit(image, (50 + i * 150, 300))
                    if list_obj[i].nombre > 1:
                        surface.blit(textimage, (60 + i * 150, 364))
                if i > 2:
                    surface.blit(image, (50 + k * 150, 400))
                    if list_obj[i].nombre > 1:
                        surface.blit(textimage, (60 + k * 150, 464))
                    k = k + 1

        # Affichage des boutons d'attaque et d'objet
        if self.bouton_selectionne == None:
            surface.blit(attaque_image, (50, 330))
            surface.blit(objets_image, (200, 330))

        # Affichage du bouton de retour si une attaque ou un objet est sélectionné
        if self.bouton_selectionne == "attaque" or self.bouton_selectionne == "objets":
            surface.blit(retour_image, (550, 400))

        # Affichage du texte du tour
        texte_tour = GAME_FONT_SIZE.render(f"Tour {self.tour}", True,
                                           (0, 0, 0))
        surface.blit(texte_tour, (300, 50))

        # Affichage de vicoire ou de defaite quand la partie est fini , en dernier pour qu'il soit devant
        if self.victoire != None:
            if self.victoire == True:
                surface.blit(victoire_image, (100, 100))
            elif self.victoire == False:
                surface.blit(defaite_image, (100, 100))

    def attaquer(self, indexattaque):
        degats = self.joueur.attaque[
            indexattaque].attaque  # on récupère les dégâts de l'attaque 1 du joueur
        precision = self.joueur.attaque[
            indexattaque].precision  # on récupère la précision de l'attaque 1 du joueur

        if randint(
                1, 100
        ) <= precision:  # l'attaque réussit si le nombre aléatoire est inférieur ou égal à la précision
            if degats - self.adversaire.defense <= 0:
                print(f"{self.adversaire.nom} n'a pas reçus de dégâts")
            else:
                degats -= self.adversaire.defense
                self.adversaire.vie -= degats
                print(
                    f"{self.joueur.nom} inflige {degats} dégâts à {self.adversaire.nom}"
                )
            gunsound.play()
        else:
            print(
                f"{self.joueur.nom} rate son attaque sur {self.adversaire.nom}"
            )

    def index_objet(self, setobj, index):
        """donne le nom de l'objet en index 'index' dans le set 'setobj' car on ne peut pas le faire avec []"""
        for i, obj in enumerate(setobj):
            if i == index:
                return obj

    def selection_objet(self, index_obj):
        self.bouton_selectionne = None
        self.objet_selectionne = self.joueur.objets_en_list[index_obj].nom
        self.afficher(screen)
        self.utilisation_objet(index_obj)
        if self.objet_selectionne == "bouclier":
            self.bouclier_vie = self.joueur.objets_en_list[
                index_obj].durabilite
        if self.objet_selectionne == "phone":
            if self.phone_nombre > 1:
                self.joueur.objets_en_list[index_obj].nombre = 1
        self.joueur.objets_en_list[index_obj].nombre -= 1
        if self.joueur.objets_en_list[index_obj].nombre <= 0:
            self.joueur.objets.discard(
                self.index_objet(self.joueur.objets, index_obj))
            self.joueur.objets_en_list = list(self.joueur.objets)

    def utilisation_objet(self, index_obj):
        if self.objet_selectionne == "grenade":
            self.adversaire.vie -= 30
            grenade_sound.play()
            print("Tu as utilisé une grenade !")
        elif self.objet_selectionne == "piege":
            self.piege_active = True
            piege_sound.play()
            self.adversaire.vie -= self.joueur.objets_en_list[index_obj].degat
            self.joueur.objets_en_list[index_obj].durabilite -= 10
            self.piege_vie = self.joueur.objets_en_list[index_obj].durabilite
            print("Tu as mis ton piège !")
        elif self.objet_selectionne == "bouclier":
            self.joueur.objets_en_list[
                index_obj].durabilite -= self.adversaire.attaque
            self.tour_enemi_en_moins += 1
            bouclier_sound.play()
            print("Tu as mis ton bouclier !")
            if self.joueur.objets_en_list[index_obj].durabilite <= 0:
                print("Ton bouclier s'est cassé !")
                casse_sound.play()
        elif self.objet_selectionne == "soin":
            self.joueur.vie += 30
            soin_sound.play()
            print("Tu t'es soigné !")
        elif self.objet_selectionne == "phone":
            self.phone_active = True
            phone_sound.play()
            self.phone_nombre = self.joueur.objets_en_list[index_obj].nombre
            self.phone_ami_nb_soin = self.joueur.objets_en_list[
                index_obj].ami_nb_obj_soin
            self.phone_ami_soin = self.joueur.objets_en_list[
                index_obj].ami_obj_soin
            if self.joueur.objets_en_list[
                    index_obj].ami_degat < self.adversaire.defense:
                self.phone_ami_degat = self.joueur.objets_en_list[
                    index_obj].ami_degat - 4
            elif self.joueur.objets_en_list[
                    index_obj].ami_degat == self.adversaire.defense:
                self.phone_ami_degat = self.joueur.objets_en_list[
                    index_obj].ami_degat - 2
            else:
                self.phone_ami_degat = self.joueur.objets_en_list[
                    index_obj].ami_degat
            print("Tu as appelé un ami !")

        elif self.objet_selectionne == "fumigene":
            self.tour_enemi_en_moins += 2
            fumigene_sound.play()
            print("Tu as utilisé un fumigène !")

    def appel(self):
        if self.joueur.vie < 30 and self.phone_ami_nb_soin > 0:
            self.joueur.vie += self.phone_ami_soin
            print("Ton ami t'as soigné !")
            self.phone_ami_nb_soin -= 1
        else:
            self.adversaire.vie -= self.phone_ami_degat
            print(f"Ton ami a fait du dégat à {self.adversaire.nom}")

    def combat_tour_par_tour(self):

        # On regarde qui commence en premier
        if self.joueur.vitesse < self.adversaire.vitesse:
            a_qui_le_tour = "adversaire"
        elif self.joueur.vitesse == self.adversaire.vitesse:
            joueurs = ["joueur", "adversaire"]
            a_qui_le_tour = joueurs[randint(0, 1)]
        else:
            a_qui_le_tour = "joueur"

        # On initialise quelques variables
        nb_utilisation_objets = 0
        for objet in self.joueur.objets:
            if objet.nom == "piege":
                piege_degat = objet.degat
                break

        # On attend que le joueur fasse une action
        stop = False

        while not stop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop = True

                # On vérifie si le joueur ou l'adversaire a perdu
                if self.joueur.vie <= 0:
                    print("Vous avez perdu!")
                    failure.play()
                    self.victoire = False
                    self.afficher(screen)
                    stop = True
                elif self.adversaire.vie <= 0:
                    print("Vous avez gagné!")
                    success.play()
                    self.victoire = True
                    self.afficher(screen)
                    # Et on vérifie si le bouclier a toujours de la vie ,et si on avait un 2eme phone, pour le remettre dans l'inventaire
                    if self.bouclier_vie != None:
                        if self.bouclier_vie > 0 and not bouclier in self.joueur.objets:
                            self.joueur.objets.add(bouclier)
                            self.joueur.objets_en_list = list(
                                self.joueur.objets)
                    if self.phone_nombre != None:
                        if self.phone_nombre > 1:
                            self.joueur.objets.add(phone)
                            self.joueur.objets_en_list = list(
                                self.joueur.objets)
                            phone_objet = None
                            for objet in self.joueur.objets_en_list:
                                if objet.nom == "phone":
                                    phone_objet = objet
                                    break
                            if phone_objet is not None:
                                phone_objet.nombre = self.phone_nombre - 1
                    stop = True
                else:
                    if a_qui_le_tour == "adversaire":
                        if self.phone_active == True:
                            self.appel()
                        if self.adversaire.nb_heal != None and self.adversaire.vie <= 40 and self.adversaire.nb_heal <= 0:
                            self.adversaire.vie += self.adversaire.heal
                            self.adversaire.nb_heal -= 1
                            print(f"{self.adversaire.nom} s'est soigné !")
                        time.sleep(0.3)
                        if self.tour_enemi_en_moins == 0:
                            self.joueur.vie -= self.adversaire.attaque
                        else:
                            self.tour_enemi_en_moins -= 1
                        a_qui_le_tour = "joueur"
                        nb_utilisation_objets = 0
                        time.sleep(0.1)
                        if self.piege_active == True and self.piege_vie > 0:
                            self.adversaire.vie -= piege_degat
                            self.piege_vie -= 10
                            if self.piege_vie <= 0:
                                print("Ton piege s'est casse !")
                                casse_sound.play()
                                self.piege_active == False

                    if a_qui_le_tour == "joueur":
                        if self.bouton_selectionne == None:
                            clickable_area_attaque = pygame.Rect((50, 350),
                                                                 (128, 128))
                            clickable_area_objets = pygame.Rect((200, 350),
                                                                (128, 128))

                        if event.type == pygame.MOUSEBUTTONDOWN:  #quand je relache le bouton

                            # Si on clique sur le bouton d'attaque
                            if self.bouton_selectionne == None:
                                if clickable_area_attaque.collidepoint(
                                        event.pos):
                                    self.bouton_selectionne = "attaque"
                                    clickable_area_retour = pygame.Rect(
                                        (550, 400), (64, 64))
                                    self.afficher(screen)
                                    pygame.display.flip()

                        # Si on clique sur le bouton d'objet
                                if nb_utilisation_objets == 0:
                                    if self.bouclier_vie != None:
                                        if self.tour_enemi_en_moins == 0 and self.bouclier_vie > 0 and not bouclier in self.joueur.objets:
                                            self.joueur.objets.add(bouclier)
                                            self.joueur.objets_en_list = list(
                                                self.joueur.objets)
                                    if clickable_area_objets.collidepoint(
                                            event.pos):
                                        self.bouton_selectionne = "objets"
                                        clickable_area_retour = pygame.Rect(
                                            (550, 400), (64, 64))
                                        self.afficher(screen)
                                        pygame.display.flip()

                        # Quand on a cliqué sur l'attaque

                        if self.bouton_selectionne == "attaque":
                            stopattaque = False
                            while not stopattaque:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        stop = True

                                    clickable_area_retour = pygame.Rect(
                                        (550, 400), (64, 64))

                                    # Si on clique sur le bouton retour_image
                                    if event.type == pygame.MOUSEBUTTONDOWN:  #quand je relache le bouton
                                        if clickable_area_retour.collidepoint(
                                                event.pos):
                                            self.bouton_selectionne = None
                                            self.afficher(screen)
                                            pygame.display.flip()
                                            stopattaque = True

                                    #Si on clique sur une attaque ,(nb d'attaque :)1 minimum ,puis après il peut en avoir plus
                                        nombre_d_attaque = len(
                                            self.joueur.attaque)
                                        clickable_area_attaque1 = pygame.Rect(
                                            (50, 320), (128, 128))
                                        if nombre_d_attaque > 1:
                                            clickable_area_attaque2 = pygame.Rect(
                                                (200, 320), (128, 128))
                                        if nombre_d_attaque == 3:
                                            clickable_area_attaque3 = pygame.Rect(
                                                (350, 320), (128, 128))

                                        if clickable_area_attaque1.collidepoint(
                                                event.pos):
                                            stopattaque = True
                                            self.bouton_selectionne = None
                                            self.attaque_selectionnee = self.joueur.attaque[
                                                0].nom
                                            self.afficher(screen)
                                            self.attaquer(0)
                                            a_qui_le_tour = "adversaire"
                                            self.tour += 1

                                        if nombre_d_attaque > 1:
                                            if clickable_area_attaque2.collidepoint(
                                                    event.pos):
                                                stopattaque = True
                                                self.bouton_selectionne = None
                                                self.attaque_selectionnee = self.joueur.attaque[
                                                    1].nom
                                                self.afficher(screen)
                                                self.attaquer(1)
                                                a_qui_le_tour = "adversaire"
                                                self.tour += 1

                                        if nombre_d_attaque == 3:
                                            if clickable_area_attaque3.collidepoint(
                                                    event.pos):
                                                stopattaque = True
                                                self.bouton_selectionne = None
                                                self.attaque_selectionnee = self.joueur.attaque[
                                                    2].nom
                                                self.afficher(screen)
                                                self.attaquer(2)
                                                a_qui_le_tour = "adversaire"
                                                self.tour += 1

                        # Quand on a cliqué sur l'objet

                        if self.bouton_selectionne == "objets":
                            stopobjets = False
                            while not stopobjets:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        stop = True

                                    clickable_area_retour = pygame.Rect(
                                        (550, 400), (64, 64))

                                    # Si on clique sur le bouton retour_image
                                    if event.type == pygame.MOUSEBUTTONDOWN:  #quand je relache le bouton
                                        if clickable_area_retour.collidepoint(
                                                event.pos):
                                            self.bouton_selectionne = None
                                            self.afficher(screen)
                                            pygame.display.flip()
                                            stopobjets = True

                                    # Si on clique sur un objets ,s'ils existent
                                        nb_objets = len(self.joueur.objets)
                                        if nb_objets > 0:
                                            clickable_area_objet1 = pygame.Rect(
                                                (50, 300), (64, 64))
                                        if nb_objets > 1:
                                            clickable_area_objet2 = pygame.Rect(
                                                (200, 300), (64, 64))
                                        if nb_objets > 2:
                                            clickable_area_objet3 = pygame.Rect(
                                                (350, 300), (64, 64))
                                        if nb_objets > 3:
                                            clickable_area_objet4 = pygame.Rect(
                                                (50, 400), (64, 64))
                                        if nb_objets > 4:
                                            clickable_area_objet5 = pygame.Rect(
                                                (200, 400), (64, 64))
                                        if nb_objets > 5:
                                            clickable_area_objet6 = pygame.Rect(
                                                (350, 400), (64, 64))

                                        if nb_objets > 0:
                                            if clickable_area_objet1.collidepoint(
                                                    event.pos):
                                                stopobjets = True
                                                nb_utilisation_objets = 1
                                                self.selection_objet(0)
                                        if nb_objets > 1:
                                            if clickable_area_objet2.collidepoint(
                                                    event.pos):
                                                stopobjets = True
                                                nb_utilisation_objets = 1
                                                self.selection_objet(1)
                                        if nb_objets > 2:
                                            if clickable_area_objet3.collidepoint(
                                                    event.pos):
                                                stopobjets = True
                                                nb_utilisation_objets = 1
                                                self.selection_objet(2)
                                        if nb_objets > 3:
                                            if clickable_area_objet4.collidepoint(
                                                    event.pos):
                                                stopobjets = True
                                                nb_utilisation_objets = 1
                                                self.selection_objet(3)
                                        if nb_objets > 4:
                                            if clickable_area_objet5.collidepoint(
                                                    event.pos):
                                                stopobjets = True
                                                nb_utilisation_objets = 1
                                                self.selection_objet(4)
                                        if nb_objets > 5:
                                            if clickable_area_objet6.collidepoint(
                                                    event.pos):
                                                stopobjets = True
                                                nb_utilisation_objets = 1
                                                self.selection_objet(5)

            # Affichage du tour
            self.afficher(screen)

            # Rafraîchissement de l'écran
            pygame.display.flip()

            if self.victoire == False:
                time.sleep(10)
                pygame.quit()


class Adversaire:

    def __init__(self, name, img_adversaire, vie, vitesse, attaque, nb_heal,
                 heal, defense):
        self.nom = name
        self.image = pygame.image.load(img_adversaire).convert_alpha()
        self.image = pygame.transform.scale(self.image, (128, 200))
        self.vie = vie
        self.vitesse = vitesse
        self.attaque = attaque
        self.nb_heal = nb_heal
        self.heal = heal
        self.defense = defense


# Lancement du premier combat

zombie1 = Adversaire("Rodeur", "zombies/zombie1.png", 100, 10, randint(3, 5),
                     None, None, 0)

Tour1 = Combat(joueur, zombie1)
Tour1.combat_tour_par_tour()

phone.ami_nb_obj_soin = 2
time.sleep(3)

#Dialogue fin combat 1

stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    fond = pygame.image.load("GameBG.png").convert()
    fond = pygame.transform.scale(fond, (640, 480))

    screen.blit(fond, (0, 0))

    imagescientifique = pygame.image.load("scientifique.png").convert_alpha()
    imagescientifique = pygame.transform.scale(imagescientifique, (256, 280))

    screen.blit(imagescientifique, (200, 200))

    textintro1, rect = GAME_FONT.render(
        f"Bien joue {joueur.nom}! Nous pouvons continuer le chemin vers ",
        (0, 0, 0))
    textintro2, rect = GAME_FONT.render(
        f"{nom_ville} pour rependre le vaccin au monde entier !", (0, 0, 0))
    textnomscientifique, rect = GAME_FONT.render("Dr." + nomscientifique,
                                                 (0, 0, 0))

    screen.blit(textintro1, (20, 25))
    screen.blit(textintro2, (20, 50))
    screen.blit(textnomscientifique, (300, 225))

    image_continuer = pygame.image.load("boutoncontinuer.png").convert_alpha()
    image_continuer = pygame.transform.scale(image_continuer, (64, 64))

    clickable_area_continuer = pygame.Rect((525, 350), (64, 64))

    screen.blit(image_continuer, clickable_area_continuer)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  #quand je relache le bouton
            if clickable_area_continuer.collidepoint(event.pos):
                stop = True

    pygame.display.flip()

# Lancement du 2eme combat

zombie2 = Adversaire("Rodeur", "zombies/zombie2.png", 100, 30, randint(8, 12),
                     1, 10, 5)

if joueur.vie < 85:
    joueur.vie += 15

Tour1 = Combat(joueur, zombie2)
Tour1.combat_tour_par_tour()

time.sleep(1)

if soin not in joueur.objets:
    if soin.nombre == 0:
        soin.nombre += 1
    joueur.objets.add(soin)
    joueur.objets_en_list = list(joueur.objets)
else:
    soin.nombre += 1

print("Tu as obtenue 1 soin !")

time.sleep(2)

#Dialogue fin combat 2

stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    fond = pygame.image.load("GameBG.png").convert()
    fond = pygame.transform.scale(fond, (640, 480))

    screen.blit(fond, (0, 0))

    imagescientifique = pygame.image.load("scientifique.png").convert_alpha()
    imagescientifique = pygame.transform.scale(imagescientifique, (256, 280))

    screen.blit(imagescientifique, (200, 200))

    textintro1, rect = GAME_FONT.render(
        f"Bien joue {joueur.nom}! Mais faite gaffe un autre rodeur arrive !",
        (0, 0, 0))
    textnomscientifique, rect = GAME_FONT.render("Dr." + nomscientifique,
                                                 (0, 0, 0))

    screen.blit(textintro1, (20, 25))
    screen.blit(textnomscientifique, (300, 225))

    image_continuer = pygame.image.load("boutoncontinuer.png").convert_alpha()
    image_continuer = pygame.transform.scale(image_continuer, (64, 64))

    clickable_area_continuer = pygame.Rect((525, 350), (64, 64))

    screen.blit(image_continuer, clickable_area_continuer)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  #quand je relache le bouton
            if clickable_area_continuer.collidepoint(event.pos):
                stop = True

    pygame.display.flip()

# Lancement du 3eme combat

zombie3 = Adversaire("49.3", "zombies/zombie3.png", 100, 50, randint(15, 18),
                     1, 40, 8)

if joueur.vie < 85:
    joueur.vie += 15

Tour1 = Combat(joueur, zombie3)
Tour1.combat_tour_par_tour()

time.sleep(3)

#Dialogue fin combat 3


#Init une petite fonction hors de la boucle
def arme_posseder_ou_pas(liste_attaques):
    liste_armes = [fusil_assaut, fusil_precision, arbalete, pistolet_laser]
    liste_armes_non_posseder = []
    for attaque in liste_armes:
        if attaque in liste_attaques:
            pass
        else:
            liste_armes_non_posseder.append(attaque)
    return liste_armes_non_posseder


stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    fond = pygame.image.load("GameBG.png").convert()
    fond = pygame.transform.scale(fond, (640, 480))

    screen.blit(fond, (0, 0))

    imagescientifique = pygame.image.load("scientifique.png").convert_alpha()
    imagescientifique = pygame.transform.scale(imagescientifique, (256, 280))

    screen.blit(imagescientifique, (200, 200))

    textintro1, rect = GAME_FONT.render(
        f"Encore bien joue {joueur.nom}! Celui ci n'etait pas simple !",
        (0, 0, 0))
    textintro2, rect = GAME_FONT.render(
        "Tennez ,prennez une des armes que j'ai trouve sur le chemin :")
    textnomscientifique, rect = GAME_FONT.render("Dr." + nomscientifique,
                                                 (0, 0, 0))

    screen.blit(textintro1, (20, 25))
    screen.blit(textintro2, (20, 50))
    screen.blit(textnomscientifique, (300, 225))

    liste_armes_non_posseder = arme_posseder_ou_pas(joueur.attaque)

    for i, attaque in enumerate(liste_armes_non_posseder):
        image = pygame.image.load(
            f"armes/{liste_armes_non_posseder[i].nom}.png").convert_alpha()
        image = pygame.transform.scale(image, (128, 128))
        screen.blit(image, (150 + i * 150, 80))

    clickable_area_arme1 = pygame.Rect((150, 80), (128, 128))
    if len(liste_armes_non_posseder) > 1:
        clickable_area_arme2 = pygame.Rect((300, 80), (128, 128))
    if len(liste_armes_non_posseder) == 3:
        clickable_area_arme3 = pygame.Rect((450, 80), (128, 128))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  #quand je relache le bouton
            if clickable_area_arme1.collidepoint(event.pos):
                stop = True
                joueur.attaque.append(liste_armes_non_posseder[0])
                print(f"Tu as recus {liste_armes_non_posseder[0].nom}")
            if len(liste_armes_non_posseder) > 1:
                if clickable_area_arme2.collidepoint(event.pos):
                    stop = True
                    joueur.attaque.append(liste_armes_non_posseder[1])
                    print(f"Tu as recus {liste_armes_non_posseder[1].nom}")
            if len(liste_armes_non_posseder) == 3:
                if clickable_area_arme3.collidepoint(event.pos):
                    stop = True
                    joueur.attaque.append(liste_armes_non_posseder[2])
                    print(f"Tu as recus {liste_armes_non_posseder[2].nom}")

    pygame.display.flip()

# Lancement du 4eme combat

zombie4 = Adversaire("Armored Rodeur", "zombies/zombie4.png", 100, 70,
                     randint(4, 5), 2, 50, 25)

if joueur.vie < 75:
    joueur.vie += 25

Tour1 = Combat(joueur, zombie4)
Tour1.combat_tour_par_tour()

time.sleep(3)



"""
exemple PNJ

sanglier = PNJ("sanglier",45,2,89,15,23)
print(sanglier.pv)
"""