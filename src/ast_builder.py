# Step 4
# this function should build ast
import os

def build_ast(source_name):
    output_name = '../input' + source_name.lstrip('../data')
    command = 'clang++ -Xclang -ast-dump -fsyntax-only ' + source_name + ' > ' + output_name
    os.system(command)
