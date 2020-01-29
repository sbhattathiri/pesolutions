def sum_square_difference(n):
    sum_of_squares = sum(num**2 for num in range(1,(n+1)))
    square_of_sum = (sum(num for num in range(1, (n+1))))**2
    difference = square_of_sum - sum_of_squares
    return difference

if __name__ == '__main__':
    print(sum_square_difference(100))