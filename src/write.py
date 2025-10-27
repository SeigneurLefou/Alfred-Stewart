import sys
import os

sys.path.insert(0, "../src")

from varjson import *

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

def function_py_info(function_line):
    function_content = '\n'.join(function_line)
    function_info = {"content": function_content}
    start_cc_var = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN_"
    cc_var = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN_0123456789"
    i = 0
    while function_line[i][0:3] != 'def':
        i += 1
    def_line = function_line[i]
    i = 4
    function_info["name"] = ""
    while function_content[i] != '(':
        function_info["name"] += function_content[i]
        i += 1
    i += 1
    function_info["argc"] = 0
    function_info["argv"] = []
    function_info["argt"] = []
    while function_content[i] != ')':
        while function_content[i] not in start_cc_var:
            i += 1
        function_info["argv"].append("")
        while function_content[i] in cc_var:
            function_info["argv"][-1] += function_content[i]
            i += 1
        while function_content[i] != ":":
            i += 1
        while function_content[i] not in "azertyuiopqsdfghjklmwxcvbn":
            i += 1
        function_info["argt"].append("")
        while function_content[i] in "azertyuiopqsdfghjklmwxcvbn":
            function_info["argt"][-1] += function_content[i]
            i += 1
        function_info["argc"] += 1
    return function_info

def reload_python_function():
    pass

def reload_bash_function():
    pass

def macropy(function_content:str, help_ft = ""):
    function_info = function_py_info(function_content)
    create_file = True
    if function_content[0:3] == "def" and function_info["name"][0] in "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN_":
        if "{}.py".format(function_info["name"]) in os.listdir():
            if input("This command already exist, do you want to erase the older version ? [y/N]\n>>> ") in ['y', 'Y']:
                create_file = True
            else:
                create_file = False
        if create_file:
            with open("{}user/functions/{}.py".format(jsonvar["userfolder"], function_info["name"]), 'w') as file:
                file.write(function_content)
                print("function add to functions/")
            with open("{}user/export.py".format(jsonvar["userfolder"]), 'a') as file:
                file.write("\nimport {}\n".format(function_info["name"]))
                print("function add to export")
            parser = "\n\tparser_{} = subparsers.add_parser(\"{}\", help=\"{help_ft}\")\n".format(function_info["name"], function_info["name"])
            for i in range(function_info["argc"]):
                parser += "\tparser_{}.add_argument(\"--{}\", type={}, required = True)\n".format(function_info["name"], function_info["argv"][i], function_info["argt"][i])
            parser += "\treturn subparsers"

            param_function = ""
            c = 0
            for arg in function_info["argv"]:
                param_function += f"args.{arg}"
                c += 1
                if c < function_info["argc"]:
                    param_function += ", "

            if_arg = "\tif args.command == \"{}\":\n\t\t{}.{}({})\n\treturn args".format(unction_info["name"], function_info["name"], function_info["name"], function_info["name"], param_function)
            
            delete_last_line("{}user/commands.py".format(jsonvar["userfolder"]))
            delete_last_line("{}user/args.py".format(jsonvar["userfolder"]))
            with open("{}user/commands.py".format(jsonvar["userfolder"]), 'a') as file:
                file.write(parser)

            with open("{}user/args.py".format(jsonvar["userfolder"]), 'a') as file:
                file.write(if_arg)

            with open("{}media/userdata.json".format(jsonvar["userfolder"]), 'r', encoding="utf-8") as file:
                data = json.load(file)
            data["userfunctions"].append(function_info["name"])
            with open("{}media/userdata.json".format(jsonvar["userfolder"]), 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4)
    else:
        raise ValueError("A python function start with \"def\".")
