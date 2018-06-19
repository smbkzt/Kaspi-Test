import re


def find_substring():
    with open("substring/INPUT.txt", 'r') as f:
        line = f.readline()

    number_of_substrings = len(re.findall("(aba)", line))

    with open("substring/OUTPUT.txt", 'w') as f:
        f.write(str(number_of_substrings))


if __name__ == "__main__":
    find_substring()
