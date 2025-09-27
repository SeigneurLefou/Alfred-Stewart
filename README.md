# Alfred-Stewart

Use this command for download Alfred. Complet with the locate of the folder where you want to place the file. Like `... dnldfrd ~/path/to/your/folder/` or nothing if you want it's on the root folder.
```function dnldlfrd()
{
    if [$# > 1]; then
        git clone https://github.com/SeigneurLefou/Alfred-Stewart.git $1/.alfred/
        echo "# Alfred the stewart in terminal"
        echo "alias alfred="python3 $1/src/main.py" 
        echo "local_folder = $1/.alfred/" >> $1/src/variable.py
    else
        git clone https://github.com/SeigneurLefou/Alfred-Stewart.git ~/.alfred/
        echo "# Alfred the stewart in terminal"
        echo "alias alfred="python3 ~/.alfred/src/main.py" 
        echo "local_folder = ~/.alfred/" >> ~/src/variable.py
    source ~/.bashrc
    fi
}
dnldlfrd ```
