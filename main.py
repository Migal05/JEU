from random import randint
import pygame
from pygame.locals import *
import pygame.freetype

#Base
pygame.init()
pygame.mixer.music.load("MainMenu.mp3")
pygame.mixer.music.play(0)
GAME_FONT = pygame.freetype.Font("FoundationTwo.ttf", 15)
GAME_FONTFONT = pygame.font.Font(None, 24)
screen = pygame.display.set_mode((400, 300), FULLSCREEN)
color = pygame.Color(0, 0, 255, 255)

#Pseudo
user_name = ''
fond = pygame.image.load("entre.png").convert()
input_rect = pygame.Rect(200, 200, 140, 32)
    




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

    
    text_surface = GAME_FONTFONT.render(user_name, True, (255, 255, 255, 25))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(100, text_surface.get_width() + 10)
    image_start = pygame.image.load("start_continue.png").convert_alpha()
    
    text_surface2, rect = GAME_FONT.render(
        "Bienvenue jeune heros dans (inserer le nom du jeu),"
        "un jeu de role numerique ou vous pourrez, aux files des choix, vivre une aventure unique"
        "Je serai votre maitre du jeu, Hans Der Schwartz.", (0, 0, 0))
    screen.blit(text_surface2, (40, 25))
    clickable_area_start = pygame.Rect((300, 100), (200, 163))
    screen.blit(image_start, clickable_area_start)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  #quand je relache le bouton
            if clickable_area_start.collidepoint(event.pos):
                stop = True
    pygame.display.update()




stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
    
    screen.fill(pygame.Color('white'))
    texteintro ,rect = GAME_FONT.render("Parfait,bienvenue " + user_name +", maintenant choisissez votre sexe", (0, 0, 0))
    screen.blit(texteintro, (0,0))
    image_homme = pygame.image.load("Homme.png").convert_alpha()
    image_homme = pygame.transform.scale(image_homme, (128, 128))
    image_femme = pygame.image.load("Femme.png").convert_alpha()
    image_femme = pygame.transform.scale(image_femme, (128, 128))
    Stopfemme , Stophomme = False , False 
    fond = pygame.image.load("entre.png").convert()
    clickable_area_homme = pygame.Rect((100, 100), (100, 100))
    clickable_area_femme = pygame.Rect((300, 100), (100, 100))
    screen.blit(image_homme, clickable_area_homme)
    screen.blit(image_femme, clickable_area_femme)
    if clickable_area_femme.collidepoint(pygame.mouse.get_pos()):
        text ,rect = GAME_FONT.render("CE role est bi1",(0,0,0))
        screen.blit(text, (5, 20))
        pygame.display.update()
        
        
        
    elif clickable_area_homme.collidepoint(pygame.mouse.get_pos()):
        text ,rect = GAME_FONT.render("CE role est encore bi1",(0,0,0))
        screen.blit(text, (5, 20))
        pygame.display.update()
    

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  #quand je relache le bouton
            if clickable_area_homme.collidepoint(event.pos):
                sexe_perso = "homme"
                stop = True
            elif clickable_area_femme.collidepoint(event.pos):
                sexe_perso = "femme"
                stop = True

    pygame.display.flip()

print("Très bien, maintenant vous allez choisir votre classe")




def descritif_score_des():
    print(
        "6 ou moins : Handicapant. Cet attribut est si mauvais qu'il vous gêne énormément dans votre mode de vie."
        "7 : Faible. Vos lacunes sont visibles de tous ceux qui vous rencontrent."
        "8 ou 9 : Sous la moyenne. Ces scores sont limitants mais dans la norme humaine."
        "10: Moyen. La plupart des personnes dans le monde ont une vie satisfaisante avec un score de 10."
        "11 ou 12 : Au-dessus de la moyenne. Ces scores sont supérieurs, mais dans la norme humaine."
        "13 ou 14 : Exceptionnel. De tels attributs sont immédiatement apparents - des muscles saillants, une grâce féline, un discours astucieux ou une vitalité éclatante- à ceux qui vous rencontrent."
        "15 ou plus : Incroyable. Un tel niveau attire constamment commentaires de la part des autres et guident vos choix de vie"
    )


def guerrier():
    print(
        "PV = (à définir) "
        "facilité : armures lourde, arme de CàC"
        "capacité physique : force 14~20 , éloquence 9~20, dexterité/agilité 9~20, vitalité/énergie 13~20, IQ 12~20 , sex appeal 0~20(peux remonter l'éloquence)"
    )


def archer():
    print(
        "PV = (à définir) "
        "facilité : armures légère, arme légère, arme de jet, "
        "cpacité physique : force 10~20 , éloquence 13~20, dexterité/agilité 14~20, vitalité/énergie 14~20, IQ 13~20, sex appeal 0~20(peux remonter l'éloquence)"
    )


def assassin():
    print(
        "PV = (à définir) "
        "facilité : armures légère, arme légère, discrétion"
        "cpacité physique : force 9~20 , éloquence 13~20, dexterité/agilité 15~20, vitalité/énergie 14~20, IQ 14~20, sex appeal 0~20(peux remonter l'éloquence)"
    )


def Shaq():
    print(
        "PV = (à définir) "
        "facilité : armures lourde, arme lourde,"
        "cpacité physique : force 16~20 , éloquence 7~20, dexterité/agilité 7~20, vitalité/énergie 14~20, IQ 11~20, sex appeal 0~20(peux remonter l'éloquence)"
    )


classe = ""
while classe == "":
    print(guerrier(), archer(), assassin(), Shaq(), descritif_score_des())
    if sexe_perso == "femme":
        loop = str(
            input(
                "Choisissez votre classe : guerrière, archère, assassin ou Shaq (votre choix change vos caractéristiques): "
            ))
        if loop not in [
                "guerrière", "archère", "assassin", "shaq", "Guerrière",
                "Archère", "Assassin", "Shaq"
        ]:
            print("Choix incorrect !")
    elif sexe_perso == "homme":
        loop = str(
            input(
                "Choisissez votre classe : guerrier, archer, assassin ou Shaq (votre choix change vos caractéristiques): "
            ))
        if loop not in [
                "guerrier", "archer", "assassin", "shaq", "Guerrier", "Archer",
                "Assassin", "Shaq"
        ]:
            print("Choix incorrect !")
    else:
        break
    classe = loop

for loop in range(1):
    if classe == "guerrier":
        classe_perso = guerrier()
    elif classe == "archer":
        classe_perso = archer()
    elif classe == "assassin":
        classe_perso = assassin()
    elif classe == "Shaq" or classe == "shaq":
        classe_perso = Shaq()
    elif classe == "guerrière":
        classe_perso = guerrier()
    elif classe == "archère":
        classe_perso = archer()

#objet
while 1:
    obj1 = str(
        input(
            "Choisissez 3 objet pour débuter votre aventure : objet1, objet2, objet3, objet4, objet5, objet6, "
            "objet7, objet8, objet9, objet10, objet11, objet12, objet13 : "))
    if obj1 not in [
            "objet1", "objet2", "objet3", "objet4", "objet5", "objet6",
            "objet7", "objet8", "objet9", "objet10", "objet11", "objet12",
            "objet13"
    ]:
        print("Choix incorrect !")
    else:
        break
objet_start1 = obj1

while 1:
    obj2 = str(
        input(
            "Choisissez 3 objet pour débuter votre aventure : objet1, objet2, objet3, objet4, objet5, objet6, "
            "objet7, objet8, objet9, objet10, objet11, objet12, objet13 : "))
    if obj2 not in [
            "objet1", "objet2", "objet3", "objet4", "objet5", "objet6",
            "objet7", "objet8", "objet9", "objet10", "objet11", "objet12",
            "objet13"
    ]:
        print("Choix incorrect !")
    elif obj2 == objet_start1:
        print("Choix incorrect !")
    else:
        break
objet_start2 = obj2

while 1:
    obj3 = str(
        input(
            "Choisissez 3 objet pour débuter votre aventure : objet1, objet2, objet3, objet4, objet5, objet6, "
            "objet7, objet8, objet9, objet10, objet11, objet12, objet13 : "))
    if obj3 not in [
            "objet1", "objet2", "objet3", "objet4", "objet5", "objet6",
            "objet7", "objet8", "objet9", "objet10", "objet11", "objet12",
            "objet13"
    ]:
        print("Choix incorrect !")
    elif obj3 == objet_start2:
        print("Choix incorrect !")
    elif obj3 == objet_start1:
        print("Choix incorrect !")
    else:
        break
objet_start3 = obj3

#classe 2

if classe_perso == guerrier():
    force = randint(12, 20)
    eloquence = randint(7, 20)
    dexterite = randint(7, 20)
    vitalite = randint(11, 20)
    discretion = randint(10, 20)
    IQ = randint(10, 20)
    sex_appeal = randint(0, 20)
elif classe_perso == archer():
    force = randint(8, 20)
    eloquence = randint(11, 20)
    dexterite = randint(13, 20)
    vitalite = randint(12, 20)
    discretion = randint(11, 20)
    IQ = randint(12, 20)
    sex_appeal = randint(0, 20)
elif classe_perso == assassin():
    force = randint(7, 20)
    eloquence = randint(11, 20)
    dexterite = randint(13, 20)
    vitalite = randint(12, 20)
    discretion = randint(13, 20)
    IQ = randint(12, 20)
    sex_appeal = randint(0, 20)
elif classe_perso == Shaq():
    force = randint(14, 20)
    eloquence = randint(7, 20)
    dexterite = randint(5, 20)
    vitalite = randint(14, 20)
    discretion = randint(7, 20)
    IQ = randint(11, 20)
    sex_appeal = randint(0, 20)

if sex_appeal <= eloquence:
    s2 = print("ce qui n'augmente pas votre eloquence")
elif sex_appeal + 5 <= eloquence:
    s2 = print("sf")
else:
    s2 = print("+")
print(sexe_perso)
print(name_perso)
print(classe, "votre force est de ", force, "votre eloquence est de ",
      eloquence, "votre dexterite est de ", dexterite,
      "votre discrétion est de ", discretion, "votre vitalite est de ",
      vitalite, "votre IQ est de ", IQ, "votre sex_appeal est de ", sex_appeal,
      s2)