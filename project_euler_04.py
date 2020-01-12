def is_number_palindrome(number):
    number_as_string = str(number)
    reversed_number_as_string = number_as_string[::-1]
    if number_as_string == reversed_number_as_string:
        return True
    return False


def get_largest_palindrome_product():
    nums = {}
    largest = 0
    for a in range(999, 100, -1):
        for b in range(999, 100, -1):
            product = a*b
            if is_number_palindrome(product):
                if product > largest:
                    largest = product
                    nums['a'] = a
                    nums['b'] = b
                    nums['product'] = product

    return nums


if __name__ == '__main__':
    print(get_largest_palindrome_product())