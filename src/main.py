from header import *

def main():
    parser = argparse.ArgumentParser(
        prog="Alfred",
        description="Alfred l\'assistant personnalisé pour des commandes d\'automatisation",
        epilog="Utilisez Alfred et ses commandes grâce à la commande `alfred`"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Sous-commande "show"
    parser_show = subparsers.add_parser("show", help="Présentation de Alfred sans bulle de texte.")
    with open(f"{local_folder}media/faces.json", "r", encoding="utf-8") as face_json:
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
    with open(f"{local_folder}media/faces.json", "r", encoding="utf-8") as face_json:
        dict_face = json.load(face_json)
        parser_albbl.add_argument("--emot", "-e", choices=[emot for emot in dict_face.keys()], default="neutral")
    parser_albbl.add_argument("--linesize", "-ls", type=int, help="La taille maximale d'une ligne.")

    args = parser.parse_args()

    if args.command == "show":
        print_alfred(args.emot or "neutral")
    if args.command == "emot":
        add_face_json(args.name, args.eyebrow or "_ _", args.ears or "c ", args.eyes or "0 0", args.nose or " | ", args.mouth or " - ")
    if args.command == "list":
        if args.column:
            column_list_emot()
        elif args.show:
            list_show_emot()
        else:
            list_emot()
    if args.command == "bbl":
        if args.txt:
            print_bubble(args.txt, args.linesize or 80)
        else:
            print_bubble(line_len = (args.linesize or 80))
    if args.command == "albbl":
        if args.txt:
            print_alfred_bubble(args.txt, emotion = args.emot, line_len = (args.linesize or 80))
        else:
            print_alfred_bubble(emotion = args.emot, line_len = (args.linesize or 80))

if __name__ == "__main__":
    main()
