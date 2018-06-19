"""
Требуется найти самую длинную непрерывную цепочку нулей в последовательности
нулей и единиц.
"""
import re


def find_nulls(line):
    if len(line) > 100:
        raise ValueError("Too big length of numbers: %d" % len(line))

    null_number = [len(i) for i in re.findall(r"[0]{2,}", line)]
    max_null_number = max(null_number)

    return max_null_number


def main():
    with open("nulls/INPUT.txt", 'r') as f:
        line = f.readline()

    null_number = find_nulls(line)

    with open("nulls/OUTPUT.txt", 'w') as f:
        f.write("%d" % null_number)


if __name__ == "__main__":
    main()
