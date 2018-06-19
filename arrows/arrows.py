import re


def find_arrows():
    with open("arrows/INPUT.txt", 'r') as f:
        line = f.readline()
    arrow_right_number = len(re.findall(r"(?=(>>-->))", line))
    arrow_left_number = len(re.findall(r"(?=(<--<<))", line))

    total_arrows_number = arrow_right_number + arrow_left_number

    with open("arrows/OUTPUT.txt", 'w') as f:
        f.write(str(total_arrows_number))


if __name__ == "__main__":
    find_arrows()
