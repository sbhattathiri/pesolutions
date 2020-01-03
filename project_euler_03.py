import math


def get_list_of_prime_numbers_below_x(x):
    list_of_prime_factors = []
    for divident in range(2, x):
        for divisor in range(2, (int)(math.sqrt(divident)+1)):
            if divident%divisor == 0:
                break
        else:
            list_of_prime_factors.append(divident)
    return list_of_prime_factors


if __name__ == '__main__':
    list_of_prime_factors = get_list_of_prime_numbers_below_x(600851475143)
    print(list_of_prime_factors[-1])