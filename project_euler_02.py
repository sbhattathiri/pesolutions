def get_sum_of_even_fibonacci_numbers_below_x(x):
    sum_of_even_fibonacci_numbers = 0
    begin, next_in_seq = 1, 2
    while next_in_seq < x:
        begin, next_in_seq = next_in_seq, (begin + next_in_seq)
        if begin%2 == 0:
            sum_of_even_fibonacci_numbers += begin
    return sum_of_even_fibonacci_numbers


if __name__ == '__main__':
    print(get_sum_of_even_fibonacci_numbers_below_x(4000000))