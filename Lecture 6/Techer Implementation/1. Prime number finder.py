def check_prime_number(number):
    if number == 0:
        return False

    # A number is prime if it's only divisible by 1 and itself.
    # More efficient approach: a number is not prime if it exists a divisor different from 1 and itself
    for i in range(1, number+1):
        # Skip 1 and itself
        if i == 1 or i == number:
            continue

        # Check dividend
        if (number % i) == 0:
            # This number is not prime! We found a divisor different from 1 and itself
            return False

    # If the function has not returned so far, it means that the for evaluated all the possible divisor and
    # never found divisors. So it's prime!
    return True


def calculate_numbers_to_check(upper_limit):
    prime_numbers = []
    for i in range (1, upper_limit+1):
        if check_prime_number(i):
            prime_numbers.append(i)
    return prime_numbers


def process_user_input(user_input):
    if user_input == 'q':
        return False
    elif user_input.isdigit():
        limit = int(user_input)
        prime_numbers = calculate_numbers_to_check(limit)
        print(prime_numbers)
        return True
    else:
        print("Invalid option chosen.")
        return True


def user_menu():
    print("Welcome to prime number finder")
    while True:
        user_input = input("Please specify the integer limit, or 'q' to exit:")
        ask_again = process_user_input(user_input)
        if not ask_again:
            print("Bye bye!")
            break


user_menu()
