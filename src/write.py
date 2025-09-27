import sys
sys.path.insert(0, "../")

from var import *

# deleting a line
# based on the position

# opening the file in
# reading mode

def delete_last_line(path):
    with open(path, 'r') as fr:
        lines = fr.readlines()
        last = len(lines)
        ptr = 1
        with open(path, 'w') as fw:
            for line in lines:
                if ptr != last:
                    fw.write(line)
                ptr += 1

def function_py_info(function_content):
    function_info = {"content": function_content}
    start_cc_var = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN_"
    cc_var = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN_0123456789"
    def_line = function_content.split('\n')[0]
    i = 4
    function_info["name"] = ""
    while function_content[i] != '(':
        function_info["name"] += function_content[i]
        i += 1
    i += 1
    function_info["argc"] = 0
    function_info["argv"] = []
    while function_content[i] != ')':
        while function_content[i] not in start_cc_var:
            i += 1
        function_info["argv"].append("")
        while function_content[i] in cc_var:
            function_info["argv"][-1] += function_content[i]
            i += 1
        function_info["argc"] += 1
    return function_info

def reload_python_function():
    pass

def reload_bash_function():
    pass

def add_python_function(function_content:str):
    function_info = function_py_info(function_content)
    if function_content[0:3] == "def" and function_info["name"][0] in "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN_":
        with open(f"{local_folder}src/user_function/function_py.py", 'a') as file:
            file.write(function_content + '\n')
            print("function add to function_py")
        with open(f"{local_folder}src/user_function/export_function.py", 'a') as file:
            file.write(function_content + '\n')
            print("function add to export_function")
        parser = f"\tparser_{function_info["name"]} = subparsers.add_parser(\"{function_info["name"]}\")\n"
        for arg in function_info["argv"]:
            parser += f"\tparser_{function_info["name"]}.add_argument(\"--{arg}\", required = True)\n"
        parser += "\treturn subparsers"

        param_function = ""
        c = 0
        for arg in function_info["argv"]:
            param_function += f"args.{arg}"
            c += 1
            if c < function_info["argc"]:
                param_function += ", "

        if_arg = f"\tif args.command == \"{function_info["name"]}\":\n\t\t{function_info["name"]}({param_function})\n\treturn args"
        
        delete_last_line(f"{local_folder}src/user_function/user_command.py")
        delete_last_line(f"{local_folder}src/user_function/user_arg.py")
        with open(f"{local_folder}src/user_function/user_command.py", 'a') as file:
            file.write(parser)

        with open(f"{local_folder}src/user_function/user_arg.py", 'a') as file:
            file.write(if_arg)

    else:
        raise ValueError("A python function start with \"def\".")

def add_bash_function(function_content:str, args:list):
    pass
