import json

from text import *
from varjson import *

def alfred(emotion = "neutral"):
    with open("{}media/faces.json".format(jsonvar["userfolder"]), "r", encoding="utf-8") as face:
        face_dict = json.load(face)
        emot_face = face_dict[emotion]
    printable_alfred = "   ____ \n  / {}\\\n  {}{}|\n  | {}|\n  | {}|\n  \\____/\n  _| |_ \n / \\_/ \\\n |     |".format(emot_face["eyebrow"], emot_face["ears"], emot_face["eyes"], emot_face["nose"], emot_face["mouth"])
    return printable_alfred.split("\n")

def print_alfred(emotion = "neutral"):
    printable_alfred = alfred(emotion)
    for line in printable_alfred:
        print(line)

def bubble(txt = "Je suis Alfred l'assistant de commande codé par Loïc Chamard.", line_len = 80):
    t_txt = treated_text(txt, line_len)
    padding = 2 + len(t_txt[0])
    bubble_tab = []
    bubble_tab.append("  __{}".format(padding * '_'))
    bubble_tab.append(" /  {}\\".format(padding * ' '))
    for line in t_txt:
        bubble_tab.append(" |  {}  |".format(line))
    bubble_tab.append(" \\  {}/".format(padding * '_'))
    bubble_tab.append("  |/")
    return bubble_tab

def print_bubble(txt = "Je suis Alfred l'assistant de commande codé par Loïc Chamard.", line_len = 80):
    bbl_tab = bubble(txt, line_len)
    for line in bbl_tab:
        print(line)

def alfred_bubble(txt = "Je suis Alfred l'assistant de commande codé par Loïc Chamard.", emotion = "neutral", line_len = 80):
    al = alfred(emotion)
    bbl = bubble(txt, line_len)
    tab_spc = (len(bbl) - 4) * [' ' * len(al[0])]
    tab_spc.extend(al)
    al = tab_spc
    albbl= []
    for i in range(len(al)):
        if i < len(bbl):
            albbl.append("{}{}".format(al[i], bbl[i]))
        else:
            albbl.append(al[i])
    return albbl

def print_alfred_bubble(txt = "Je suis Alfred l'assistant de commande codé par Loïc Chamard.", emotion = "neutral", line_len = 80):
    albbl_tab = alfred_bubble(txt, emotion, line_len)
    for line in albbl_tab:
        print(line)
