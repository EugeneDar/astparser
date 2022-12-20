# Step 3
# this file should preprocess all cpps:
# 1. wrap all includes by flags-variables
import random

def preprocess(file_name):
    # reading
    file1 = open(file_name, "r")
    lines = []

    while True:
        line = ''
        try:
            line = file1.readline()
        except:
            continue

        if not line:
            break

        if '#include ' in line:
            lines.append('int INCLUDE_SECTION_START_FLAG_' + str(random.randint(0, 2_000_000_000)) + ' = 0;\n')
            lines.append(line)
            lines.append('int INCLUDE_SECTION_FINISH_FLAG_' + str(random.randint(0, 2_000_000_000)) + ' = 0;\n')
        else:
            lines.append(line)

    file1.close()

    # writing
    file1 = open(file_name, "w")

    for line in lines:
        file1.write(line)

    file1.close()
