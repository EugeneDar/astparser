# Step 5
# this function should parse ast and return list

class Object:
    def __init__(self, name):
        self.name = name
        self.nested_objects = []


def refactor_line(input_str):
    pos = input_str.find(next(filter(str.isalpha, input_str)))

    formatted = input_str[pos:]
    formatted = formatted[:formatted.find(" ")]

    if formatted == "CXXNewExpr":
        formatted = "new operator"
    elif formatted == "ForStmt":
        formatted = "For"
    elif formatted == "VarDecl":
        formatted = "Variable declaration"
    else:
        formatted = ""

    if formatted == "":
        ret = (0, "")
    else:
        ret = (pos * 2, formatted)

    return ret


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


# main function
def parse(filename):

