class Calculator:
    def __init__(self):
        self.stack = []
        self.operations = ['+', '-', '*', '/']

    @staticmethod
    def _calculation(a, b, opr):
        if opr == '+':
            return a + b
        elif opr == '-':
            return a - b
        elif opr == '*':
            return a * b
        elif opr == '/':
            return a / b

    def calculator(self, string):
        for s in string:
            if s == ')':
                b = self.stack.pop()
                opr = self.stack.pop()
                a = self.stack.pop()
                del self.stack[-1]

                self.stack.append(self._calculation(int(a), int(b), opr))
            else:
                self.stack.append(s)

        return self.stack.pop()


cal = Calculator()
print(cal.calculator("((3*(4+2))-5)"))
print(cal.calculator("3*(4+2)-5"))
print(cal.calculator("3(4+2)-5"))
# 42+3*5-

