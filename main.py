def refactor_line(input_str):
    pos = input_str.find(next(filter(str.isalpha, input_str)))
    space = " " * pos
    formatted = input_str[pos:]
    formatted = formatted[:formatted.find(" ")]
    return space + formatted


file_name = "input/simple_loop.cpp"

file = open(file_name, "r")

while True:
    line = file.readline()
    if not line:
        break
    string = refactor_line(line.strip())
    print(string)
    # print(line.strip())

file.close()

