"""
Scoping example:
consider the following: the ide warns us that last_was_even variable might be
used before initialization. However, the code runs perfectly since the the scoping in Python
is local also from within the for-loop
"""
numbers = [1, 5, 6, 9, 2]


def count_even():
    even = 0
    for el in numbers:
        if el % 2 == 0:
            even += 1
            last_was_even = True
        else:
            last_was_even = False
    print("Last item was even? {}".format(last_was_even))
    return even


even_nums = count_even()
print(even_nums)
