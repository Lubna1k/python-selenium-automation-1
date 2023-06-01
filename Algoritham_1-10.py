##The Compute the sum of digits in all  numbers from 1 to n:
def fib(n):
    sum = 0
    for x in range(1, n+1):
        sum+=x
    return sum


##Numbers
number = int(input ("Enter a number greater than 1 and press enter: \n"))
my_fib = fib(number)
# my_fib = fib(9)
print ('The Fibonnacci result of the number your entered is', my_fib)
#print result