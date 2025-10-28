function dnldlfrd() {
    local target_dir="$HOME"
    local alfred_dir="${target_dir}/.alfred"
    local current_shell=$(ps -p $$ | awk 'NR==2 {print $4}')
    local alias_line="alias alfred=\"python3 ${alfred_dir}/src/main.py\""
    local userjson=$(cat <<EOF
{
	"username":"Bruce",
	"userfunctions":[],
	"userfolder":"${alfred_dir}/"
}
EOF
    )
    local varfile=$(cat <<EOF
import json
with open("${alfred_dir}/media/userdata.json", "r") as data:
    jsonvar = json.load(data)
EOF
    )
    local exportfile=$(cat <<EOF
import sys
sys.path.insert(0, "$alfred_dir/src/functions/")
# ==========
EOF
    )

    # Suppression du dossier existant si nécessaire
    if [ -d "${alfred_dir}" ]; then
        echo "Le dossier ${alfred_dir} existe déjà. Suppression en cours..."
        rm -Rf "${alfred_dir}"
    fi

    # Clone du dépôt
    if ! command -v git &> /dev/null; then
        echo "Erreur : git n'est pas installé." >&2
        return 1
    fi
    if ! git clone https://github.com/SeigneurLefou/Alfred-Stewart.git "${alfred_dir}"; then
        echo "Erreur : échec du clonage. Vérifie ta connexion réseau." >&2
        return 1
    fi

    # Création des dossiers nécessaires
    mkdir -p "${alfred_dir}/media"
    mkdir -p "${alfred_dir}/src"

    # Écriture des fichiers de configuration
    echo "$userjson" > "${alfred_dir}/media/userdata.json"
    echo "Fichier userdata.json créé."
    echo "$varfile" > "${alfred_dir}/src/varjson.py"
    echo "Fichier varjson.py créé."
    echo "$exportfile" > "${alfred_dir}/src/export.py"
    echo "Fichier varjson.py créé."

    # Gestion de l'alias selon le shell
    case "$current_shell" in
        *bash*)
            echo "Configuration pour Bash détectée."
            if ! grep -qF "$alias_line" ~/.bashrc; then
                echo "$alias_line" >> ~/.bashrc
                echo "Alias ajouté à ~/.bashrc. Exécute 'source ~/.bashrc' pour l'activer."
            else
                echo "L'alias existe déjà dans ~/.bashrc."
            fi
            ;;
        *zsh*)
            echo "Configuration pour Zsh détectée."
            if ! grep -qF "$alias_line" ~/.zshrc; then
                echo "$alias_line" >> ~/.zshrc
                echo "Alias ajouté à ~/.zshrc. Exécute 'source ~/.zshrc' pour l'activer."
            else
                echo "L'alias existe déjà dans ~/.zshrc."
            fi
            ;;
        *)
            echo "Shell non reconnu ($current_shell). Ajoute manuellement l'alias :"
            echo "$alias_line"
            ;;
    esac

    echo "Alfred est prêt ! Teste-le avec : alfred show"
}
dnldlfrd
