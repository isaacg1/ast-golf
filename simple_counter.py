import sys
import ast
import tokenize
import io

with open(sys.argv[1], 'r') as f:
    code = f.read()

g = tokenize.tokenize(io.BytesIO(code.encode('utf-8')).readline)
for token in g:
    if len(token.string) > 15:
        print("Illegal token:", token.string)
        break
else:
    print(len(list(ast.walk(ast.parse(code)))))
