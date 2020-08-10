def is_op(token):
    return token in ['+', '-', '*', '/']


def eval_op(op, arg1, arg2):
    if op == '+':
        return arg1 + arg2
    if op == '-':
        return arg1 - arg2
    if op == '*':
        return arg1 * arg2
    if op == '/':
        return arg1 / arg2

# This implementation assumes that the input is correctly tokenized. 
# For example an input string like + 1 would result in an index out of bounds
def eval_tokens(tokens, index):
    token = tokens[index]
    if is_op(token):
        arg1, index = eval_tokens(tokens, index + 1)
        arg2, index = eval_tokens(tokens, index + 1)
        return eval_op(token, arg1, arg2), index
    else:
        return int(token), index


def eval(input):
    tokens = input.split(" ")
    result, _ = eval_tokens(tokens, 0)
    return result


def assertEqual(actual, expected):
    if (actual == expected):
        print("OK")
    else:
     print("BAD!!")


def test(input, expected):
    assertEqual(eval(input), expected)


def main():
    test("3", 3)
    test("+ 3 5", 8)
    test("+ 1 * 2 31", 63)
    test("+ * 1 2 3", 5)
    test("/ 10 3", 10 / 3)


main()
