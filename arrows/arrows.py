"""
Задана последовательность, состоящая только из символов ‘>’, ‘<’ и ‘-‘.
Требуется найти количество стрел, которые спрятаны в этой последовательности.
Стрелы – это подстроки вида ‘>>-->’ и ‘<--<<’.
"""

import re


def find_arrows(line):
    if len(line) > 250:
        raise ValueError("The line is too big.")

    arrow_right_number = len(re.findall(r"(?=(>>-->))", line))
    arrow_left_number = len(re.findall(r"(?=(<--<<))", line))

    return arrow_right_number + arrow_left_number


def main():
    with open("arrows/INPUT.txt", 'r') as f:
        line = f.readline()

    arrow_num = find_arrows(line)

    with open("arrows/OUTPUT.txt", 'w') as f:
        f.write("%d" % arrow_num)


if __name__ == "__main__":
    main()
