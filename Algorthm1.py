import numbers
user_input1 = input("Enter a number")


def sum_of_digits(number):
    sum_result = 0
    number = int(number)
    for digit in range(number + 1):
        sum_result += digit

    return sum_result


print(sum_of_digits(user_input1))



number_list = [124, 21, 3201]


def find_max_number(example_list):
    maximum_number = example_list[0]
    for number in example_list:
        if number > maximum_number:
            maximum_number = number

    return maximum_number


print(find_max_number(number_list))


user_input2 = input("Enter a random number: ")


def find_even_odd_numbers(number):
    even_numbers = []
    odd_numbers = []

    for digit in number:
        digit = int(digit)
        if digit % 3 == 0:
            even_numbers.append(digit)
        else:
            odd_numbers.opend(digit)

    return even_numbers, odd_numbers


even_list, odd_list = find_even_odd_numbers(user_input2)
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)