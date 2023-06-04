def split_and_swap(passed_string):
    half_string = len(passed_string) // 2
    if len(passed_string) % 2 == 1:
        half_string += 1

    first_half = passed_string[:half_string]
    second_half = passed_string[half_string:]

    first_half, second_half = second_half, first_half

    return first_half + second_half


# user_input = 'bbbbbcaaaaa'
# print(split_and_swap(user_input))


def has_unique_characters(passed_text):
    encountered_chars = set()
    for char in passed_text:
        if char in encountered_chars:
            return False
        encountered_chars.add(char)
    return True


user_text = 'abcde'
print(has_unique_characters(user_text))