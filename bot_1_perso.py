import pyautogui as pg
import time
import pyperclip
import json
import time
from time import sleep
import numpy as np

# import keyboard
# import time
# import random
# import win32api,win32con
w, h = pg.size()
print("running bot")

# acitvate chat guilde, activat guilde chat only, activate object instead of sorts
largeur = 1920
hauteur = 1080

class Player:
    def __init__(self, name, pos_init, init_idx_tour, name_tour):
        self.name = name

        #self.collecting = False
        self.difference_position = [0,0]
        self.in_target_map = False
        self.full_pod=False
        self.target_map = [0,0]
        self.actuel_map = pos_init

        self.is_cutting = False

        self.idx_tour = init_idx_tour
        #self.tour_astrub =  [[4, -24],[5,-24],[3, -31],[3, -28],[3, -26],[3, -24],[3, -23],[3, -22],[5, -22],[6, -22],
        #                     [4, -23],[4, -27],[4, -28],[4, -29],[4, -30],[6, -29],[6, -28],[7, -27],[5, -27]]
        self.name_tour = name_tour
        self.tour_astrub = [[4,-26],[5,-26]]
        self.tour_astrub_ble1 = [[6,-30],[6,-29],[6,-28],[4,-29],[4,-27],[3,-26]]#[4,-30] au debut
        self.tour_astrub_ble2 = [[5, -25], [7, -25], [7, -23], [9, -23], [7, -21], [5, -22],[3,-22],[3,-23]]
        #self.tour_astrub_ble2 = [[4, -30], [6, -30], [6, -29], [6, -28], [4, -29], [4, -27], [3, -26]]

        self.timer_begin_cutting = 0
        self.timer_begin_moving = 0


        self.cut_ble = False
        self.cut_orge = False
        self.cut_avoine = False
        self.cut_houblon = True
        self.cut_lin = False
        self.cut_seigle = False
        self.cut_malt = False
        self.cut_ortie = False
        self.cut_frene = False
        self.cut_list = [self.cut_ble,self.cut_orge,self.cut_avoine,self.cut_houblon,self.cut_lin,self.cut_seigle,
                         self.cut_malt,self.cut_ortie,self.cut_frene]



    def moving_target(self):

        self.difference_position[0] = self.target_map[0] - self.actuel_map[0]
        self.difference_position[1] = self.target_map[1] - self.actuel_map[1]

        print(self.name)
        #print('Actual->target')
        print(self.actuel_map)
        print(self.target_map)

        if self.difference_position[0]==0 and self.difference_position[1]==0:
            self.in_target_map = True
            #if self.full_pod == False:
            #    self.collecting = True
            #return

        if self.difference_position[0] != 0 or self.difference_position[1] != 0:
            self.in_target_map = False
            if self.difference_position[0] > 0:
                pg.click(right)
                self.timer_begin_moving = time.time()
                self.difference_position[0] = self.difference_position[0] - 1
                self.actuel_map[0] = self.actuel_map[0] + 1
                sleep(1)
                return

            if self.difference_position[0] < 0:
                pg.click(left)
                self.timer_begin_moving = time.time()
                self.difference_position[0] = self.difference_position[0] + 1
                self.actuel_map[0] = self.actuel_map[0] - 1
                sleep(1)
                return

            if self.difference_position[1] > 0:
                pg.click(down)
                self.timer_begin_moving = time.time()
                self.difference_position[1] = self.difference_position[1] - 1
                self.actuel_map[1] = self.actuel_map[1] + 1
                sleep(1)
                return

            if self.difference_position[1] < 0:
                pg.click(up)
                self.timer_begin_moving = time.time()
                self.difference_position[1] = self.difference_position[1] + 1
                self.actuel_map[1] = self.actuel_map[1] - 1
                sleep(1)
                return

    #check
    def collect(self):
        for idx in range(np.shape(self.cut_list)[0]):
            if self.cut_list[idx] == True:
                ##CHANGE HERE: ask for specific picture in function of i
                try:
                    c = pg.locateOnScreen('./images/cereales/ble.jpg', confidence=0.7, region=(x(367), y(47), x(1181), y(842)))
                    if c == None:
                        c = pg.locateOnScreen('./images/cereales/ble1.jpg', confidence=0.7,
                                              region=(x(367), y(47), x(1181), y(842)))
                    if c == None:
                        c = pg.locateOnScreen('./images/cereales/ble2.jpg', confidence=0.7,
                                              region=(x(367), y(47), x(1181), y(842)))
                    if c == None:
                        c = pg.locateOnScreen('./images/cereales/ble3.jpg', confidence=0.7,
                                              region=(x(367), y(47), x(1181), y(842)))
                    if c == None:
                        c = pg.locateOnScreen('./images/cereales/ble4.jpg', confidence=0.8,
                                              region=(x(367), y(47), x(1181), y(842)))
                    if c!=None:
                        self.timer_begin_cutting = time.time()
                        self.is_cutting = True
                        c = pg.center(c)
                        pg.moveTo(c[0], c[1])
                        pg.click()
                        return
                except:
                    return
        #fini de collect tout sur la map

        #this will be execute if there is nothing to cut in the map
        #print('Pas de ressources ici')
        self.idx_tour = self.idx_tour + 1
        if self.name_tour=='astrub1':
            tour = self.tour_astrub_ble1

        if self.name_tour == 'astrub2':
            tour = self.tour_astrub_ble2

        if self.idx_tour >= np.shape(tour)[0]:
            self.idx_tour=0
        self.in_target_map = False


    def checkFullPod(self):

        full_pod = pg.locateOnScreen('./images/full_pod.jpg', confidence=0.7,
                                     region=(x(1235), y(990), x(65), y(35)))

        if full_pod == None:
            return
        else:
            print('full_pod')
            self.full_pod=True

            return

    def go_bank_astrub(self):
        print('map of bank')
        # sleep(1)
        sleep(3)
        # entrer bank
        pg.click(x(1130), y(372))
        # sleep(6)
        sleep(10)
        # clic pnj
        pg.click(x(1111), y(459))
        # sleep(1)
        sleep(3)
        # answer pnj
        pg.click(x(913), y(754))
        # sleep(2)
        sleep(5)
        # clic arrow inventaire
        pg.click(x(1261), y(153))
        # sleep(1)
        sleep(3)
        # clic tout les objets
        pg.click(x(1362), y(166))
        # sleep(1)
        sleep(3)
        # close windows
        pg.click(x(1552), y(117))
        # sleep(1)
        sleep(3)
        # go out of bank
        pg.click(x(716), y(696))
        # sleep(2)
        sleep(6)
        self.full_pod=False
        self.in_target_map=False

    #def time_check(self):
        #time = time_actuel->use fct timer
        #if (time-self.timer_begin_cutting)>3.5:
            #self.is_cutting = False






# convert
def x(x):
    x = largeur / 1920 * x
    return int(x)


def y(y):
    y = hauteur / 1080 * y
    return int(y)

left = [x(200), y(500)]
right = [x(1700), y(500)]
up = [x(900), y(31)]
down = [x(1050), y(903)]

def checkFight():
    f = pg.locateOnScreen('./images/fight/pret.jpg', confidence =0.8, region = (x(1300),y(913),x(160),y(65)))
    if f == None:
        #print('No fight')
        return
    else:
        fight()
        return

def invocation_sacrifiee(Coyeur1, Coyeur2, Coyeur3, Coyeur4):
    #print('sacrifiee')
    sleep(2)
    if Coyeur1 != None:
        # clic sort sacrifiee
        pg.click(939, 942)
        sleep(2)
        pg.click(Coyeur1[0] - 45, Coyeur1[1] - 25)
        sleep(1)
        pg.moveTo(780, 942)
        sleep(1)
        sacrifiee_lancee = pg.locateOnScreen('./images/fight/sacrifiee_lancee.jpg', confidence=0.8,
                                             region=(x(911), y(911), x(45), y(45)))
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
        sacrifiee_lancee = pg.locateOnScreen('./images/fight/sacrifiee_lancee.jpg', confidence=0.8,
                                             region=(x(911), y(911), x(45), y(45)))
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
        sacrifiee_lancee = pg.locateOnScreen('./images/fight/sacrifiee_lancee.jpg', confidence=0.8,
                                             region=(x(911), y(911), x(45), y(45)))
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
        sacrifiee_lancee = pg.locateOnScreen('./images/fight/sacrifiee_lancee.jpg', confidence=0.8,
                                             region=(x(911), y(911), x(45), y(45)))
        if sacrifiee_lancee == None:
            sleep(2)
            pg.click(939, 942)
            sleep(2)
            pg.click(Coyeur4[0] - 45, Coyeur4[1] + 25)

    sleep(1)


def fight():
    #print("fight")
    # click pret
    sleep(1)
    pg.click(1378, 952)
    fermer = pg.locateOnScreen('./images/fight/fermer.jpg', confidence=0.8, region=(x(813), y(589), x(200), y(60)))
    sleep(2)

    Coyeur1 = pg.locateOnScreen('./images/coyeur_pano_bouftou/dos_gauche_rouge.jpg', confidence=0.8,
                                region=(x(367), y(47), x(1181), y(842)))
    Coyeur2 = pg.locateOnScreen('./images/coyeur_pano_bouftou/dos_droite_rouge.jpg', confidence=0.8,
                                region=(x(367), y(47), x(1181), y(842)))
    Coyeur3 = pg.locateOnScreen('./images/coyeur_pano_bouftou/face_gauche_rouge.jpg', confidence=0.8,
                                region=(x(367), y(47), x(1181), y(842)))
    Coyeur4 = pg.locateOnScreen('./images/coyeur_pano_bouftou/face_droite_rouge.jpg', confidence=0.8,
                                region=(x(367), y(47), x(1181), y(842)))

    while Coyeur1 == None and Coyeur2 == None and Coyeur3 == None and Coyeur4 == None:
        Coyeur1 = pg.locateOnScreen('./images/coyeur_pano_bouftou/dos_gauche_rouge.jpg', confidence=0.8,
                                    region=(x(367), y(47), x(1181), y(842)))
        Coyeur2 = pg.locateOnScreen('./images/coyeur_pano_bouftou/dos_droite_rouge.jpg', confidence=0.8,
                                    region=(x(367), y(47), x(1181), y(842)))
        Coyeur3 = pg.locateOnScreen('./images/coyeur_pano_bouftou/face_gauche_rouge.jpg', confidence=0.8,
                                    region=(x(367), y(47), x(1181), y(842)))
        Coyeur4 = pg.locateOnScreen('./images/coyeur_pano_bouftou/face_droite_rouge.jpg', confidence=0.8,
                                    region=(x(367), y(47), x(1181), y(842)))

    if Coyeur1 != None:
        Coyeur1 = pg.center(Coyeur1)

    if Coyeur2 != None:
        Coyeur2 = pg.center(Coyeur2)

    if Coyeur3 != None:
        Coyeur3 = pg.center(Coyeur3)

    if Coyeur4 != None:
        Coyeur4 = pg.center(Coyeur4)

    # invoc sacrifiee
    invocation_sacrifiee(Coyeur1, Coyeur2, Coyeur3, Coyeur4)
    round_before_spell = 7

    while fermer == None:
        # click passer tour , a verifier
        if round_before_spell == 0:
            invocation_sacrifiee(Coyeur1, Coyeur2, Coyeur3, Coyeur4)
            round_before_spell = 7
        else:
            #print('passe tour')
            pg.click(1378, 952)
            round_before_spell = round_before_spell - 1
            sleep(6)
            fermer = pg.locateOnScreen('./images/fight/fermer.jpg', confidence=0.8,
                                       region=(x(813), y(589), x(200), y(60)))

    # click in cas of level up
    sleep(1)
    pg.click(961, 776)
    sleep(1)
    # close summary fight
    pg.click(916, 616)

def change_window(mode):
    if mode=='tab':
        pg.keyDown('alt')
        pg.press('tab')
        pg.keyUp('alt')
    if mode=='esc':
        pg.keyDown('alt')
        pg.press('esc')
        pg.keyUp('alt')


def initialize():
    pg.click(555, 1008)
    pg.write("%pos%")
    pg.press('enter')

    # attention, acitvé le chat de guilde
    pg.click(468, 975)
    pg.dragTo(430, 972, 1, button='left')
    #pg.dragTo(410, 975, 2, button='left')
    pg.keyDown('ctrl')
    pg.press('c')
    pg.keyUp('ctrl')
    map_actual = pyperclip.paste()
    #from IPython import embed
    #embed()
    #print(map_actual)
    map_actual = map_actual.strip()

    # convert string to list
    #%pos%
    # map_actual = json.loads(map_actual)
    map_actual = [6,-28]
    return map_actual




sleep(6)
change_window('esc')
#on player1 window
pos_initial1 = initialize()
#sleep(1)
#change_window('esc')
#on player2 window
#sleep(1)
#pos_initial2 = initialize()
#change_window('esc')
#on player3 window
#sleep(1)
#pos_initial3 = initialize()
#sleep(1)
#change_window('esc')
#change_window('esc')
sleep(1)


player1 = Player('player1',pos_initial1,0,'astrub1')
#player2 = Player('player2',pos_initial2,0,'astrub2')
#player3 = Player('player3',pos_initial3,4,'astrub2')

player1.in_target_map=False
#player2.in_target_map=False
#player3.in_target_map=False

while True:

    #P1
    if time.time()-4 > player1.timer_begin_cutting and time.time()-7 > player1.timer_begin_moving:
        if time.time()-4 > player1.timer_begin_cutting:
            player1.is_cutting = False

        sleep(abs(np.random.normal(loc=0.0, scale=1.0, size=None)))

        #checkFight()

        player1.checkFullPod()
        if player1.full_pod==True: #and player1.is_collecting==False:
            player1.target_map = [4, -18]
            player1.moving_target()
            if player1.actuel_map == player1.target_map:
                # is on the bank map
                print('in map bank')
                sleep(3)
                player1.go_bank_astrub()
                player1.full_pod = False
                player1.target_map = player1.tour_astrub_ble1[player1.idx_tour]
                player1.moving_target()


        if player1.in_target_map==False and player1.full_pod==False: #and player1.collecting==False :
            #print('moving')
            player1.target_map = player1.tour_astrub_ble1[player1.idx_tour]
            #print(player1.target_map)
            player1.moving_target()

        if player1.in_target_map==True and player1.full_pod==False and player1.is_cutting == False:
            #print('collecting')
            player1.collect()








