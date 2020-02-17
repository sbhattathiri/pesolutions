import math


def get_list_of_prime_numbers_below_x(x):
    set_of_prime_factors = set()

    while x%2 == 0:
        set_of_prime_factors.add(2)
        x = x/2

    for divisor in range(3,int(math.sqrt(x))+1, 2):
        while x%divisor == 0:
            x = x/divisor
            set_of_prime_factors.add(divisor)

    if x > 2:
        set_of_prime_factors.add(x)

    return set_of_prime_factors


if __name__ == '__main__':
    set_of_prime_factors = get_list_of_prime_numbers_below_x(600851475143)
    print(max(set_of_prime_factors))
