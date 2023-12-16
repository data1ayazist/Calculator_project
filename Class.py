class Calculator:
    def __init__(self):
        self.tokens = []
        self.stack = []
        self.OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}
# использование данного объекта было вдохновлено https://habr.com/ru/articles/273253/'
    def get_tokens(self, expr):
    # Разбиваем выражение на токены и добавляем их в список self.tokens 
        self.tokens = []
        num_str = ''
        prev_char = ''
        for char in expr:
            if char.isdigit() or char == '.':
                num_str += char
            elif char in ['+', '-', '*', '/', '**', '(', ')']:
                if num_str != '':
                    self.tokens.append(float(num_str))
                num_str = ''
                if prev_char in ['(', ''] and char == '-':
                    self.tokens.append(0.0)
                self.tokens.append(char)
            elif char  == ' ':
                pass
            else:
                raise ValueError('Некорректный символ в выражении')
            if char != ' ':
                prev_char = char
        if num_str != '':
            self.tokens.append(float(num_str))
        return self.tokens
# Реализация метода вдохновлена   'https://habr.com/ru/articles/273253/'
    def get_rpn(self):
        self.stack = []  # в качестве стэка используем список
        for token in self.tokens:
            if token in self.OPERATORS: 
                while self.stack and self.stack[-1] != "(" and self.OPERATORS[token][0] <= self.OPERATORS[self.stack[-1]][0]:
                    yield self.stack.pop()
                self.stack.append(token)
            elif token == ")":
                while self.stack:
                    x = self.stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                self.stack.append(token)
            else:
                yield token
        while self.stack:
            yield self.stack.pop()
    
    def evaluate(self): 
        stack = [] 
        for rpn_token in self.stack: 
            if isinstance(rpn_token,float) : 
                stack.append(rpn_token) 
            else: 
                right = stack.pop() 
                left = stack.pop() 
            if rpn_token == '+': 
                stack.append(left + right) 
            elif rpn_token == '-': 
                stack.append(left - right) 
            elif rpn_token == '*': 
                stack.append(left * right) 
            elif rpn_token == '/': 
                if right == 0:
                    raise ZeroDivisionError('На ноль делить нельзя')
                else:
                    stack.append(left / right) 
        return stack.pop() 
    
    def calc_string(self, expr):
        self.get_tokens(expr)
        self.stack = self.get_rpn()
        return self.evaluate()