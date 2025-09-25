function emotion()
{
	python3 alfred_face.py $1 $2
}

## A trier et convertir en python
function bbll()
{
	declare text="$1"
	declare -i padding=2+${#text}
	declare underscore=$(printf '%*s' "$padding" | tr ' ' '_')
	declare space=$(printf '%*s' "$padding")
	echo "  __$underscore"
	echo " /  $space\\"
	echo " |  $1  |"
	echo " \\  $underscore/"
	echo "  |/"
}

function bblr()
{
	declare text="$1"
	declare -i padding=2+${#text}
	declare underscore=$(printf '%*s' "$padding" | tr ' ' '_')
	declare space=$(printf '%*s' "$padding")
	echo "  __$underscore"
	echo " /  $space\\"
	echo " |  $1  |"
	echo " \\$underscore  /"
	echo "  $space\\|"
}

function alfred()
{
	echo "   ____ "
	echo "  /    \\"
	echo "  c-0=0|"
	echo "  |  | |"
	echo "  |  - |"
	echo "  \\____/"
	echo "  _| |_"
	echo " / \\_/ \\"
	echo " |     |"
}

function alfpers()
{
	echo "   ____ "
	echo "  /    \\"
	echo "  | $1|"
	echo "  | $2|"
	echo "  | $3|"
	echo "  \\____/"
	echo "  _| |_"
	echo " / \\_/ \\"
	echo " |     |"
}
function alpres()
{
	echo "   _   _  __            _ "
	echo "  /_\ | |/ _|_ _ ___ __| |"
	echo " / _ \| |  _| '_/ -_) _\` |"
	echo "/_/ \_\_|_| |_| \\___\\__,_|"
                       
}

function albbl()
{
	declare text="$1"
	declare -i padding=2+${#text}
	declare underscore=$(printf '%*s' "$padding" | tr ' ' '_')
	declare space=$(printf '%*s' "$padding")
	echo "          __$underscore"
	echo "   ____  /  $space\\"
	echo "  /    \\ |  $text  |"
	echo "  c-0=0| \\  $underscore/"
	echo "  |  | |  |/"
	echo "  |  - |"
	echo "  \\__ _/"
	echo "  _| |_"
	echo " / \\_/ \\"
	echo "_|     |____"
}

function aldead()
{
	albbl "Au revoir, revenez vite."
	sleep 1
	poweroff
}
