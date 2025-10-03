function dnldlfrd() {
    local target_dir="${1:-$HOME}"
    local alfred_dir="${target_dir}/.alfred/"
    local current_shell=$(ps -p $$ | awk 'NR==2 {print $4}')
    local alias_line="alias alfred=\"python3 ${alfred_dir}src/main.py\""

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

    local var_line="import os
local_folder = \"${alfred_dir}\""
	echo "$var_line" >> "${alfred_dir}src/var.py"
	echo "Fichier var.py mis à jour."

    echo "Alfred est prêt ! Teste-le avec : alfred show"
}
