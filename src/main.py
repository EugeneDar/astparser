import os

import numpy as np

from util import nth_substring
from parser import parse
from counter import count_allocations
from cpp_finder import get_cpps_list
from ast_builder import build_ast
from data_collector import collect
from preprocessor import preprocess

collect()

cpps = get_cpps_list("/data")

f = open('/result/results.csv', 'w')

f.write('objects_count, file_name, if_non_heap, if_heap, loop_non_heap, loop_heap, linear_non_heap, linear_heap, lines_count\n')

print('Cycle started')

for file in cpps:
    try:
        print('Start file:', file)
        preprocess(file)
        ast_name = build_ast(file)
        allocations = count_allocations(parse(ast_name))
        print(allocations)

        object_count = np.sum(allocations)

        if object_count == 0:
            continue

        curr_file = open(file, 'r')
        lines_count = len(curr_file.readlines())

        f.write(
            str(object_count) + ', ' +
            str(file[8:]) + ', ' +
            str(allocations[0, 0]) + ', ' +
            str(allocations[0, 1]) + ', ' +
            str(allocations[1, 0]) + ', ' +
            str(allocations[1, 1]) + ', ' +
            str(allocations[2, 0]) + ', ' +
            str(allocations[2, 1]) + ', ' +
            str(lines_count) + '\n'
        )

    except:
        print('Some error')

f.write('Finish')
f.close()
