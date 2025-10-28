function dnldlfrd() {
    local target_dir="$HOME"
    local alfred_dir="${target_dir}/.alfred"
    local current_shell=$(ps -p $$ | awk 'NR==2 {print $4}')
    local alias_line='alias alfred="python3 ${alfred_dir}/src/main.py"'
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

    # Deleting existing directory if necessary
    if [ -d "${alfred_dir}" ]; then
        echo "Directory ${alfred_dir} already exists. Deleting..."
        rm -Rf "${alfred_dir}"
        echo "Directory deleted."
    fi

    # Cloning the repository
    if ! command -v git &> /dev/null; then
        echo "Error: git is not installed." >&2
        return 1
    fi
    echo "Cloning repository..."
    if ! git clone https://github.com/SeigneurLefou/Alfred-Stewart.git "${alfred_dir}"; then
        echo "Error: Clone failed. Check your network connection." >&2
        return 1
    fi
    echo "Repository cloned successfully."

    # Creating necessary directories
    echo "Creating media directory..."
    mkdir -p "${alfred_dir}/media"
    echo "Media folder created."

    echo "Creating src directory..."
    mkdir -p "${alfred_dir}/src"
    echo "SRC folder created."

    echo "Creating functions directory..."
    mkdir -p "${alfred_dir}/src/functions"
    echo "Functions folder created."

    # Writing configuration files
    echo "Creating userdata.json..."
    echo "$userjson" > "${alfred_dir}/media/userdata.json"
    echo "File userdata.json created."

    echo "Creating varjson.py..."
    echo "$varfile" > "${alfred_dir}/src/varjson.py"
    echo "File varjson.py created."

    echo "Creating export.py..."
    echo "$exportfile" > "${alfred_dir}/src/export.py"
    echo "File export.py created."

	if ! command -v python3 &> /dev/null; then
	    echo "Error: python3 is not installed." >&2
	    return 1
	fi

    # Managing alias according to shell
    case "$current_shell" in
        *bash*)
            echo "Bash configuration detected."
            if ! grep -qF "$alias_line" ~/.bashrc; then
                echo "Adding alias to ~/.bashrc..."
                echo "$alias_line" >> ~/.bashrc
                echo "Alias added to ~/.bashrc. Run 'source ~/.bashrc' to activate."
            else
                echo "Alias already exists in ~/.bashrc."
            fi
            ;;
        *zsh*)
            echo "Zsh configuration detected."
            if ! grep -qF "$alias_line" ~/.zshrc; then
                echo "Adding alias to ~/.zshrc..."
                echo "$alias_line" >> ~/.zshrc
                echo "Alias added to ~/.zshrc. Run 'source ~/.zshrc' to activate."
            else
                echo "Alias already exists in ~/.zshrc."
            fi
            ;;
        *)
            echo "Unrecognized shell ($current_shell). Manually add the alias:"
            echo "$alias_line"
            ;;
    esac

    echo "Alfred is ready! Test it with: alfred show"
}
