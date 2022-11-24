# Step 5
# this function should parse ast and return list
from enum import Enum


class Type(Enum):
    VARIABLE_DECLARATION = "VARIABLE DECLARATION"
    NEW_OPERATOR = "NEW OPERATOR"
    FOR = "FOR"
    WHILE = "WHILE"
    IF = "IF"
    OTHER = ""


def refactor_action_name(action_name):
    if action_name == "CXXNewExpr":
        return Type.NEW_OPERATOR
    if action_name == "VarDecl":
        return Type.VARIABLE_DECLARATION
    if action_name == "ForStmt":
        return Type.FOR
    if action_name == "WhileStmt":
        return Type.WHILE
    if action_name == "IfStmt":
        return Type.IF

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
