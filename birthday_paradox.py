import random


def birthday_paradox(num_people, num_trials):
    """
    Simulate the birthday paradox by randomly generating birthdays for a number of people
    and checking if any two people share the same birthday.

    :param num_people: Number of people to simulate
    :param num_trials: Number of trials to run
    :return: The number of trials where at least two people share a birthday over the total number of trials
    """

    num_shared_birthdays = 0

    for _ in range(num_trials):
        # Generate random birthdays for 23 people
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        # Check if there are any shared birthdays
        if len(birthdays) != len(set(birthdays)):
            num_shared_birthdays += 1

    return num_shared_birthdays / num_trials