# Step 6
# this function should count all allocations via scopes

def count_allocations(lines_list):
    # first - stack, second - heap
    if_allocations = [0, 0]
    loop_allocations = [0, 0]
    linear_allocations = [0, 0]

    for i in range(len(lines_list)):
        indent = lines_list[i][0]

        curr_scope_end = i
        for j in range(i + 1, len(lines_list)):
            if lines_list[j][0] >= indent:
                curr_scope_end = j
                break
