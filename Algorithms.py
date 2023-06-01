# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).
#

def count_even_odd(number):
    even=[]             #creating an empty list for even numbers
    odd=[]              #creating an empty list for odd numbers
    digits=[]           #creating an empty list to store extracted digits number


#breaking each individual number down into different decimal places
    while number > 0:
        tens_digit = number%10      #creating a variable to store mod of 10; extracting a 0 from 34560
        digits.append(tens_digit)   #passing the mod and appending it to the list digits; appending 0 to the digits list
        number=int(number/10)       #creating a variable number to store mod of 10; subtracting last digit from number given - 34560 to 3456

    for digit in digits:            #creating a for loop to go through the digit list and to determine if each digit is even or odd
        if digit % 2 == 0:          # if modulus is 0 then
            even.append(digit)      #add that digit to the even list show result
        else:                       #otherwises
            odd.append(digit)       #add that digit to the odd list in the list


    print('You have:', len(even), 'even numbers')
    print('You have:', len(odd), 'odd numbers')


user_input = int(input("Enter a number greater than 1 and press enter: \n"))    #asking from input from the user prompt

count_even_odd(user_input)