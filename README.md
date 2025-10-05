# Alfred-Stewart

Alfred is an assisstant to use for add some automatisation in python, and soon in bash, C and C++. You can also use the base command like `alfred albbl "text"` in your .bashrc or in your .zschrc with simple function.

## Command

`alfred show` : Showing the face of Alfred with emotion precise with --emot flag or "neutral" face

`alfred emot` : Add an emotion with a name, eyebrows, ears, eyes, nose, and mouth

`alfred list` : List available emotion face can be use with alfred. In row, column or with example.

`alfred bbl` : Print a simple bubble with some text wrapping and size limitation.

`alfred albbl` : Print Alfred with a bubble of text with emotion, text wrapping and size limit.

`alfred add_python_function` : Add an function python define by the user. Use type specificator for argument ! Use `alfred add_python_function -h "Help text of your function" -f "$(cat file_with_only_one_function)"`.

## Download

_For the moment that not work, but soon. Thanks you for your patience. The dev_

_Soon a branch dev come for this moment and you'll have a work command during the changement_

Install Alfred using the following command. Specify a target directory or omit it to install in your home folder (`~/.alfred/`).

Copy the following command and execute in your terminal

```
curl https://raw.githubusercontent.com/SeigneurLefou/Alfred-Stewart/refs/heads/main/other/download.sh | sh
```

~~After the execution copy and paste this command in your terminal and complete with the path you want to use, or nothing if you want to use root.~~

~~```
dnldlfrd # [/path/to/target/directory] Default: ~/```~~
