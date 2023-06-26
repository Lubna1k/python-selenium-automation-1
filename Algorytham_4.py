def even_numbers_first(numbers):
    left_index = 0
    right_index = len(numbers) - 1

    while left_index < right_index:
        if numbers[left_index] % 2 == 0:
            left_index += 1
        else:
            numbers.append(numbers[left_index])
            del numbers[left_index]
            right_index -= 1

    return numbers

test_numbers = [7, 3, 5, 6, 4, 10, 3, 2]
print(even_numbers_first(test_numbers))


def increment_integer(digits):
    carry = 1
    for i in range(len(digits)-1, -1, -1):
        digits[i] += carry
        if digits[i] < 10:
            carry = 0
            break
        else:
            digits[i] = 0
    if carry == 1:
        digits.insert(0, 1)
    return digits


test_digits = [1, 2, 9]
print(increment_integer(test_digits)) # [1, 3, 0]
