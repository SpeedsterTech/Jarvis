import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\irons\\AppData\\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'steam': "C:\\Program Files (x86)\\Steam\\steam.exe",
    'obs' : "C:\\Users\\Public\\Desktop\\OBS Studio.lnk",
    'fusion' : "C:\\Users\\irons\\OneDrive\\Desktop\\Autodesk Fusion.lnk",
    'audacity' : "C:\\Users\\Public\\Desktop\\Audacity.lnk",
    'timer': "functions\\timer.py",
    'code': "C:\\Users\\irons\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
}

#def open_camera():
    #os.startfile(paths['camera'])

def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])
def open_steam():
    os.startfile(paths['steam'])

def open_obs():
    os.startfile(paths['obs'])

def open_fusion():
    os.startfile(paths['fusion'])

def open_audacity():
    os.startfile(paths['audacity'])

def open_bots():
    os.startfile(paths['streamer'])
    os.startfile(paths['speaker'])