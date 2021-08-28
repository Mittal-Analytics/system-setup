import subprocess


class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def print_heading(text):
    print(color.GREEN + color.BOLD + f"\n\n\n{text}" + color.END)


def print_error(text):
    print(color.RED + color.BOLD + text + color.END)


def get_continue(prompt="Continue [Y/n]?"):
    is_okay = input(prompt) or "y"
    return is_okay.strip().lower() == "y"


def bash(command):
    if isinstance(command, list):
        is_shell = False
    else:
        is_shell = True
        command = [command]
    subprocess.run(args=command, shell=is_shell, check=True)


def replace_line(path, search, replacement, change_is_must=True):
    # the readlines and writelines have a \n in end
    search = search + "\n"
    replacement = replacement + "\n"

    with open(path) as tmp:
        lines = tmp.readlines()

    is_changed = False
    new_lines = []
    for line in lines:
        if line == search:
            new_line = replacement
            is_changed = True
        else:
            new_line = line
        new_lines.append(new_line)

    if change_is_must and not is_changed:
        raise ValueError(f"{search} not found in {path}")

    with open(path, "w") as tmp:
        tmp.writelines(new_lines)
