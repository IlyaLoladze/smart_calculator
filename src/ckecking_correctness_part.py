from supported_characters import number_values, operation_values, open_bracket, closed_bracket
number_values = number_values
operation_values = operation_values
open_bracket = open_bracket
closed_bracket = closed_bracket


def check_symbols(text):
    global number_values
    global operation_values
    global open_bracket
    global closed_bracket

    for i in range(len(text)):
        if text[i] not in number_values and text[i] not in operation_values \
                and text[i] != open_bracket and text[i] != closed_bracket:
            return False
    return True


def check_brackets(text):
    global open_bracket
    global closed_bracket
    cnt_open_brackets = 0
    cnt_closed_brackets = 0

    for i in range(len(text)):
        if text[i] == open_bracket:
            cnt_open_brackets += 1
        elif text[i] == closed_bracket:
            cnt_closed_brackets += 1
            if cnt_closed_brackets > cnt_open_brackets:
                return False

    return cnt_open_brackets == cnt_closed_brackets


def check_numbers_part(numbers_part, is_integer_part=True):
    if is_integer_part:
        return numbers_part == '0' or 0 < len(numbers_part) < 10 and numbers_part[0] != '0'
    return 0 < len(numbers_part) < 10


def check_number(number_text):
    dot_index = number_text.find('.')

    if dot_index == -1:
        return check_numbers_part(number_text)
    elif number_text.count('.') > 1:
        return False
    else:
        return check_numbers_part(number_text[:dot_index]) and check_numbers_part(number_text[dot_index + 1:], False)


def check_all_numbers(text):
    global number_values
    start_number = -1

    for i in range(len(text)):
        if text[i] in number_values:
            if start_number == -1:
                start_number = i
            if i == len(text) - 1:
                if check_number(text[start_number:]) is False:
                    return False
        elif start_number != -1:
            # numer ended and we check it separately
            if check_number(text[start_number:i]) is False:
                return False
            start_number = -1
    return True


def сheck_operations(text):
    global number_values
    global operation_values
    global open_bracket
    global closed_bracket

    for i in range(len(text)):
        if text[i] == '-':
            pass
        elif text:
            pass
    return True
