# Alfred-Stewart

Alfred is a personal assistant designed to automate tasks or create macros in Python, and soon in Bash, C, and C++. Macros is function in this langages than Alfred include in his code like a command and you can use zith this. You can also use basic commands like `alfred albbl "text"` in your `.bashrc` or `.zshrc` by defining simple functions. Macros are just one part of Alfred's capabilities—over time, you could even code a game and integrate it into Alfred using `sys` and importing different files.

## Commands

| Command          | Description                                                                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `alfred show`    | Displays Alfred’s face with a specific emotion (use the `--emot` flag) or a neutral face by default.                                                                                                       |
| `alfred emot`    | Adds a new emotion with a name, eyebrows, ears, eyes, nose, and mouth.                                                                                                                                      |
| `alfred list`    | Lists available emotions for Alfred’s face. Can be displayed in rows, columns, or with examples.                                                                                                           |
| `alfred bbl`     | Prints a simple speech bubble with text wrapping and size limitations.                                                                                                                                       |
| `alfred albbl`   | Prints Alfred with a speech bubble, including an emotion, text wrapping, and size limits.                                                                                                                   |
| `alfred macropy` | Adds a user-defined Python function. Use type specifiers for arguments! Use `alfred macropy -h "Help text for your function" -f "$(cat file_with_only_one_function.py)"`.                                      |

## Download

Install Alfred using the following command. You can specify a target directory or omit it to install in your home folder (`~/.alfred/`).

Copy and execute the appropriate command for your terminal:

- **Zsh terminal:**
  ```bash
  curl https://raw.githubusercontent.com/SeigneurLefou/Alfred-Stewart/refs/heads/main/.download.sh | zsh
  
- **Bash terminal:**
  ```bash
  curl https://raw.githubusercontent.com/SeigneurLefou/Alfred-Stewart/refs/heads/main/.download.sh | bash
  
- **Fish terminal:**
  ```bash
  curl https://raw.githubusercontent.com/SeigneurLefou/Alfred-Stewart/refs/heads/main/.download.sh | fish

## User Contributions

If you have ideas for useful commands or features, feel free to open an issue to present your suggestion!

## Basic Roadmap

- [x] Add download script
- [x] Add basic printable commands
- [x] Add `emot` command

## Macro Command Roadmap

- [x] Add `macropy` command
- [ ] Add reload command for user functions
- [ ] Add delete command for user functions
- [ ] Add `macroc` command
- [ ] Add `macrocpp` command
- [ ] Add `macrosh` command

## Command Roadmap

- [ ] Add shutdown command
- [ ] Add reboot command
- [ ] Add basic universal commands (based on user ideas)

## Other (If Time Permits)

- [ ] Add a library with Alfred’s basic commands
- [ ] Create a separate repository for add-ons, including themes and bundles for less universal utilities
- [ ] Create the Alfred website for centralize Alfred download, Add-ons, themes, function bundle and more !
