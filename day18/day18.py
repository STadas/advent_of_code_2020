from pathlib import Path


def solve_multiple(expr, pre=None):
    do_op = {"*": lambda x, y: x + y, "+": lambda x, y: x * y}
    todo = []

    while pre in expr:
        num1 = int(expr.pop())
        op = expr.pop()

        if op == pre:
            expr.append(str(do_op[op](num1, int(expr.pop()))))
        else:
            todo.append(num1)
            todo.append(op)

    while len(todo) > 0:
        expr.append(todo.pop())

    while len(expr) > 1:
        num1 = int(expr.pop())
        op = expr.pop()
        num2 = int(expr.pop())
        expr.append(str(do_op[op](num1, num2)))

    return expr[0]


def xd():
    with open(str(Path(__file__).parent.absolute()) + "/input") as f:
        data = [line.split() for line in f.read().replace("(", "( ").replace(")", " )").splitlines()]

    p1, p2 = 0, 0
    for line in data:
        stack1, stack2 = [], []

        for c in line:
            if c.isnumeric() or c in ("(", "+", "*"):
                stack1.append(c)
                stack2.append(c)
            elif c == ")":
                ordered = []
                while stack1[-1] != "(":
                    ordered.append(stack1.pop())
                stack1.pop()
                stack1.append(solve_multiple(ordered))

                ordered = []
                while stack2[-1] != "(":
                    ordered.append(stack2.pop())
                stack2.pop()
                stack2.append(solve_multiple(ordered, "+"))

        p1 += int(solve_multiple(list(reversed(stack1))))
        p2 += int(solve_multiple(list(reversed(stack2)), "+"))

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
