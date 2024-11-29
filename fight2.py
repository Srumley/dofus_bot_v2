import pyautogui as pg
import time
import pyperclip
import json

from time import sleep


def checkFight():


    f = pg.locateOnScreen('./images/fight/pret.jpg', confidence =0.8, region = (1332,940,100,36))

    if f == None:
        print('No fight')
        return
    else:
        fight()
        return

def invocation_sacrifiee(Coyeur1,Coyeur2,Coyeur3,Coyeur4):
    print('sacrifiee')
    sleep(2)
    if Coyeur1 != None:
        # clic sort sacrifiee
        pg.click(939, 942)
        sleep(2)
        pg.click(Coyeur1[0] - 45, Coyeur1[1] - 25)
        sleep(1)
        pg.moveTo(780, 942)
        sleep(1)
        sacrifiee_lancee = pg.locateOnScreen('./images/fight/sacrifiee_lancee.jpg', confidence=0.8, region=(911,911,45,45))
        if sacrifiee_lancee == None:
            sleep(1)
            pg.click(939, 942)
            sleep(2)
            pg.click(Coyeur1[0] + 45, Coyeur1[1] - 25)


    elif Coyeur2 != None:
        # clic sort sacrifiee
        pg.click(939, 942)
        sleep(2)
        pg.click(Coyeur2[0] + 45, Coyeur2[1] - 25)
        sleep(1)
        pg.moveTo(780, 942)
        sleep(1)
        sacrifiee_lancee = pg.locateOnScreen('./images/fight/sacrifiee_lancee.jpg', confidence=0.8,region=(911, 911, 45, 45))
        if sacrifiee_lancee == None:
            sleep(1)
            pg.click(939, 942)
            sleep(2)
            pg.click(Coyeur2[0] - 45, Coyeur2[1] - 25)


    elif Coyeur3 != None:
        # clock sort sacrifiee
        pg.click(939, 942)
        sleep(2)
        pg.click(Coyeur3[0] - 45, Coyeur3[1] + 25)
        sleep(1)
        pg.moveTo(780, 942)
        sleep(1)
        sacrifiee_lancee = pg.locateOnScreen('./images/fight/sacrifiee_lancee.jpg', confidence=0.8,region=(911, 911, 45, 45))
        if sacrifiee_lancee == None:
            sleep(2)
            pg.click(939, 942)
            sleep(2)
            pg.click(Coyeur3[0] + 45, Coyeur3[1] + 25)

    elif Coyeur4 != None:
        # clock sort sacrifiee
        pg.click(939, 942)
        sleep(2)
        pg.click(Coyeur4[0] + 45, Coyeur4[1] + 25)
        sleep(1)
        pg.moveTo(780, 942)
        sleep(1)
        sacrifiee_lancee = pg.locateOnScreen('./images/fight/sacrifiee_lancee.jpg', confidence=0.8,region=(911, 911, 45, 45))
        if sacrifiee_lancee == None:
            sleep(2)
            pg.click(939, 942)
            sleep(2)
            pg.click(Coyeur4[0] - 45, Coyeur4[1] + 25)

    sleep(1)


def fight():
    #click pret
    print("fight")
    sleep(1)
    pg.click(1378,952)
    fermer = pg.locateOnScreen('./images/fight/fermer.jpg', confidence=0.8, region=(813,589,200,60))
    sleep(2)

    Coyeur1 = pg.locateOnScreen('./images/coyeur_pano_bouftou/dos_gauche_rouge.jpg', confidence=0.8,
                                region=(367, 47, 1181, 842))
    Coyeur2 = pg.locateOnScreen('./images/coyeur_pano_bouftou/dos_droite_rouge.jpg', confidence=0.8,
                                region=(367, 47, 1181, 842))
    Coyeur3 = pg.locateOnScreen('./images/coyeur_pano_bouftou/face_gauche_rouge.jpg', confidence=0.8,
                                region=(367, 47, 1181, 842))
    Coyeur4 = pg.locateOnScreen('./images/coyeur_pano_bouftou/face_droite_rouge.jpg', confidence=0.8,
                                region=(367, 47, 1181, 842))

    while Coyeur1 == None and Coyeur2 == None and Coyeur3 == None and Coyeur4 == None:
        Coyeur1 = pg.locateOnScreen('./images/coyeur_pano_bouftou/dos_gauche_rouge.jpg', confidence=0.7,
                                    region=(367, 47, 1181, 842))
        Coyeur2 = pg.locateOnScreen('./images/coyeur_pano_bouftou/dos_droite_rouge.jpg', confidence=0.7,
                                    region=(367, 47, 1181, 842))
        Coyeur3 = pg.locateOnScreen('./images/coyeur_pano_bouftou/face_gauche_rouge.jpg', confidence=0.7,
                                    region=(367, 47, 1181, 842))
        Coyeur4 = pg.locateOnScreen('./images/coyeur_pano_bouftou/face_droite_rouge.jpg', confidence=0.7,
                                    region=(367, 47, 1181, 842))

    if Coyeur1 != None:
        Coyeur1 = pg.center(Coyeur1)

    if Coyeur2 != None:
        Coyeur2 = pg.center(Coyeur2)

    if Coyeur3 != None:
        Coyeur3 = pg.center(Coyeur3)

    if Coyeur4 != None:
        Coyeur4 = pg.center(Coyeur4)



    #invoc sacrifiee
    invocation_sacrifiee(Coyeur1,Coyeur2,Coyeur3,Coyeur4)
    round_before_spell = 6

    while fermer == None:
        #click passer tour , a verifier
        if round_before_spell == 0:
            invocation_sacrifiee(Coyeur1,Coyeur2,Coyeur3,Coyeur4)
            round_before_spell = 6
        else:
            print('passe tour')
            pg.click(1378, 952)
            round_before_spell = round_before_spell - 1
            sleep(6)
            fermer = pg.locateOnScreen('./images/fight/fermer.jpg', confidence=0.8, region=(813, 589, 200, 60))

    #click in cas of level up
    sleep(1)
    pg.click(961,776)
    sleep(1)
    #close summary fight
    pg.click(916,616)


while True:
    checkFight()