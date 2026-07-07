from astNodes import *
from error import MeowError # <-- Updated to import from error.py

class Interpreter:
    def __init__(self):
        # memory storage to keep variables and values
        self.variables = {}

    def _get_value(self, val):
        # helper to find if the value is int or a variable lookup
        if isinstance(val, int):
            return val
        if isinstance(val, str):
            # if it is a string literal inside quotes, strip them and return the text
            if val.startswith('"') and val.endswith('"'):
                return val[1:-1]
            if val.isdigit():
                return int(val)
            
            if val not in self.variables:
                MeowError.lost_toy_error("Runtime", val)
                
            return self.variables.get(val, 0)
        return 0

    def check_condition(self, left, operator, right):
        # evaluates boolean expressions for sniff and zoomies
        if operator == ">": return left > right
        elif operator == "<": return left < right
        elif operator == "==": return left == right
        elif operator == ">=": return left >= right
        elif operator == "<=": return left <= right
        elif operator == "!=": return left != right
        return False

    def execute_body(self, body_nodes):
       # runs internal blocks for conditions and loops (if/while statements)
        for cmd in body_nodes:
            if isinstance(cmd, PrintNode):
                print(self._get_value(cmd.value))
            elif isinstance(cmd, AssignNode):
                left_val = self._get_value(cmd.left)
                right_val = self._get_value(cmd.right)
                
                res = 0
                if cmd.operator == "+": res = left_val + right_val
                elif cmd.operator == "-": res = left_val - right_val
                elif cmd.operator == "*": res = left_val * right_val
                elif cmd.operator == "/": 
                    if right_val == 0: MeowError.empty_bowl_error("Runtime")
                    res = left_val // right_val
                elif cmd.operator == "%": 
                    if right_val == 0: MeowError.empty_bowl_error("Runtime")
                    res = left_val % right_val
                self.variables[cmd.name] = res

    def run(self, nodes):
        # main loop that executes parsed AST nodes
        for node in nodes:
            if isinstance(node, VariableNode):
                if isinstance(node.value, str) and not node.value.isdigit() and not (node.value.startswith('"') and node.value.endswith('"')):
                    if node.value not in self.variables:
                        MeowError.lost_toy_error("Runtime", node.value)
                    self.variables[node.name] = self.variables.get(node.value, 0)
                else:
                    self.variables[node.name] = self._get_value(node.value)
            # print statement(meow)
            elif isinstance(node, PrintNode):
                print(self._get_value(node.value))
             # math assignments(exp. x=y+1)
            elif isinstance(node, AssignNode):
                left_val = self._get_value(node.left)
                right_val = self._get_value(node.right)
                
                result = 0
                if node.operator == "+": result = left_val + right_val
                elif node.operator == "-": result = left_val - right_val
                elif node.operator == "*": result = left_val * right_val
                elif node.operator == "/": 
                    if right_val == 0: MeowError.empty_bowl_error("Runtime")
                    result = left_val // right_val
                elif node.operator == "%": 
                    if right_val == 0: MeowError.empty_bowl_error("Runtime")
                    result = left_val % right_val
                self.variables[node.name] = result
            # selection statement (sniff-hiss)
            elif isinstance(node, IfNode):
                left_val = self.variables.get(node.variable, 0)
                right_val = self._get_value(node.value)
                
                if self.check_condition(left_val, node.operator, right_val):
                    self.execute_body(node.body)
                elif hasattr(node, 'else_body') and node.else_body:
                    self.execute_body(node.else_body)
            # loop statement (zoomies)  
            elif isinstance(node, WhileNode):
                while True:
                    left_val = self.variables.get(node.variable, 0)
                    right_val = self._get_value(node.value)
                    
                    if not self.check_condition(left_val, node.operator, right_val):
                        break
                    self.execute_body(node.body)