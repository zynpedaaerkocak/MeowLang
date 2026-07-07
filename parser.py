from astNodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        nodes = []
        while self.position < len(self.tokens):
            token = self.tokens[self.position]
            
            # handles variable declaration (kitten keyword)
            if token.type == "VARIABLE":
                name = self.tokens[self.position + 1].value
                # check if it is an inline math assignments (exp. x=a*b)
                if self.position + 4 < len(self.tokens) and self.tokens[self.position + 4].value in ["+", "-", "*", "/", "%"]:
                    left = self.tokens[self.position + 3].value
                    operator = self.tokens[self.position + 4].value
                    right = self.tokens[self.position + 5].value
                    nodes.append(AssignNode(name, left, operator, right))
                    self.position += 6
                else:
                    value = self.tokens[self.position + 3].value
                    nodes.append(VariableNode(name, value))
                    self.position += 4
                # handles print statement (meow keyword)
            elif token.type == "PRINT":
                value = self.tokens[self.position + 1].value
                nodes.append(PrintNode(value))
                self.position += 2
                # handle standalone re-assignments (exp. count = count - 1)
            elif token.type == "IDENTIFIER":
                name = token.value
                if self.position + 1 < len(self.tokens) and self.tokens[self.position + 1].value == "=":
                    left = self.tokens[self.position + 2].value
                    operator = self.tokens[self.position + 3].value
                    right = self.tokens[self.position + 4].value
                    nodes.append(AssignNode(name, left, operator, right))
                    self.position += 5
                else:
                    self.position += 1
                 # handles conditional block (sniff keyword)
            elif token.type == "IF": #'sniff' means IF
                variable = self.tokens[self.position + 1].value
                operator = self.tokens[self.position + 2].value
                value = self.tokens[self.position + 3].value
                self.position += 4
                # parses the main if body until hitting sleep or hiss
                body = []
                while self.position < len(self.tokens) and self.tokens[self.position].type not in ["END", "ELSE"]:
                    curr_token = self.tokens[self.position]
                    if curr_token.type == "PRINT":
                        body.append(PrintNode(self.tokens[self.position + 1].value))
                        self.position += 2
                    elif curr_token.type == "IDENTIFIER" and self.position + 1 < len(self.tokens) and self.tokens[self.position + 1].value == "=":
                        body.append(AssignNode(curr_token.value, self.tokens[self.position + 2].value, self.tokens[self.position + 3].value, self.tokens[self.position + 4].value))
                        self.position += 5
                    else:
                        self.position += 1
                # reads the else block if hiss keyword is found
                else_body = []
                if self.position < len(self.tokens) and self.tokens[self.position].type == "ELSE": #'hiss' means 'ELSE'
                    self.position += 1 
                    while self.position < len(self.tokens) and self.tokens[self.position].type != "END":
                        curr_token = self.tokens[self.position]
                        if curr_token.type == "PRINT":
                            else_body.append(PrintNode(self.tokens[self.position + 1].value))
                            self.position += 2
                        elif curr_token.type == "IDENTIFIER" and self.position + 1 < len(self.tokens) and self.tokens[self.position + 1].value == "=":
                            else_body.append(AssignNode(curr_token.value, self.tokens[self.position + 2].value, self.tokens[self.position + 3].value, self.tokens[self.position + 4].value))
                            self.position += 5
                        else:
                            self.position += 1
                
                if_node = IfNode(variable, operator, value, body)
                if_node.else_body = else_body
                nodes.append(if_node)
                
                if self.position < len(self.tokens) and self.tokens[self.position].type == "END":
                    self.position += 1
                # parse loop block (zoomies keyword)
            elif token.type == "WHILE":
                variable = self.tokens[self.position + 1].value
                operator = self.tokens[self.position + 2].value
                value = self.tokens[self.position + 3].value
                self.position += 4
                #read the block until seeing sleep
                body = []
                while self.position < len(self.tokens) and self.tokens[self.position].type != "END":
                    curr_token = self.tokens[self.position]
                    if curr_token.type == "PRINT":
                        body.append(PrintNode(self.tokens[self.position + 1].value))
                        self.position += 2
                    elif curr_token.type == "IDENTIFIER" and self.position + 1 < len(self.tokens) and self.tokens[self.position + 1].value == "=":
                        body.append(AssignNode(curr_token.value, self.tokens[self.position + 2].value, self.tokens[self.position + 3].value, self.tokens[self.position + 4].value))
                        self.position += 5
                    else:
                        self.position += 1
                        
                nodes.append(WhileNode(variable, operator, value, body))
                if self.position < len(self.tokens) and self.tokens[self.position].type == "END":
                    self.position += 1
            else:
                self.position += 1
        return nodes