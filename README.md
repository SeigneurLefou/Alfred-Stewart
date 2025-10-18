# Alfred-Stewart

Alfred is an assistant to use for add some automatisation or macro in python, and soon in bash, C and C++. You can also use the base command like `alfred albbl "text"` in your .bashrc or in your .zschrc with simple function. The macro is just a little part of the opportunity, you can, with time, code a game and add him in alfred with use sys and different file import with sys.

## Command

`alfred show` : Showing the face of Alfred with emotion precise with --emot flag or "neutral" face

`alfred emot` : Add an emotion with a name, eyebrows, ears, eyes, nose, and mouth

`alfred list` : List available emotion face can be use with alfred. In row, column or with example.

`alfred bbl` : Print a simple bubble with some text wrapping and size limitation.

`alfred albbl` : Print Alfred with a bubble of text with emotion, text wrapping and size limit.

`alfred macropy` : Add an function python define by the user. Use type specificator for argument ! Use `alfred macropy -h "Help text of your function" -f "$(cat file_with_only_one_function.py)"`.

## User

If you have idea of command who could be useful or not useless so open an issue for present your idea.

## Download

Install Alfred using the following command. Specify a target directory or omit it to install in your home folder (`~/.alfred/`).

Copy the following command and execute in your terminal

If you use zsh terminal :

```
curl https://raw.githubusercontent.com/SeigneurLefou/Alfred-Stewart/refs/heads/main/.download.sh | zsh
```

If you use bash terminal :

```
curl https://raw.githubusercontent.com/SeigneurLefou/Alfred-Stewart/refs/heads/main/.download.sh | bash
```

If you use fish terminal :

```
curl https://raw.githubusercontent.com/SeigneurLefou/Alfred-Stewart/refs/heads/main/.download.sh | fish
```

## TODO List
- [ ] Add user function for Reload and Delete more clean
- [ ] Add other langage for user function like bash, C or C++, with command macroc, macrocpp, and macrosh
- [ ] Add basic shutdown reboot or other
- [ ] Add Alfred library with basic function can be used.
