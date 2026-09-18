"""
Tutorial 1: The Loop & Conditional Dungeon
===========================================

Welcome, adventurer! You've stumbled into a dungeon full of half-broken
spells. Each function below almost works, but a small bug is standing
between you and treasure. Your job is NOT to write this code from
scratch -- it's already here! You just need to find and fix each bug.

Learning Objectives:
- Practice reading and debugging for/while loops
- Practice reading and debugging if/elif/else conditionals
- Practice nested conditionals and logical operators (and/or/not)
- Build confidence tracing through code line-by-line

Instructions:
- Every bug is marked with a "TODO" comment and a "Hint" right above it.
- Fix ONLY what the TODO asks you to fix -- the rest of the code works!
- Run the program using: uv run dungeon.py
- Check the "Expected" comment next to each print() call to confirm success.
"""


def classify_number(num):
    """
    Decide whether a number is positive, negative, or zero.

    Args:
        num (int): the number to classify

    Returns:
        str: "positive", "negative", or "zero"
    """
    # TODO: This condition mislabels 0 as "positive". Fix the comparison
    # Hint: zero is not greater than zero -- use > instead of >=
    if num >= 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"


def secret_door(door):
    """
    Choose a door and discover what's behind it.

    Args:
        door (str): the chosen door, e.g. "red", "blue", "green"

    Returns:
        str: a message describing what's behind the door
    """
    if door == "red":
        return "🔥 You found a treasure chest!"
    # TODO: This spelling mistake means the blue door never matches
    # Hint: compare against "blue", not "blu"
    elif door == "blu":
        return "🌊 You discovered a hidden underwater tunnel!"
    elif door == "green":
        return "🌲 You entered a magical forest!"
    else:
        return "❌ That door doesn't exist!"


def countdown_blaster(start):
    """
    Count down from `start` to 1, collecting each number in a list.

    Args:
        start (int): the number to count down from

    Returns:
        list: the numbers counted down, e.g. [3, 2, 1]
    """
    countdown = []
    count = start

    # TODO: This while loop never ends because `count` never changes
    # Hint: decrease count by 1 somewhere inside the loop body (count -= 1)
    while count > 0:
        countdown.append(count)

    return countdown


def print_even_numbers(limit):
    """
    Build a list of every even number from 2 up to and including `limit`.

    Args:
        limit (int): the highest number to consider

    Returns:
        list: the even numbers found
    """
    even_numbers = []

    # TODO: This range starts and steps incorrectly, so it collects odd numbers
    # Hint: start at 2 (not 1) and step by 2: range(2, limit + 1, 2)
    for number in range(1, limit + 1, 2):
        even_numbers.append(number)

    return even_numbers


def is_prime_check(number):
    """
    Determine whether `number` is prime using a for/else loop.

    Args:
        number (int): the number to test (assume number >= 3 and odd)

    Returns:
        bool: True if prime, False otherwise
    """
    # TODO: Stepping by 3 skips most possible factors, so this misfires
    # Hint: divisors of an odd number can only be odd, so step by 2, not 3
    for i in range(3, number, 3):
        if number % i == 0:
            return False
    return True


def combo_lock(entered_a, entered_b, correct_a, correct_b):
    """
    Check whether both halves of a two-part combo code are correct.

    Args:
        entered_a (int): first number entered
        entered_b (int): second number entered
        correct_a (int): correct first number
        correct_b (int): correct second number

    Returns:
        bool: True only if BOTH halves match
    """
    # TODO: Using "or" lets the lock open with only one correct half
    # Hint: a combo lock needs BOTH halves right -- use "and" instead of "or"
    if entered_a == correct_a or entered_b == correct_b:
        return True
    return False


def treasure_room(has_key, is_locked):
    """
    Decide what happens when you enter the treasure room.

    Args:
        has_key (bool): whether the adventurer is holding the key
        is_locked (bool): whether the door is locked

    Returns:
        str: a message describing the outcome
    """
    if is_locked:
        # TODO: "not has_key" checks the opposite of what we want here
        # Hint: we want to reward the adventurer when they DO have the key
        if not has_key:
            return "🔑 You unlock the door and find a mountain of gold!"
        else:
            return "🚪 The door is locked and you have no key. Dead end!"
    else:
        return "🏆 The door was already open -- treasure for the taking!"


def main():
    """
    Run every dungeon challenge and print the results.
    """
    print("\n" + "=" * 60)
    print("Tutorial 1: The Loop & Conditional Dungeon")
    print("=" * 60)

    print("\n[Room 1] Classifying numbers...")
    for n in [-5, 0, 5]:
        print(f"  classify_number({n}) -> {classify_number(n)}")
    # Expected: negative, zero, positive

    print("\n[Room 2] Choosing a door...")
    print(f"  secret_door('blue') -> {secret_door('blue')}")
    # Expected: 🌊 You discovered a hidden underwater tunnel!

    print("\n[Room 3] Countdown blaster...")
    print(f"  countdown_blaster(3) -> {countdown_blaster(3)}")
    # Expected: [3, 2, 1]

    print("\n[Room 4] Even numbers up to 10...")
    print(f"  print_even_numbers(10) -> {print_even_numbers(10)}")
    # Expected: [2, 4, 6, 8, 10]

    print("\n[Room 5] Prime checks...")
    for n in [9, 11, 15, 17]:
        print(f"  is_prime_check({n}) -> {is_prime_check(n)}")
    # Expected: False, True, False, True

    print("\n[Room 6] Combo lock...")
    print(f"  combo_lock(4, 2, 4, 7) -> {combo_lock(4, 2, 4, 7)}")
    print(f"  combo_lock(4, 7, 4, 7) -> {combo_lock(4, 7, 4, 7)}")
    # Expected: False, True

    print("\n[Room 7] Treasure room...")
    print(f"  treasure_room(has_key=True, is_locked=True) -> "
          f"{treasure_room(True, True)}")
    # Expected: 🔑 You unlock the door and find a mountain of gold!

    print("\n" + "=" * 60)
    print("If every result above matches its Expected comment, you win!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
