class VariableNode:
    # holds data when a new variable is created with(kitten)
    def __init__(self, name, value):
        self.name = name
        self.value = value

class PrintNode:
    #  holds data when we want to print something with (meow)
    def __init__(self, value):
        self.value = value

class AssignNode:
    # handles variable assignments and calculations
    def __init__(self, name, left, operator, right):
        self.name = name
        self.left = left
        self.operator = operator
        self.right = right

class IfNode:
    # node for sniff and hiss conditional structures
    def __init__(self, variable, operator, value, body, else_body=None):
        self.variable = variable
        self.operator = operator
        self.value = value
        self.body = body
        self.else_body = else_body if else_body else []

class WhileNode:
    # nope for loop structures(zoomies)
    def __init__(self, variable, operator, value, body):
        self.variable = variable
        self.operator = operator
        self.value = value
        self.body = body