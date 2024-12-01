# Lambda functions

add_two = lambda my_input: my_input + 2

# <WHAT TO RETURN IF STATEMENT IS TRUE> if <IF STATEMENT> else <WHAT TO RETURN IF STATEMENT IS FALSE>
is_substring = lambda my_string: my_string in "This is the master string"

# T/F check if the  letter a is in the input word.
contains_a = lambda word: True if 'a' in word else False

# T/F check to see if the input string is longer than 12 characters.
long_string = lambda str: True if len(str) > 12 else False

# T/F check to see if the last letter of the input string is a
ends_in_a = lambda str: True if str[-1] is 'a' else False

# Takes number checks to see if its greater than  10, doubles it if it is, otherweise returns 0
double_or_zero = lambda num: num * 2 if num > 10 else 0

# Even or odd checker
even_or_odd = lambda num: 'even' if num%2 == 0 else 'odd'

# Multiple of three checker
multiple_of_three = lambda num: 'multiple of three' if num % 3 == 0 else 'not a multiple'

# Rating checker - Lambdas return booleans
rate_movie = lambda rating: 'I liked this movie' if rating > 8.5 else 'This movie was not very good'

# Finding the last digit in a number
ones_place = lambda num: num % 10

# Mathematical operations
double_square = lambda num: (num ** 2) * 2

# Add a number plus a random integer from a range defined in random.randint
add_random = lambda num: num + random.randint(1, 10)
