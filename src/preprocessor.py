# Step 3
# this file should preprocess all cpps:
# 1. wrap all includes by flags-variables

def preprocess(file_name):
    file1 = open(file_name, "r")

    while True:
        line = file1.readline()
        if not line:
            break
        print(line.strip())

    file1.close()
