file_name = "input/simple_loop.cpp"

file = open(file_name, "r")

while True:
    line = file.readline()
    if not line:
        break
    print(line.strip())

file.close()

