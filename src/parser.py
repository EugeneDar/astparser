# Step 5
# this function should parse ast and return list

class Object:
    def __init__(self, name):
        self.name = name
        self.nested_objects = []


def refactor_action_name(action_name):
    if action_name == "CXXNewExpr":
        return "new operator"
    if action_name == "VarDecl":
        return "Variable declaration"
    if action_name == "ForStmt":
        return "For"
    if action_name == "IfStmt":
        return "If"
    if action_name == "":
        return ""
    if action_name == "":
        return ""
    if action_name == "":
        return ""

    return ""


def refactor_line(input_str):
    pos = input_str.find(next(filter(str.isalpha, input_str)))

    formatted = input_str[pos:]
    formatted = formatted[:formatted.find(" ")]

    action_name = refactor_action_name(formatted)

    if action_name == "":
        return [0, ""]
    else:
        return [pos, action_name]


def refactor_all_lines(filename):
    file = open(filename, "r")

    lines_list = []

    while True:
        line = file.readline()
        if not line:
            break
        pair = refactor_line(line.strip())
        if pair[1] != "":
            lines_list.append(pair)

    file.close()
    return lines_list


def parse(filename):
    lines = refactor_all_lines(filename)
    return lines
