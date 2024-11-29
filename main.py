import pyautogui as pg
import time
import pyperclip
import json

from time import sleep

# import keyboard
# import time
# import random
# import win32api,win32con
w, h = pg.size()
print("running bot")


#acitvate chat guilde, activat guilde chat only, activate object instead of sorts
largeur = 1920
hauteur = 1080

#convert
def x(x):
    x = largeur/1920*x
    return int(x)
def y(y):
    y = hauteur/1080*y
    return int(y)

left = [x(200),y(500)]
right = [x(1700),y(500)]
up = [x(900),y(31)]
down = [x(1050), y(903)]

def checkBle():
    try:
        c = pg.locateOnScreen('./images/cereales/ble.jpg', confidence =0.7, region = (x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/ble1.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/ble2.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/ble3.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/ble4.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        c = pg.center(c)
        pg.moveTo(c[0], c[1])
        pg.click()
        #time.sleep(1)
        return True
    except:
        print('Pas de blé trouvé')
        return False

    #time.sleep(0.5)

def checkOrge():
    try:
        c = pg.locateOnScreen('./images/cereales/orge.jpg', confidence =0.8, region = (x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/orge1.jpg', confidence=0.8, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/orge2.jpg', confidence=0.8, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/orge3.jpg', confidence=0.8, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/orge4.jpg', confidence=0.8, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/orge5.jpg', confidence=0.8, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/orge6.jpg', confidence=0.8, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/orge7.jpg', confidence=0.8, region=(x(367),y(47),x(1181),y(842)))
        c = pg.center(c)
        pg.moveTo(c[0], c[1])
        pg.click()
        #time.sleep(1)
        return True
    except:
        #print('Pas de orge trouvé')
        return False

    #time.sleep(0.5)

def checkAvoine():
    try:
        '''
        c = pg.locateOnScreen('./images/cereales/avoine.jpg', confidence =0.7, region = (367,47,1181,842))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/avoine1.jpg', confidence=0.7, region=(367, 47, 1181, 842))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/avoine2.jpg', confidence=0.7, region=(367, 47, 1181, 842))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/avoine3.jpg', confidence=0.7, region=(367, 47, 1181, 842))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/avoine4.jpg', confidence=0.7, region=(367, 47, 1181, 842))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/avoine5.jpg', confidence=0.7, region=(367, 47, 1181, 842))
        
        if c == None:
            c = pg.locateOnScreen('./images/cereales/avoine6.jpg', confidence=0.6, region=(367, 47, 1181, 842))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/avoine7.jpg', confidence=0.6, region=(367, 47, 1181, 842))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/avoine8.jpg', confidence=0.6, region=(367, 47, 1181, 842))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/avoine9.jpg', confidence=0.6, region=(367, 47, 1181, 842))
        '''
        c = pg.locateOnScreen('./images/cereales/avoine9.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/avoine10.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/avoine11.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/avoine12.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/avoine13.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/avoine14.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/avoine15.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        c = pg.center(c)
        pg.moveTo(c[0], c[1])
        pg.click()
        #time.sleep(1)
        return True
    except:
        #print('Pas de avoine trouvé')
        return False

    #time.sleep(0.5)

def checkHoublon():
    try:
        c = pg.locateOnScreen('./images/cereales/houblon.jpg', confidence =0.7, region = (x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/houblon1.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/houblon2.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/houblon3.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/houblon4.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        c = pg.center(c)
        pg.moveTo(c[0], c[1])
        pg.click()
        #time.sleep(1)
        return True
    except:
        #print('Pas de houblon trouvé')
        return False

def checkLin():
    try:
        c = pg.locateOnScreen('./images/cereales/lin.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/lin1.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/lin2.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/lin3.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/lin4.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/lin5.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/lin6.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))

        c = pg.center(c)
        pg.moveTo(c[0], c[1])
        pg.click()
        # time.sleep(1)
        return True
    except:
        # print('Pas de lin trouvé')
        return False

    #time.sleep(0.5)

def checkOrtie():
    try:
        c = pg.locateOnScreen('./images/ortie.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/ortie1.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))

        c = pg.center(c)
        pg.moveTo(c[0], c[1])
        pg.click()
        # time.sleep(1)
        return True
    except:
        # print('Pas de ortie trouvé')
        return False

    #time.sleep(0.5)

def checkFrene():
    try:
        c = pg.locateOnScreen('./images/frene.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/frene1.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))

        c = pg.center(c)
        pg.moveTo(c[0], c[1])
        pg.click()
        # time.sleep(1)
        return True
    except:
        # print('Pas de frene trouvé')
        return False

    #time.sleep(0.5)

def checkSeigle():
    try:
        c = pg.locateOnScreen('./images/cereales/seigle.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/seigle1.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))

        c = pg.center(c)
        pg.moveTo(c[0], c[1])
        pg.click()
        # time.sleep(1)
        return True
    except:
        # print('Pas de seigle trouvé')
        return False

def checkMalt():
    try:
        c = pg.locateOnScreen('./images/cereales/malt.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/malt1.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))
        if c == None:
            c = pg.locateOnScreen('./images/cereales/malt2.jpg', confidence=0.7, region=(x(367),y(47),x(1181),y(842)))

        c = pg.center(c)
        pg.moveTo(c[0], c[1])
        pg.click()
        # time.sleep(1)
        return True
    except:
        # print('Pas de malt trouvé')
        return False


def changeMap(map_target,s):
    #copy position
    pg.click(555, 1008)
    pg.write("%pos%")
    pg.press('enter')
    # attention, acitvé le chat de guilde
    pg.click(575, 975)
    pg.dragTo(481, 975, 1, button='left')
    pg.keyDown('ctrl')
    pg.press('c')
    pg.keyUp('ctrl')
    map_actual = pyperclip.paste()
    map_actual = map_actual.strip()
    print(map_target)
    print(map_actual)
    #convert string to list
    map_actual = json.loads(map_actual)

    difference_position = [-1,-1]
    difference_position[0] = map_target[0] - map_actual[0]
    difference_position[1] = map_target[1] - map_actual[1]

    while difference_position[0]!=0 or difference_position[1]!=0:
        print(difference_position)

        if difference_position[0] > 0:
            pg.click(right)
            difference_position[0] = difference_position[0]-1
            black_screen = pg.locateOnScreen('./images/change_map.jpg', confidence=0.9, region=(x(932),y(788), x(279), y(215)))
            print(black_screen)
            while black_screen == None:
                black_screen = pg.locateOnScreen('./images/change_map.jpg', confidence=0.9, region=(x(932),y(788), x(279), y(215)))
            sleep(1)

        if difference_position[0] < 0:
            pg.click(left)
            difference_position[0] = difference_position[0]+1
            black_screen = pg.locateOnScreen('./images/change_map.jpg', confidence=0.9, region=(x(932),y(788), x(279), y(215)))
            print(black_screen)
            while black_screen == None:
                black_screen = pg.locateOnScreen('./images/change_map.jpg', confidence=0.9, region=(x(932),y(788), x(279), y(215)))
            sleep(1)

        if difference_position[1] > 0:
            pg.click(down)
            difference_position[1] = difference_position[1]-1
            black_screen = pg.locateOnScreen('./images/change_map.jpg', confidence=0.9, region=(x(932),y(788), x(279), y(215)))
            print(black_screen)
            while black_screen == None:
                black_screen = pg.locateOnScreen('./images/change_map.jpg', confidence=0.9, region=(x(932),y(788), x(279), y(215)))
            sleep(1)

        if difference_position[1] < 0:
            pg.click(up)
            difference_position[1] = difference_position[1]+1
            black_screen = pg.locateOnScreen('./images/change_map.jpg', confidence=0.9, region=(x(932),y(788), x(279), y(215)))
            print(black_screen)
            while black_screen == None:
                black_screen = pg.locateOnScreen('./images/change_map.jpg', confidence=0.9, region=(x(932),y(788), x(279), y(215)))
            sleep(1)


    print("you are in target map")


def cuttingProcess():
    ble = False
    orge = False
    avoine = False
    houblon = True
    lin = True
    seigle = False
    malt = False
    ortie = True
    frene = False

    while ble:
        ble = checkBle()
        #if ble == False:
            #orge = checkOrge()
        # wait during cutting
        if ble:
            print('coupe')
            sleep(4)
        sleep(0.5)
        checkFight()
        full = checkFullPod()
        if full == True:
            return
        print("blé:", ble)

    while orge:
        orge = checkOrge()
        # wait during cutting
        if orge:
            print('coupe')
            sleep(4)
        sleep(0.5)
        checkFight()
        full = checkFullPod()
        if full == True:
            return
        print("orge:", orge)

    while avoine:
        avoine = checkAvoine()
        # wait during cutting
        if avoine:
            print('coupe')
            sleep(4)
        sleep(0.5)
        checkFight()
        full = checkFullPod()
        if full == True:
            return
        print("avoine:", avoine)

    while houblon:
        houblon = checkHoublon()
        # wait during cutting
        if houblon:
            print('coupe')
            sleep(4)
        #sleep(0.5)
        checkFight()
        full = checkFullPod()
        if full == True:
            return
        print("houblon:", houblon)

    while lin:
        lin = checkLin()
        # wait during cutting
        if lin:
            print('coupe')
            sleep(4)
        #sleep(0.5)
        checkFight()
        full = checkFullPod()
        if full == True:
            return
        print("lin:", lin)

    while seigle:
        seigle = checkSeigle()
        # wait during cutting
        if seigle:
            print('coupe')
            sleep(4)
        sleep(0.5)
        checkFight()
        full = checkFullPod()
        if full == True:
            return
        print("seigle:", seigle)

    while malt:
        malt = checkMalt()
        # wait during cutting
        if malt:
            print('coupe')
            sleep(4)
        sleep(0.5)
        checkFight()
        full = checkFullPod()
        if full == True:
            return
        print("malt:", malt)

    while ortie:
        ortie = checkOrtie()
        # wait during cutting
        if ortie:
            print('coupe')
            sleep(6)
        #sleep(0.5)
        checkFight()
        full = checkFullPod()
        if full == True:
            return
        print("ortie:", ortie)

    while frene:
        frene = checkFrene()
        # wait during cutting
        if frene:
            print('coupe')
            sleep(4)
        sleep(0.5)
        checkFight()
        full = checkFullPod()
        if full == True:
            return
        print("frene:", frene)
    #peut etre supprimer ici
    checkFight()


def go_bank_astrub():

    changeMap([4, -18])
    #sleep(1)
    sleep(3)
    # entrer bank
    pg.click(x(1130), y(372))
    #sleep(6)
    sleep(10)
    # clic pnj
    pg.click(x(1111), y(459))
    #sleep(1)
    sleep(3)
    # answer pnj
    pg.click(x(913), y(754))
    #sleep(2)
    sleep(5)
    # clic arrow inventaire
    pg.click(x(1261), y(153))
    #sleep(1)
    sleep(3)
    # clic tout les objets
    pg.click(x(1362), y(166))
    #sleep(1)
    sleep(3)
    # close windows
    pg.click(x(1552), y(117))
    #sleep(1)
    sleep(3)
    # go out of bank
    pg.click(x(716), y(696))
    #sleep(2)
    sleep(6)
    changeMap([4, -24])

def go_bank_amakna():

    changeMap([2, -2],8)
    sleep(1)
    # entrer bank
    pg.click(968, 296)
    sleep(4)
    # clic pnj
    pg.click(1073,478)
    sleep(1)
    # answer pnj
    pg.click(914,753)
    sleep(2)
    # clic arrow inventaire
    pg.click(1261, 153)
    sleep(1)
    # clic tout les objets
    pg.click(1362, 166)
    sleep(1)
    # close windows
    pg.click(1552, 117)
    sleep(1)
    # go out of bank
    pg.click(761,675)
    sleep(2)
    changeMap([3, 5],8)

def checkFullPod():
    #full_pod = pg.locateOnScreen('./images/full_pod.jpg', confidence =0.9, region = (1280,1011,23,16))
    full_pod = pg.locateOnScreen('./images/fullpod.jpg', confidence =0.9, region = (x(1265),y(1002),x(31),y(26)))
    print(full_pod)
    if full_pod == None:
        return False
    else:
        print('full_pod')
        #go bank astrub
        #go_bank_astrub()
        go_bank_amakna()
        return True


def checkFight():
    #peut etre remove le try

    f = pg.locateOnScreen('./images/fight/pret.jpg', confidence =0.8, region = (x(1332),y(940),x(100),y(36)))

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
        sacrifiee_lancee = pg.locateOnScreen('./images/fight/sacrifiee_lancee.jpg', confidence=0.8, region=(x(911),y(911),x(45),y(45)))
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
        sacrifiee_lancee = pg.locateOnScreen('./images/fight/sacrifiee_lancee.jpg', confidence=0.8,region=(x(911),y(911),x(45),y(45)))
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
        sacrifiee_lancee = pg.locateOnScreen('./images/fight/sacrifiee_lancee.jpg', confidence=0.8,region=(x(911),y(911),x(45),y(45)))
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
        sacrifiee_lancee = pg.locateOnScreen('./images/fight/sacrifiee_lancee.jpg', confidence=0.8,region=(x(911),y(911),x(45),y(45)))
        if sacrifiee_lancee == None:
            sleep(2)
            pg.click(939, 942)
            sleep(2)
            pg.click(Coyeur4[0] - 45, Coyeur4[1] + 25)

    sleep(1)


def fight():
    print("fight")
    #click pret
    sleep(1)
    pg.click(1378,952)
    fermer = pg.locateOnScreen('./images/fight/fermer.jpg', confidence=0.8, region=(x(813),y(589),x(200),y(60)))
    sleep(2)

    Coyeur1 = pg.locateOnScreen('./images/coyeur_pano_bouftou/dos_gauche_rouge.jpg', confidence=0.8,
                                region=(x(367),y(47),x(1181),y(842)))
    Coyeur2 = pg.locateOnScreen('./images/coyeur_pano_bouftou/dos_droite_rouge.jpg', confidence=0.8,
                                region=(x(367),y(47),x(1181),y(842)))
    Coyeur3 = pg.locateOnScreen('./images/coyeur_pano_bouftou/face_gauche_rouge.jpg', confidence=0.8,
                                region=(x(367),y(47),x(1181),y(842)))
    Coyeur4 = pg.locateOnScreen('./images/coyeur_pano_bouftou/face_droite_rouge.jpg', confidence=0.8,
                                region=(x(367),y(47),x(1181),y(842)))

    while Coyeur1 == None and Coyeur2 == None and Coyeur3 == None and Coyeur4 == None:
        Coyeur1 = pg.locateOnScreen('./images/coyeur_pano_bouftou/dos_gauche_rouge.jpg', confidence=0.8,
                                    region=(x(367),y(47),x(1181),y(842)))
        Coyeur2 = pg.locateOnScreen('./images/coyeur_pano_bouftou/dos_droite_rouge.jpg', confidence=0.8,
                                    region=(x(367),y(47),x(1181),y(842)))
        Coyeur3 = pg.locateOnScreen('./images/coyeur_pano_bouftou/face_gauche_rouge.jpg', confidence=0.8,
                                    region=(x(367),y(47),x(1181),y(842)))
        Coyeur4 = pg.locateOnScreen('./images/coyeur_pano_bouftou/face_droite_rouge.jpg', confidence=0.8,
                                    region=(x(367),y(47),x(1181),y(842)))

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
    round_before_spell = 7

    while fermer == None:
        #click passer tour , a verifier
        if round_before_spell == 0:
            invocation_sacrifiee(Coyeur1,Coyeur2,Coyeur3,Coyeur4)
            round_before_spell = 7
        else:
            print('passe tour')
            pg.click(1378, 952)
            round_before_spell = round_before_spell - 1
            sleep(6)
            fermer = pg.locateOnScreen('./images/fight/fermer.jpg', confidence=0.8, region=(x(813), y(589), x(200), y(60)))

    #click in cas of level up
    sleep(1)
    pg.click(961,776)
    sleep(1)
    #close summary fight
    pg.click(916,616)



def tour_astrub():
    sleep(2)
    changeMap([4, -24],8)

    sleep(2)
    changeMap([3, -31],6)
    sleep(2)
    cuttingProcess()

    changeMap([3, -28],6)
    sleep(2)
    cuttingProcess()

    changeMap([3, -26],6)
    sleep(2)
    cuttingProcess()

    changeMap([3, -24],6)
    sleep(2)
    cuttingProcess()

    changeMap([3, -23],6)
    sleep(2)
    cuttingProcess()

    changeMap([3, -22],6)
    sleep(2)
    cuttingProcess()

    changeMap([5, -22],6)
    sleep(2)
    cuttingProcess()

    changeMap([6, -22],6)
    sleep(2)
    cuttingProcess()

    changeMap([4, -23],6)
    sleep(2)
    cuttingProcess()
    sleep(1)

    changeMap([4, -27],6)
    sleep(2)
    cuttingProcess()
    sleep(1)

    changeMap([4, -28],6)
    sleep(2)
    cuttingProcess()
    sleep(1)

    changeMap([4, -29],6)
    sleep(2)
    cuttingProcess()
    sleep(1)

    changeMap([4, -30],6)
    sleep(2)
    cuttingProcess()
    sleep(1)

    changeMap([6, -29],6)
    sleep(2)
    cuttingProcess()
    sleep(1)

    changeMap([6, -28],6)
    sleep(2)
    cuttingProcess()
    sleep(1)

    changeMap([7, -27],6)
    sleep(2)
    cuttingProcess()
    sleep(1)

    changeMap([5, -27],6)
    sleep(2)
    cuttingProcess()
    sleep(1)


def tour_amakna_orge_avoine_houblon():

    #sleep(2)
    #changeMap([3, 5])

    sleep(2)
    changeMap([7, 4],8)
    sleep(2)
    cuttingProcess()
    sleep(1)

    #changeMap([11, 6],6)
    #sleep(2)
    #cuttingProcess()
    #sleep(1)

    changeMap([9, 6],6)
    sleep(2)
    cuttingProcess()
    sleep(1)

    changeMap([9, 7],6)
    sleep(2)
    cuttingProcess()
    sleep(1)

    changeMap([9, 9], 6)
    sleep(2)
    cuttingProcess()
    sleep(1)


    changeMap([8, 8],6)
    sleep(2)
    cuttingProcess()
    sleep(1)


    changeMap([7, 9], 6)
    sleep(2)
    cuttingProcess()
    sleep(1)

    changeMap([7, 8], 6)
    sleep(2)
    cuttingProcess()
    sleep(1)


    changeMap([6, 8], 6)
    sleep(2)
    cuttingProcess()
    sleep(1)

    changeMap([7,7], 6)
    sleep(2)
    cuttingProcess()
    sleep(1)

sleep(5)
nb_tour = 0
while nb_tour<50:

    tour_astrub()
    #tour_amakna_orge_avoine_houblon()

    print("end of the round nb:", nb_tour)
    nb_tour = nb_tour+1
    sleep(5)

