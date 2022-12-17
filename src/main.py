from parser import parse
from counter import count_allocations
from cpp_finder import get_cpps_list
from ast_builder import build_ast
from data_collector import collect



# collect repos with cpp files
collect()



# find all cpps
cpps = get_cpps_list()



# preprocess (wrap includes)
# todo



# build ast trees
ast_names = []

for file in cpps:
    ast_names.append(build_ast(file))



# parse ast trees and count allocations
all_allocations = [0, 0, 0]

for ast_name in ast_names:
    allocations = count_allocations(parse(ast_name))
    all_allocations[0] += allocations[0]
    all_allocations[1] += allocations[1]
    all_allocations[2] += allocations[2]



# print results
print(all_allocations)
