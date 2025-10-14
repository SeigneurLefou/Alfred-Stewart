import json
from alfred import *
from var import *

class Face:
    def __init__(self, eyebrow="_ _", ears="c ", eyes="0 0", nose=" | ", mouth=" - "):
        self.eyebrow = eyebrow
        self.ears = ears
        self.eyes = eyes
        self.nose = nose
        self.mouth = mouth
    def dict_return(self):
        return {"eyebrow": self.eyebrow, "ears": self.ears, "eyes": self.eyes, "nose": self.nose, "mouth": self.mouth}

def add_emotion(dict_face:dict, emotion:str, list_face:list):
    if emotion in dict_face:
        if input("Cette emotion existe deja, voulez vous la modifier avec votre nouvelle version ?\nTapez [y] si oui.\n>>> ") == "y":
            dict_face[emotion] = Face(list_face[0], list_face[1], list_face[2], list_face[3], list_face[4]).dict_return()
    else:
        dict_face[emotion] = Face(list_face[0], list_face[1], list_face[2], list_face[3], list_face[4]).dict_return()
    return dict_face

def str_face_to_list_face(str_face:"str"):
    list_face = [str_face[0:3], str_face[3:5]]
    mini = 5
    for maxi in range(7, len(str_face) + 1, 3):
        list_face.append(str_face[mini:maxi])
        mini = maxi
    return list_face

def write_json_file(dict_face):
    json.dump(dict_face, open(f"{local_folder}media/face.json", 'w', encoding='utf-8'), indent=4, ensure_ascii=False)

def add_face_json_with_str(emotion, str_face):
    with open(f"{local_folder}/media/face.json", "r", encoding='utf-8') as face_json:
        dict_face = json.load(face_json)

        dict_face = add_emotion(dict_face, emotion, str_face_to_list_face(str_face))
        write_json_file(dict_face)

def add_face_json(emotion, eyebrow="_ _", ears="c ", eyes="0 0", nose=" | ", mouth=" - "):
    with open(f"{local_folder}/media/face.json", "r", encoding='utf-8') as face_json:
        dict_face = json.load(face_json)

        dict_face = add_emotion(dict_face, emotion, [eyebrow[0:3], ears[0:2], eyes[0:3], nose[0:3], mouth[0:3]])
        write_json_file(dict_face)

def list_emot():
    with open(f"{local_folder}media/face.json", "r", encoding='utf-8') as face_json:
        dict_face = json.load(face_json)
        print(", ".join(list(dict_face.keys())))

def column_list_emot():
    with open(f"{local_folder}media/face.json", "r", encoding='utf-8') as face_json:
        dict_face = json.load(face_json)
        print("\n".join(list(dict_face.keys())))

def list_show_emot():
    with open(f"{local_folder}media/face.json", "r", encoding='utf-8') as face_json:
        dict_face = json.load(face_json)
        for emot in dict_face.keys():
            print_alfred(emot)
            print(" {}".format(emot))
