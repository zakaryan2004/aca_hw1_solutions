"""

## Problem 3 ~ Greatest Common Divisor
Create a function that takes an arbitrary number of integers (2 or more) and uses 
the [Euclidean Algorithm](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm)
to compute the greatest common divisor (GCD) for those numbers.

The (GCD)[https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-expressions-and-variables/cc-6th-gcf/v/greatest-common-divisor] 
of 2 numbers is defined as the highest number that divides both of the numbers exactly.

The GCD of more than 2 numbers can be calculated using factoring as follows: `GCD(a, b, c) = GCD(GCD(a, b), c)`

### Example 1
`gcd(24, 36, 16)`

#### Output:
`4`

#### Explanation:
`GCD(24, 36, 16) = GCD(GCD(24, 36), 16) = GCD(12, 16) = 4)`

### Test Cases
| Input               | Output  |
| ------------------- | ------- |
| `gcd(24, 36, 16)`   | `4`     |
| `gcd(24, 36)`       | `12`    |
| `gcd(24)`           | `Error` |
| `gcd()`             | `Error` |

**Note:** Python has an implementation of GCD in the Standard Library. Please refrain from using it for this exercise.

"""


def gcd_helper(a, b) -> int:
    """
    Helper function that computes the gcd of two integers using the Euclidean Algorithm.

    Parameters
    ----------
    a : int
        First integer.
    b : int
        Second integer.

    Returns
    -------
    int
        The GCD of the two input integers.

    """
    if b == 0:
        return abs(a)

    return gcd_helper(b, a % b)


def gcd(*numbers: int) -> int:
    """
    Compute the greatest common divisor of an arbitrary number of integers.

    Parameters
    ----------
    numbers : Tuple of int
        A tuple of integers to compute the GCD of.

    Returns
    -------
    gcd : int
        The greatest common divisor of the input numbers.

    """
    if len(numbers) < 2:
        raise ValueError("At least 2 numbers are required to compute the GCD.")

    if len(numbers) == 2:
        return gcd_helper(numbers[0], numbers[1])

    return gcd(gcd_helper(numbers[0], numbers[1]), *numbers[2:])


if __name__ == "__main__":
    print(gcd(24, 36, 16))
    print(gcd(24, 36))
    print(gcd(-24, -4))
    print(gcd(5, 0))
    print(gcd(24))
    print(gcd())
