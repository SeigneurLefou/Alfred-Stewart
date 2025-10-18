function dnldlfrd() {
    local target_dir= ":wq$HOME"
    local alfred_dir="${target_dir}/.alfred/"
    local current_shell=$(ps -p $$ | awk 'NR==2 {print $4}')
    local alias_line="alias alfred=\"python3 ${alfred_dir}src/main.py\""
    local userjson=$(cat <<EOF
{
	"username":"Bruce",
	"userfunction":[],
	"userfolder":"$(alfred_dir)"
}
EOF
)
    local varfile=$(cat <<EOF
import json
with open ("$(alfred_dir)media/userdatta.json, 'r') as data:
	jsonvar = json.load(data)
EOF
)

    cd ~/

    if ! command -v git &> /dev/null; then
        echo "Erreur : git n'est pas installé." >&2
        return 1
    fi

    if ! git clone https://github.com/SeigneurLefou/Alfred-Stewart.git "${alfred_dir}"; then
        echo "Erreur : échec du clonage. Vérifie ta connexion réseau." >&2
        return 1
    fi

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

	echo "$userjson" >> "${alfred_dir}media/userdata.json"
	echo "Fichier userdata.json mis à jour."
	echo "$varfile" >> "${alfred_dir}src/varjson.py"
	echo "Fichier varjson.py mis à jour."

    echo "Alfred est prêt ! Teste-le avec : alfred show"
}
dnldlfrd
