
def solve_homework():
    mult = 1

    with open("homework/INPUT.txt", 'r') as f:
        line = f.readlines()
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

    with open("homework/OUTPUT.txt", 'w') as f:
        f.write("{} {}".format(sum_of_positive_num, mult))


if __name__ == "__main__":
    solve_homework()
