# Step 6
# this function should count all allocations via scopes
from parser import Type


def count_allocations(lines_list):
    # first - stack, second - heap
    if_allocations = [0, 0]
    loop_allocations = [0, 0]
    linear_allocations = [0, 0]

    print(lines_list)

    lineage = [True] * len(lines_list)

    for i in range(len(lines_list)):
        indent = lines_list[i][0]

        if lines_list[i][1] == Type.NEW_OPERATOR or lines_list[i][1] == Type.OTHER:
            continue

        if lines_list[i][1] == Type.VARIABLE_DECLARATION:
            if not lineage[i]:
                continue
            if i < len(lines_list) - 1 and lines_list[i + 1][1] == Type.NEW_OPERATOR:
                linear_allocations[1] += 1
            linear_allocations[0] += 1
            continue

        curr_scope_end = len(lines_list)
        for j in range(i + 1, len(lines_list)):
            if lines_list[j][0] <= indent:
                curr_scope_end = j
                break

        print(lines_list[i], i, curr_scope_end)

        var_counter = 0
        new_counter = 0
        for j in range(i, curr_scope_end):
            if lines_list[j][1] == Type.VARIABLE_DECLARATION:
                var_counter += 1
            if lines_list[j][1] == Type.NEW_OPERATOR:
                new_counter += 1

            lineage[j] = False

        if lines_list[i][1] == Type.IF:
            if_allocations[0] += var_counter
            if_allocations[1] += new_counter
        if lines_list[i][1] == Type.FOR or lines_list[i][1] == Type.WHILE:
            loop_allocations[0] += var_counter
            loop_allocations[1] += new_counter
        if lineage[i]:
            linear_allocations[0] += var_counter
            linear_allocations[1] += new_counter

    # print("IF ", if_allocations)
    # print("LOOP ", loop_allocations)
    # print("LINEAR", linear_allocations)
    return [if_allocations, loop_allocations, linear_allocations]
