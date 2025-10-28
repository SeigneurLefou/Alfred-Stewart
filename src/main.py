from header import *
import export
import commands
import args

def main():
    parser = argparse.ArgumentParser(
        prog="Alfred",
        description="Alfred l\'assistant personnalisé pour des commandes d\'automatisation",
        epilog="Utilisez Alfred et ses commandes grâce à la commande `alfred`"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Sous-commande "show"
    parser_show = subparsers.add_parser("show", help="Présentation de Alfred sans bulle de texte.")
    with open("{}media/faces.json".format(jsonvar["userfolder"]), "r", encoding="utf-8") as face_json:
        dict_face = json.load(face_json)
        parser_show.add_argument("--emot", "-e", choices=[emot for emot in dict_face.keys()], default="neutral")

    # Sous-commande "emot"
    parser_emot = subparsers.add_parser("emot", help="Ajout d'une émotion à la base de donnée.")
    parser_emot.add_argument("--name", "-n", type=str, required=True, help="Donne le nom de la nouvelle emotion")
    parser_emot.add_argument("--eyebrow", type=str, help="Les sourcils de la nouvelle emotion")
    parser_emot.add_argument("--ears", type=str, help="Les oreilles de la nouvelle emotion")
    parser_emot.add_argument("--eyes", type=str, help="Les yeux de la nouvelle emotion")
    parser_emot.add_argument("--nose", type=str, help="Le nez de la nouvelle emotion")
    parser_emot.add_argument("--mouth", type=str, help="La bouche de la nouvelle emotion")

    # Sous-commande "list"
    parser_emot = subparsers.add_parser("list", help="Liste les émotions de la base de donnée en ligne.")
    parser_emot.add_argument("--column", "-c", action='store_true', help="Liste les émotions de la base de donnée en colonne.")
    parser_emot.add_argument("--show", "-s", action='store_true', help="Affiche un petit visuel de chaque emotion")

    # Sous-commande "bbl"
    parser_bbl = subparsers.add_parser("bbl", help="Affiche une bulle de texte à la manière des comics ou des bd.")
    parser_bbl.add_argument("--txt", "-t", type=str, help="Le texte que vous voulez affichez dans la bulle de texte.")
    parser_bbl.add_argument("--linesize", "-ls", type=int, help="La taille maximale d'une ligne.")

    # Sous-commande "albbl"
    parser_albbl = subparsers.add_parser("albbl", help="Faire parler Alfred.")
    parser_albbl.add_argument("--txt", "-t", type=str, help="Le texte que vous voulez affichez dans la bulle de texte.")
    with open("{}media/faces.json".format(jsonvar["userfolder"]), "r", encoding="utf-8") as face_json:
        dict_face = json.load(face_json)
        parser_albbl.add_argument("--emot", "-e", choices=[emot for emot in dict_face.keys()], default="neutral")
    parser_albbl.add_argument("--linesize", "-ls", type=int, help="La taille maximale d'une ligne.")

    parser_add_python_function = subparsers.add_parser("macropy", help="Permet d'ajouter une commande personnalisé à Alfred")
    parser_add_python_function. add_argument("--function", "-f", required=True, help="Contenue de la fonction à ajouter. Cependant votre fonction doit respecter un entete particulier avec les type des arguments de spécifié `def foo(arg:str, arg:int):`. Possible utilisation de `alfred macropy -f \"$(cat file_avec_votre_fonction.py)\"`.")
    parser_add_python_function. add_argument("--help_function", "-hf", type=str, help="Contenue du help de votre fonction")

    subparsers = commands.ft_user_command(subparsers)

    arguments = parser.parse_args()

    if arguments.command == "show":
        print_alfred(arguments.emot or "neutral")
    if arguments.command == "emot":
        add_face_json(arguments.name, args.eyebrow or "_ _", args.ears or "c ", args.eyes or "0 0", args.nose or " | ", args.mouth or " - ")
    if arguments.command == "list":
        if arguments.column:
            column_list_emot()
        elif arguments.show:
            list_show_emot()
        else:
            list_emot()
    if arguments.command == "bbl":
        if arguments.txt:
            print_bubble(args.txt, arguments.linesize or 80)
        else:
            print_bubble(line_len = (arguments.linesize or 80))
    if arguments.command == "albbl":
        if arguments.txt:
            print_alfred_bubble(arguments.txt, emotion = arguments.emot, line_len = (arguments.linesize or 80))
        else:
            print_alfred_bubble(emotion = arguments.emot, line_len = (arguments.linesize or 80))
    if arguments.command == "macropy":
        macropy(arguments.function.splitlines(), arguments.help_function or "")

    arguments = args.ft_user_arg(arguments)

if __name__ == "__main__":
    main()
