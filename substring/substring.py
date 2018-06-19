"""
Строка S была записана много раз подряд, после чего из получившейся строки
взяли подстроку и дали Вам. Ваша задача определить минимально возможную длину
исходной строки S.
"""

import re


def find_substring(line):
    if len(line) > 5000:
        raise ValueError("The line is too big")

    return len(re.findall("(aba)", line))


def main():
    with open("substring/INPUT.txt", 'r') as f:
        line = f.readline()
    substr_num = find_substring(line)
    with open("substring/OUTPUT.txt", 'w') as f:
        f.write("%d" % substr_num)


if __name__ == "__main__":
    main()
