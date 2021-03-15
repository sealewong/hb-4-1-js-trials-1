"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in the given array.

    Ex.:
    >>> outputAllItems([1, 'hello', true]);
    1
    hello
    true"""

    for item in items:
        print(item)


def get_all_evens(nums):
    """Given an array of numbers, return an array of all even numbers.

    Ex.:
    > getAllEvens([7, 8, 10, 1, 2, 2]);
    [8, 2, 2]"""

    even_numbers = []

    for num in nums:
        if num % 2 == 0:
            even_numbers.append(num)
    
    return even_numbers


def get_odd_indices(items):
    pass  # TODO: replace this line with your code


def print_as_numbered_list(items):
    pass  # TODO: replace this line with your code


def get_range(start, stop):
    pass  # TODO: replace this line with your code


def censor_vowels(word):
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
