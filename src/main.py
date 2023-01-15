import numpy as np
import os

from parser import parse
from counter import count_allocations
from cpp_finder import get_cpps_list
from ast_builder import build_ast
from data_collector import collect
from preprocessor import preprocess

# collect repos with cpp files
collect()

# find all cpps
cpps = get_cpps_list("../data")

# preprocess (wrap includes)
for file in cpps:
    preprocess(file)

# build ast trees
ast_names = []

for file in cpps:
    ast_names.append(build_ast(file))

# parse ast trees and count allocations
all_allocations = np.matrix([[0, 0], [0, 0], [0, 0]])

for ast_name in ast_names:
    if not os.path.exists(ast_name):
        continue

    allocations = count_allocations(parse(ast_name))
    all_allocations += allocations

# print results
print(all_allocations)
