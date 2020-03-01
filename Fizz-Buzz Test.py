# A solution for the Fizz-Buzz test using lists

# Test: Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”. For numbers which
# are multiples of both three and five print “FizzBuzz”.

multiple_3 = list(range(3, 101, 3))
multiple_5 = list(range(5, 101, 5))

for number in range(1, 101):
    if number in multiple_3:
        if number in multiple_5:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif number in multiple_5:
        print("Buzz")
    else:
        print(number)
