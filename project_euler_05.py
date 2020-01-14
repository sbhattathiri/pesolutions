import math


def get_lcm_of_first_n_natural_numbers(n):
    divisors = list(range(1,n))
    for num in range(1, math.factorial(n)):
        if all(num%divisor == 0 for divisor in divisors):
            return num
    return None


if __name__ == '__main__':
    print(get_lcm_of_first_n_natural_numbers(20))