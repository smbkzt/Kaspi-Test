"""
Необходимо сократить дробь, записанную в римской системе счисления. Напомним,
что в римской записи используются символы M, D, C, L, X, V и I. Приведем
таблицу с примерами перевода римских чисел в арабскую систему:
"""


class IncorrectInputValue(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.logger()

    def logger(self):
        with open("rome_numbers/OUTPUT.txt", "w") as f:
            f.write("ERROR")


letterValues = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


def get_values(ch):
    num = letterValues.get(ch.upper(), "")
    if not isinstance(num, int):
        raise IncorrectInputValue(
            "There is no number like that: %s" % ch)
    else:
        return num


def convert_from_roman(number):
    result = 0
    lastValue = 0
    for ch in number:
        value = get_values(ch)
        if value > lastValue:
            result += value - 2 * lastValue
        else:
            result += value
        lastValue = value

    if result > 999:
        raise IncorrectInputValue("The number is too big: %d" % result)
    else:
        return result


def convert_to_roman(num):
    roman = ''

    while num > 0:
        for i, r in letterValues.items():
            while num >= r:
                roman += i
                num -= r
    return roman


def find_nod(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def main():
    with open("rome_numbers/INPUT.txt", 'r') as f:
        line = f.readline()
    if len(line) > 100:
        raise IncorrectInputValue

    first_num, second_num = line.split("/")
    first_num = convert_from_roman(first_num)
    second_num = convert_from_roman(second_num)
    nod = find_nod(first_num, second_num)

    f_n = convert_to_roman(first_num/nod)
    s_n = convert_to_roman(second_num/nod)

    with open("rome_numbers/OUTPUT.txt", 'w') as f:
        if s_n == "I":
            f.write(str(f_n))
        else:
            f.write("%s/%s" % (f_n, s_n))


if __name__ == "__main__":
    main()
