# Alfred-Stewart

Use this command for download Alfred. Complet with the locate of the folder where you want to place the file. Like `... dnldfrd ~/path/to/your/folder/` or nothing if you want it's on the root folder.
```function dnldlfrd() {
    local target_dir="${1:-$HOME}"
    local alfred_dir="$target_dir/.alfred"
    local src_dir="$alfred_dir/src"
    local var_file="$src_dir/var.py"

    # Vérifie git
    if ! command -v git &> /dev/null; then
        echo "Erreur : git n'est pas installé. Installe-le avec 'sudo dnf install git' (Fedora)."
        return 1
    fi

    # Clone le dépôt
    if ! git clone https://github.com/SeigneurLefou/Alfred-Stewart.git "$alfred_dir"; then
        echo "Erreur : échec du clonage du dépôt."
        return 1
    fi

    # Crée la configuration
    {
        echo "# Alfred the steward in terminal"
        echo "alias alfred='python3 $src_dir/main.py'"
        echo "local_folder = \"$alfred_dir/\""
    } >> "$var_file"

    # Détecte le shell et source automatiquement
    if [ -n "$ZSH_VERSION" ]; then
        echo "Configuration pour Zsh détectée. Mise à jour de ~/.zshrc..."
        echo "source $var_file" >> ~/.zshrc
        source ~/.zshrc
        echo "Fichier ~/.zshrc mis à jour et sourcé avec succès."
    elif [ -n "$BASH_VERSION" ]; then
        echo "Configuration pour Bash détectée. Mise à jour de ~/.bashrc..."
        echo "source $var_file" >> ~/.bashrc
        source ~/.bashrc
        echo "Fichier ~/.bashrc mis à jour et sourcé avec succès."
    else
        echo "Shell non reconnu ($SHELL). Ajoute manuellement cette ligne à ton fichier de config :"
        echo "    source $var_file"
        echo "Puis exécute 'source ~/<ton_fichier_de_config>' pour appliquer les changements."
    fi

    echo "Alfred est prêt ! Teste-le avec : alfred show"
}
dnldlfrd ```
