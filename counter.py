import sys
import ast
with open(sys.argv[1], 'r') as f:
    code = f.read()

code_grid = code.split('\n')
loc_counts = [[0 for _ in line] for line in code.split('\n')]
def count(node):
    unallocated = 1
    total = 1
    for child in ast.iter_child_nodes(node):
        child_total, child_unallocated = count(child)
        unallocated += child_unallocated
        total += child_total
    try:
        loc_counts[node.lineno-1][node.col_offset] += unallocated
        return total, 0
    except AttributeError:
        return total, unallocated
total_count, unallocated = count(ast.parse(code))
print(total_count)
print('----------------------------')
for i in range(len(code_grid)):
    print(''.join(str(count) if count else ' 'for count in loc_counts[i]))
    print(code_grid[i])
