"""
A simple, well-commented random number generator.

This script can:
- Generate a single random integer in a range
- Generate a single random floating-point number in a range
- Generate multiple numbers (ints or floats) at once

Run it directly or import the functions from other code.
"""

import random
from typing import List, Literal

# Define a type for the number kind we support: integer or float
NumberKind = Literal["int", "float"]


def random_int(min_value: int, max_value: int) -> int:
    """
    Generate a single random integer between min_value and max_value (inclusive).

    Args:
        min_value: The lowest integer to possibly return.
        max_value: The highest integer to possibly return.

    Returns:
        A random integer in [min_value, max_value].
    """
    # randint includes both endpoints
    return random.randint(min_value, max_value)


def random_float(min_value: float, max_value: float) -> float:
    """
    Generate a single random floating-point number between min_value and max_value.

    Args:
        min_value: The lowest float to possibly return.
        max_value: The highest float to possibly return.

    Returns:
        A random float uniformly distributed in [min_value, max_value].
    """
    # random.random() returns [0.0, 1.0); scale and shift into [min_value, max_value]
    return min_value + (max_value - min_value) * random.random()


def generate_many(kind: NumberKind, count: int, min_value: float, max_value: float) -> List[float]:
    """
    Generate a list of random numbers of the specified kind.

    Args:
        kind: "int" for integers, "float" for floating-point numbers.
        count: How many numbers to generate.
        min_value: Minimum value (int or float). For ints, will be cast to int.
        max_value: Maximum value (int or float). For ints, will be cast to int.

    Returns:
        A list containing `count` random numbers.
    """
    # Validate inputs early to prevent confusing results
    if count <= 0:
        raise ValueError("count must be a positive integer")
    if min_value > max_value:
        raise ValueError("min_value must be <= max_value")

    results: List[float] = []

    if kind == "int":
        # Ensure bounds are integers for integer generation
        imin = int(min_value)
        imax = int(max_value)
        for _ in range(count):
            results.append(random_int(imin, imax))
    elif kind == "float":
        for _ in range(count):
            results.append(random_float(float(min_value), float(max_value)))
    else:
        raise ValueError("kind must be either 'int' or 'float'")

    return results


def _print_examples() -> None:
    """
    Print a few example generations for quick visual testing.
    """
    print("Examples: \n")

    # Single int
    print("Single int [1, 10]:", random_int(1, 10))

    # Single float
    print("Single float [0.0, 1.0]:", random_float(0.0, 1.0))

    # Many ints
    print("Five ints [10, 20]:", generate_many("int", 5, 10, 20))

    # Many floats
    print("Five floats [1.5, 2.5]:", generate_many("float", 5, 1.5, 2.5))


if __name__ == "__main__":
    # If run directly, show examples and a minimal CLI.
    # Using argparse provides a simple command line interface.
    import argparse

    parser = argparse.ArgumentParser(
        description="Basic random number generator (ints or floats)")
    parser.add_argument(
        "--kind",
        choices=["int", "float"],
        default="int",
        help="Type of number to generate",
    )
    parser.add_argument(
        "--min",
        type=float,
        default=0,
        help="Minimum value (inclusive)",
    )
    parser.add_argument(
        "--max",
        type=float,
        default=100,
        help="Maximum value (inclusive for ints)",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="How many numbers to generate",
    )
    parser.add_argument(
        "--examples",
        action="store_true",
        help="Print a few example outputs",
    )

    args = parser.parse_args()

    if args.examples:
        _print_examples()
    else:
        # Generate requested numbers and print them line-by-line
        numbers = generate_many(args.kind, args.count, args.min, args.max)
        for n in numbers:
            print(n)
