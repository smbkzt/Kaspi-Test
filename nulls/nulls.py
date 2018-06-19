import re


def find_nulls():
    with open("nulls/INPUT.txt", 'r') as f:
        line = f.readline()
    null_number = [len(i) for i in re.findall(r"[0]{2,}", line)]
    max_null_number = max(null_number)

    with open("nulls/OUTPUT.txt", 'w') as f:
        f.write(str(max_null_number))


if __name__ == "__main__":
    find_nulls()
