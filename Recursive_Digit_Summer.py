def sum_of_digits(number):
    return number%10+sum_of_digits(number//10) if number!=0 else 0
