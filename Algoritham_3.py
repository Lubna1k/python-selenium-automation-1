def numbers_below_arithmetical_mean(passed_list):
    # Create an empty list to store numbers below the arithmetical mean
    below_mean_list = []

    # Calculate the arithmetical mean of the list
    arithmetical_mean = sum(passed_list) / len(passed_list)

    # Iterate over each number in the list
    for number in passed_list:
        # Check if the number is below the arithmetical mean
        if number < arithmetical_mean:
            # Add the number to the below_mean_list
            below_mean_list.append(number)

    # Return the list of numbers below the arithmetical mean
    return below_mean_list


# Example usage
example_list = [1, 3, 5, 6, 4, 10, 2, 3]
print(numbers_below_arithmetical_mean(example_list))



def two_lowest_numbers(used_list):
    # Initialize the lowest number and second-smallest number with the first element of the list
    lowest_number = used_list[0]
    second_smallest_number = used_list[0]

    # Iterate over each number in the list
    for number in used_list:
        # Check if the number is lower than the current lowest number
        if number < lowest_number:
            # Update the second-smallest number as the previous lowest number
            second_smallest_number = lowest_number
            # Update the lowest number with the new lowest number
            lowest_number = number
        # Check if the number is lower than the current second-smallest number and not equal to the lowest number
        elif number < second_smallest_number and number != lowest_number:
            # Update the second-smallest number with the new second-smallest number
            second_smallest_number = number

    # Return the lowest number and second-smallest number as a tuple
    return lowest_number, second_smallest_number


# Example usage
example_list2 = [198, 3, 4, 9, 10, 9, 2]
print(two_lowest_numbers(example_list2))