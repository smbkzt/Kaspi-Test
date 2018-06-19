"""
Петя успевает по математике лучше всех в классе, поэтому учитель задал ему
сложное домашнее задание, в котором нужно в заданном наборе целых чисел найти
сумму всех положительных элементов, затем найти где в заданной
последовательности находятся максимальный и минимальный элемент и вычислить
произведение чисел, расположенных между ними. Так же известно, что минимальный
и максимальный элемент встречаются в заданном множестве чисел только один раз.
Поскольку задач такого рода учитель дал Пете около ста, то Петя как сильный
программист смог написать программу, которая по заданному набору чисел
самостоятельно находит решение. А Вам слабо?
"""


def solve_homework(line):
    mult = 1

    numbers = [int(i) for i in line[1].split(" ")]
    sum_of_positive_num = sum([i for i in numbers if i > 0])

    index_of_max = numbers.index(max(numbers))
    index_of_min = numbers.index(min(numbers))
    if index_of_max > index_of_min:
        indexes_to_mult = range(index_of_min+1, index_of_max)
    else:
        indexes_to_mult = range(index_of_max+1, index_of_min)

    # numbers multiplication between max and min
    for i in indexes_to_mult:
        mult *= numbers[i]

    if (abs(sum_of_positive_num) or abs(mult)) > 3*104:
        raise ValueError("Incorrect input value")
    else:
        return sum_of_positive_num, mult


def main():
    with open("homework/INPUT.txt", 'r') as f:
        line = f.readlines()

    sum_of_positive_num, mult = solve_homework(line)

    with open("homework/OUTPUT.txt", 'w') as f:
        f.write("{} {}".format(sum_of_positive_num, mult))


if __name__ == "__main__":
    main()
