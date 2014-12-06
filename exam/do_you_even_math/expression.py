from random import randint


class Expression:
    available_operations = ['+', '-', '*', '/', '^']

    def __init__(self, left_op, op, right_op):
        self.left_operand = left_op
        self.op = op
        self.right_operand = right_op

    @staticmethod
    def generate_expression():
        left_operand = randint(1, 10)
        oper = Expression.available_operations[randint(0, len(Expression.available_operations) - 1)]
        right_operand = randint(1, 10)
        expression = Expression(left_operand, oper, right_operand)
        return expression

    def solve_expression(self):
        if self.op == '+':
            self.result = self.left_operand + self.right_operand
        elif self.op == '-':
            self.result = self.left_operand - self.right_operand
        elif self.op == '*':
            self.result = self.left_operand * self.right_operand
        elif self.op == '/':
            self.result = self.left_operand / self.right_operand
        elif self.op == '^':
            self.result = self.left_operand ** self.right_operand
        return self.result

    def __str__(self):
        return str(self.left_operand) + ' ' + self.op + ' ' + str(self.right_operand)


def main():
    a = Expression.generate_expression()
    print(a)
    a.solve_expression()
    print(a.result)

if __name__ == '__main__':
    main()
