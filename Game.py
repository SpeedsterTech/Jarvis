from random import randint
from functions.math import word_to_int
from functions.InfoPack import InfoPack
from functions.math import word_to_int
Games = []
consoles = ["playstation","computer","switch"," "]
class Game():
    def __init__(self, n, console, min=1,max =1):
        self.name = n
        self.console = console
        self.min = min
        self.max = max
        Games.append(self)
    def display(self):
        print(self.name + ", " + self.console + ", Min: " + str(self.min) + ", Max: " + str(self.max))

def sort(console, players = 1):
    list = []
    list2 = []
    for i in range(0,len(Games)):
        if Games[i].console.lower() == console.lower():
            list.append(Games[i])
    for i in range(0,len(list)):
        if players <= list[i].max and players >= list[i].min:
            list2.append(list[i])
    return list2

def pick(console,players =1):
    canPlay = sort(console,players)
    i = randint(0,len(canPlay)-1)
    canPlay[i].display()
    return canPlay[i].name

def add(string,console,min,max):
    name = ""
    min = word_to_int(min)
    max = word_to_int(max)
    if 'playstation' in console:
        console = 'playstation'
    elif 'computer' in console:
        console = 'computer'
    else:
        console = 'switch'
    f = open('Game.py','a')
    for i in range(0,string.index(" ")):
        name+=string[i]
    f.write(name + ' = Game("'+string + '", "' + console + '", min = ' + str(min) + ', max = ' + str(max) + ') \n')  

def remove(string):
    doc = []
    with open("Game.py", "r+") as file:
        for line in file:
            if not string.lower() in line.lower():
                doc.append(line)
    with open("Game.py", "w") as file:
        file.write("")
    with open("Game.py", "a") as file:
        for i in range(0,len(doc)):
            file.write(doc[i])

def getPickInfo(string):
    things = []
    things.append('people')
    things.append('console')
    for i in range(0,len(consoles)):
        if consoles[i] in string:
            things[1]+=(str(i))
    things[0]+= str(word_to_int(string))
    if 'None' in things[0]:
        things[0]= "people "
    gmInfo = InfoPack(things)
    return gmInfo

rdr2 = Game("Red Dead Redemption 2", "playstation")
ITT = Game("It Takes Two","Computer",2,2)
Minecraft = Game("Minecraft","Computer",10)
Buckshot = Game("Buckshot Roulette", "Computer",max=2)
DL = Game("Dying Light", "Computer",max=4)
Lethal = Game("Lethal Company", "Computer",max=4)
Phas = Game("Phasmophobia","Computer",max=4)
portal = Game("Portal", "Computer")
repo = Game("R.E.P.O.","Computer",max=6)
roblox = Game("Roblox", "Computer",max = 10)
apex = Game("Apex Legends","Playstation", max= 3)
cotL = Game("Cult of the Lamb", "Playstation")
ER = Game("Elden Ring", "Playstation")
Fort = Game("Fortnite", "Playstation", max=4)
GOW = Game("God of War", "PLaystation")
GOWR = Game("God of War Ragnarok", "Playstation")
GTA = Game("GTA 5", "Playstation")
HL = Game("Hogwarts Legacy", "Playstation")
Horizon = Game("Horizon Zero Dawn","Playstation")
INJ = Game("Injustice", "Playstation")
INJ2 = Game("Injustice 2", "Playstation")
LN = Game("Little Nightmares", "Playstation")
LN2 = Game("Little Nightmares 2", "Playstation")
MR = Game("Marvel Rivals", "Playstation",max=6)
MA = Game("Marvel's Avengers", "Playstation")
GOTG = Game("Guardians of the Galaxy", "Playstation")
SM = Game("Spider-Man", "Playstation")
SM2 = Game("Spider-Man 2", "Playstation")
SMMM = Game("Spider-Man: Miles Morales", "Playstation")
MK = Game("Mortal Kombat", "Playstation")
NH3 = Game("Nascar Heat 3", "Playstation")
RC = Game("Ratchet & Clank", "Playstation")
RC2 = Game("Ratchet & Clank: Rift Apart", "Playstation")
RL = Game("Rocket League", "Playstation",max= 4)
SF = Game("Sonic Frontiers", "Playstation")
jedi = Game("Jedi: Fallen Order", "Playstation")
stray = Game("Stray", "Playstation")
sub = Game("Subnautica","Playstation")
