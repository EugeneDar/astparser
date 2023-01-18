import os

import numpy as np

from util import nth_substring
from parser import parse
from counter import count_allocations
from cpp_finder import get_cpps_list
from ast_builder import build_ast
from data_collector import collect
from preprocessor import preprocess

# todo add loging here
collect()

projects = set()
cpps = get_cpps_list("../data")

for file in cpps:
    pos = nth_substring(file, '/', 4)
    projects.add(file[:pos])

os.system('touch results.txt')
f = open('results.txt', 'w')

for project_name in projects:
    all_allocations = np.matrix([[0, 0], [0, 0], [0, 0]])

    for file in cpps:
        if not file.startswith(project_name):
            continue

        try:
            preprocess(file)
            allocations = count_allocations(parse(build_ast(file)))
            all_allocations += allocations
        except:
            print('Some error')

    object_count = np.sum(all_allocations)

    result = {'objects_count': object_count, 'project_name': project_name[8:],
              'if_non_heap': all_allocations[0, 0], 'if_heap': all_allocations[0, 1],
              'loop_non_heap': all_allocations[1, 0], 'loop_heap': all_allocations[1, 1],
              'linear_non_heap': all_allocations[2, 0], 'linear_heap': all_allocations[2, 1]}
    print(result, file=f)

f.close()
print('Finished')
while True:
    a = 1 + 1
