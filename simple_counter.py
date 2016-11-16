import sys
import ast
with open(sys.argv[1], 'r') as f:
    code = f.read()

print(len(list(ast.walk(ast.parse(code)))))
