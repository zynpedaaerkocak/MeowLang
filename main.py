# main file to execute everything
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

with open("program.meow", "r", encoding="utf-8") as f:
    code = f.read()

#step 1:run the lexer to go get tpkens
lexer = Lexer(code)
tokens = lexer.tokenize()
print("TOKENS:")
for t in tokens:
    print(t)

#step 2:run the parser to get AST nodes
parser = Parser(tokens)
nodes = parser.parse()

#step3: pass nodes into the interpreter
interpreter = Interpreter()
print("\nOUTPUT:")
interpreter.run(nodes)