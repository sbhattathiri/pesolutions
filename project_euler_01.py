def get_list_of_multiple_of_3_but_not_5_below_x(x):
    multiples_of_3_but_not_5 = []
    for i in range(1, x):
        if i%3 == 0 and i%5 != 0:
            multiples_of_3_but_not_5.append(i)
    return multiples_of_3_but_not_5


def get_list_of_multiples_of_5_below_x(x):
    multiples_of_5 = []
    for i in range(1, x):
        if i%5 == 0:
            multiples_of_5.append(i)
    return multiples_of_5


def sum_of_multiples_of_3_and_5_below_x(x):
    list_of_multiple_of_3_but_not_5_below_x = get_list_of_multiple_of_3_but_not_5_below_x(x)
    list_of_multiples_of_5_below_x = get_list_of_multiples_of_5_below_x(x)
    sum_of_multiples_of_3_and_5 = sum(list_of_multiple_of_3_but_not_5_below_x, sum(list_of_multiples_of_5_below_x))
    return sum_of_multiples_of_3_and_5


if __name__ == '__main__':
    print(sum_of_multiples_of_3_and_5_below_x(1000))