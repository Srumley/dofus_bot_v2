import pyautogui as pg
import time
import pyperclip
import json

from time import sleep
def fight(f):
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
    print('ici', Coyeur1)
    print('la',Coyeur1==None)
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
    if Coyeur1 != None:
        #clic sort sacrifiee
        pg.click(939,942)
        sleep(1)
        pg.click(Coyeur1[0]-46,Coyeur1[1]-22)
        sleep(1)
    elif Coyeur2 != None:
        # clic sort sacrifiee
        pg.click(939, 942)
        sleep(1)
        pg.click(Coyeur2[0] + 46, Coyeur2[1] - 22)
        sleep(1)
    elif Coyeur3 != None:
        # clic sort sacrifiee
        pg.click(939, 942)
        sleep(1)
        pg.click(Coyeur3[0] - 46, Coyeur3[1] + 22)
        sleep(1)
    elif Coyeur4 != None:
        # clic sort sacrifiee
        pg.click(939, 942)
        sleep(1)
        pg.click(Coyeur4[0] + 46, Coyeur4[1] + 22)
        sleep(1)


    while fermer == None:
        #click passer tour , a verifier
        print('passe tour')
        pg.click(1378, 952)
        sleep(6)
        fermer = pg.locateOnScreen('./images/fight/fermer.jpg', confidence=0.8, region=(813, 589, 200, 60))

    #close summary fight
    pg.click(916,616)




def checkFight():
    #peut etre remove le try

    f = pg.locateOnScreen('./images/fight/pret.jpg', confidence =0.8, region = (1332,940,100,36))

    if f == None:
        print('try: No fight')
        return
    else:
        fight(f)
        return


#while True:
#    checkFight()