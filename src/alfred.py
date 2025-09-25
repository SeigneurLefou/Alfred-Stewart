# import wrapper as wrp
import json

def alfred(emotion:str):
    with open("media/faces.json", "r", encoding="utf-8") as face:
        face_dict = json.load(face)
        emot_face = face_dict[emotion]
    printable_alfred = "   ____\n  / {}\\\n  {}{}|\n  | {}|\n  | {}|\n  \\____/\n  _| |_\n / \\_/ \\\n |     |".format(emot_face["eyebrow"], emot_face["ears"], emot_face["eyes"], emot_face["nose"], emot_face["mouth"])
    return printable_alfred

def print_alfred(emotion):
    printable_alfred = alfred(emotion)
    print(printable_alfred)

def albbl(emotion, txt):
    pass
