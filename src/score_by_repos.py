import numpy as np
import os

from parser import parse
from counter import count_allocations
from cpp_finder import get_cpps_list
from ast_builder import build_ast
from data_collector import collect
from preprocessor import preprocess

# remove old data
command = "rm -rf ../data && mkdir ../data && rm -rf ../input && mkdir ../input"
os.system(command)

# collect repos with cpp files
repos = collect()

for repo in repos:
    cpps = get_cpps_list(repo)

    for file in cpps:
        preprocess(file)

    ast_names = []

    for file in cpps:
        ast_names.append(build_ast(file))

    all_allocations = np.matrix([[0, 0], [0, 0], [0, 0]])

    for ast_name in ast_names:
        if not os.path.exists(ast_name):
            continue

        allocations = count_allocations(parse(ast_name))
        all_allocations += allocations

    f = open('logs.txt', "a")
    f.write(repo + '\n')
    f.write(str(all_allocations) + '\n\n')
    f.close()

