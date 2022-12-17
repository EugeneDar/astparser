# Step 4
# this function should build ast
import os
import random

def build_ast(source_name):
    output_name = '../input/' + os.path.basename(source_name) + '___' + str(random.random())
    print(output_name)
    command = 'clang++ -Xclang -ast-dump -fsyntax-only ' + source_name + ' > ' + output_name
    os.system(command)
    return output_name
