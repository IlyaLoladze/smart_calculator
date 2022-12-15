from ckecking_correctness_part import check_symbols, check_brackets, check_all_numbers
from supported_characters import number_values, operation_values, open_bracket, \
    closed_bracket, operations_priority

number_values = number_values
operation_values = operation_values
open_bracket = open_bracket
closed_bracket = closed_bracket


def check_expression_for_correctness(expression):
    if check_symbols(expression) is False:
        return False, 'Incorrect symbols are used'
    elif check_brackets(expression) is False:
        return False, 'Wrong brackets placement'
    elif check_all_numbers(expression) is False:
        return False, 'Wrong number / numbers in expression'
    else:
        return True, ''


def calculate_expression(simple_operation):
    global operation_values
    operation_index = -1

    for i in range(len(simple_operation)):
        if simple_operation[i] in operation_values:
            operation_index = i
            break
    left_number = float(simple_operation[:i])
    right_number = float(simple_operation[i+1:])
    if simple_operation[i] == '+':
        return str(left_number + right_number)
    elif simple_operation[i] == '-':
        return str(left_number - right_number)
    elif simple_operation[i] == '/':
        return str(left_number / right_number)
    elif simple_operation[i] == '*':
        return str(left_number * right_number)
    else:  # simple_operation[i] == '^':
        return str(left_number ** right_number)


def get_most_priority_operation_index(operations_lst):  # [[1, '+'], [3, '^'] ...]
    global operations_priority
    chosen_operation = [-1, '']

    for el in operations_lst:
        if chosen_operation == [-1, '']:
            chosen_operation = el
        else:
            if operations_priority[el[1]] > operations_priority[chosen_operation[1]]:
                chosen_operation = el
    return chosen_operation[0]


def divide_and_calculate_expression(expression):
    global number_values
    global operation_values
    global open_bracket
    global closed_bracket
    operations_cnt = 0
    numbers_cnt = 0

    if expression[0] == open_bracket and expression[-1] == closed_bracket \
            and check_brackets(expression[1:-1]):
        expression = expression[1:-1]

    for el in expression:
        if el in number_values:
            numbers_cnt += 1

    for op in operation_values:
        operations_cnt += expression.count(op)

    if numbers_cnt == len(expression):
        return expression
    elif operations_cnt == 1:
        return calculate_expression(expression)
    else:
        cnt_open_brackets = 0
        cnt_closed_brackets = 0
        outside_operation_indexes = []
        for i in range(len(expression)):
            if expression[i] == open_bracket:
                cnt_open_brackets += 1
            elif expression[i] == closed_bracket:
                cnt_closed_brackets += 1
            elif expression[i] in operation_values and cnt_open_brackets == cnt_closed_brackets:
                outside_operation_indexes.append([i, expression[i]])
        oper_index = get_most_priority_operation_index(outside_operation_indexes)
        left_side = divide_and_calculate_expression(expression[:oper_index])
        right_side = divide_and_calculate_expression(expression[oper_index+1:])
        return divide_and_calculate_expression(left_side + expression[oper_index] + right_side)


def execute_program():
    while True:
        print('Write your expression:')
        expression = input().replace(' ', '').replace(',', '.')
        if expression == '':
            break
        is_correct, comment = check_expression_for_correctness(expression)
        if is_correct is False:
            print('The input expression is incorrect: ', comment)
        else:
            print('The answer:')
            print(divide_and_calculate_expression(expression))


if __name__ == '__main__':
    print('Welcome to SmartCalculator, which can find answers')
    print('for different mathematical expressions with multiple')
    print('operations like \'2 + 4 - (22^5 / 30 * 40)\'.')
    print('At the moment the program supports these operations:')
    print('  +  summing,\n  -  subtraction,\n  /  division,')
    print('  *  multiplication,\n  ^  and exponentiation.')
    print('-' * 35)
    print('to exit application press \'Enter\'')

    execute_program()
    print('finish')
