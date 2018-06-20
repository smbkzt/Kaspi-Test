
def get_num_of_methods(number):
    if number in [2, 3]:
        return number - 1
    elif number == 0 or number == 1:
        return 0
    elif number > 3:
        a = 3
        methods = 2
        for i in range(4, number+1):
            b = a * (i-1)
            a = b + methods
            methods = b
        return methods


def main():
    with open("birthday/INPUT.txt", 'r') as f:
        number = int(f.readline())

    methods = get_num_of_methods(number)

    with open("birthday/OUTPUT.txt", 'w') as f:
        f.write("%d" % methods)


if __name__ == "__main__":
    main()
