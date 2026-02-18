from math import isqrt
from typing import Iterable, Optional


def largest_prime(numbers: Iterable[int]) -> Optional[int]:
    """Return the largest prime number in `numbers`, or None if there isn't one."""

    # Convert to a list so we can handle single-pass iterables and empty inputs safely.
    number_list = list(numbers)

    # Immediately return None for empty inputs.
    if not number_list:
        return None

    def is_prime(value: int) -> bool:
        """Check primality efficiently using trial division up to sqrt(value)."""
        # Primes are integers greater than 1.
        if value < 2:
            return False

        # Handle the smallest prime directly.
        if value == 2:
            return True

        # Exclude even numbers greater than 2.
        if value % 2 == 0:
            return False

        # Test odd divisors only up to the integer square root.
        limit = isqrt(value)
        for divisor in range(3, limit + 1, 2):
            if value % divisor == 0:
                return False

        # No divisors found: value is prime.
        return True

    # Track the largest prime seen while scanning the input once.
    largest = None
    for num in number_list:
        if is_prime(num):
            if largest is None or num > largest:
                largest = num

    # If no prime was found, largest remains None.
    return largest


# Small example with input and output.
if __name__ == "__main__":
    sample_numbers = [10, 15, 17, 23, 42]
    print(f"Input: {sample_numbers}")
    print(f"Largest prime: {largest_prime(sample_numbers)}")  # Output: 23
