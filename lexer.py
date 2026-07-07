import re
from token import Token
from error import MeowError

class Lexer:
    def __init__(self, source_code):
        self.source = source_code
        self.tokens = []
        # grammar and keyword rules for MeowLang
        self.spec = [
            (r'\s+', None),  # skips spaces and new lines
            (r'kitten\b', 'VARIABLE'),
            (r'meow\b', 'PRINT'),
            (r'zoomies\b', 'WHILE'),
            (r'sleep\b', 'END'),
            (r'sniff\b', 'IF'), 
            (r'hiss\b', 'ELSE'), 
            (r'"[^"\n]*"', 'STRING'),  # rule for matching string literals
            (r'[0-9]+', 'NUMBER'),
            (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),
            (r'==', 'OPERATOR'),
            (r'>=', 'OPERATOR'),
            (r'<=', 'OPERATOR'),
            (r'!=', 'OPERATOR'),
            (r'=', 'OPERATOR'),
            (r'\+', 'OPERATOR'),
            (r'-', 'OPERATOR'),
            (r'\*', 'OPERATOR'),
            (r'/', 'OPERATOR'),
            (r'%', 'OPERATOR'),
            (r'>', 'OPERATOR'),
            (r'<', 'OPERATOR'),
        ]
        # combines regex rules into a single pattern
        pattern = '|'.join(f'(?P<g_{i}>{regex})' for i, (regex, _) in enumerate(self.spec))
        self.regex = re.compile(pattern, re.DOTALL)

    def tokenize(self):
        line_no = 1
        pos = 0
        source_len = len(self.source)
        
        while pos < source_len:
            match = self.regex.match(self.source, pos)
            if not match:
                MeowError.hairball_error(line_no, "Invalid character or broken cat syntax.")
            
            group_name = match.lastgroup
            index = int(group_name.split('_')[1])
            
            token_type = self.spec[index][1]
            value = match.group()
            
            if token_type is None:
                line_no += value.count('\n')
                pos = match.end()
                continue
                
            if token_type == 'NUMBER':
                value = int(value)
                
            self.tokens.append(Token(token_type, value, line_no, 1))
            pos = match.end()
            
        return self.tokens