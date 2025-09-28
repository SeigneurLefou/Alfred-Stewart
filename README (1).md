# Alfred-Stewart
---
---

Alfred is an assisstant to use for add some automatisation in python, and soon in bash, C and C++. You can also use the base command like `alfred albbl "text"` in your .bashrc or in your .zschrc with simple function.

## Command
---

`alfred show` : Showing the face of Alfred with emotion precise with --emot flag or "neutral" face
`alfred emot` : Add an emotion with a name, eyebrows, ears, eyes, nose, and mouth
`alfred list` : List available emotion face can be use with alfred. In row, column or with example.
`alfred bbl` : Print a simple bubble with some text wrapping and size limitation.
`alfred albbl` : Print Alfred with a bubble of text with emotion, text wrapping and size limit.
`alfred add_python_function` : Add an function python define by the user. Use `alfred add_python_function -h "Help text of your function" -f "$(cat file_with_only_one_function)"

## Download
---

Install Alfred using the following command. Specify a target directory or omit it to install in your home folder (`~/.alfred/`).

Copy the following command and execute in your terminal

```
function dnldlfrd() {
    local target_dir="${1:-$HOME}"
    local alfred_dir="${target_dir}/.alfred/"
    local current_shell=$(ps -p $$ | awk 'NR==2 {print $4}')
    local alias_line="alias alfred=\"python3 ${alfred_dir}src/main.py\""

    if ! command -v git &> /dev/null; then
        echo "Erreur : git n'est pas installé." >&2
        return 1
    fi

    if ! git clone https://github.com/SeigneurLefou/Alfred-Stewart.git "${alfred_dir}"; then
        echo "Erreur : échec du clonage. Vérifie ta connexion réseau." >&2
        return 1
    fi

	mkdir "$alfred_dir/src/user_function"
	touch "$alfred_dir/src/user_function/export_function.py"
	touch "$alfred_dir/src/user_function/function_py.py"
	touch "$alfred_dir/src/user_function/function_sh.sh"
	echo "from export_function import *
def ft_user_arg(args):
	return args" >> "$alfred_dir/src/user_function/user_arg.py"
	echo "def ft_user_command(subparsers):
	return subparsers
	" >> u"$alfred_dir/src/user_function/user_command.py"


    case "$current_shell" in
        *bash*)
            echo "Configuration pour Bash détectée."
            if ! grep -qF "$alias_line" ~/.bashrc; then
                echo "$alias_line" >> ~/.bashrc
                source ~/.bashrc
                echo "Alias ajouté à ~/.bashrc et sourcé."
            else
                echo "L\'alias existe déjà dans ~/.bashrc. Aucune modification nécessaire."
            fi
            ;;
        *zsh*)
            echo "Configuration pour Zsh détectée."
            if ! grep -qF "$alias_line" ~/.zshrc; then
                echo "$alias_line" >> ~/.zshrc
                source ~/.zshrc
                echo "Alias ajouté à ~/.zshrc et sourcé."
            else
                echo "L'alias existe déjà dans ~/.zshrc. Aucune modification nécessaire."
            fi
            ;;
        *)
            echo "Shell non reconnu ($current_shell). Ajoute manuellement l'alias :"
            echo "$alias_line"
            echo "Puis exécute 'source ~/.bashrc' ou 'source ~/.zshrc'."
            ;;
    esac

    local var_line="import os
local_folder = os.path.expanduser(\"${alfred_dir}\") if \"${alfred_dir}\"[0] == "~" else ${alfred_dir}"
	echo "$var_line" >> "${alfred_dir}src/var.py"
	echo "Fichier var.py mis à jour."

    echo "Alfred est prêt ! Teste-le avec : alfred show"
}
```

After the execution copy and paste this command in your terminal and complete with the path you want to use, or nothing if you want to use root.

`dnldlfrd # [/path/to/target/directory] Default: ~/`
