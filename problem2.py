"""

## Problem 2 ~ Two Sum
You are given a list `nums` and an integer `target`. Return the indeces of the elements from `n` that sum to `target`.
### Example 1
`nums = [2, 5, 3, 7, 3, 8]`

`target = 12`

#### Output:
`[1, 3]`

#### Explanation:
If we take the element at index `1`, which is **5** and the element at index `3` which is **7**, it sums to **12**.
`nums[1] + nums[3] == 5 + 7 == 12`

### Test Cases
| Input                                          | Output |
| ---------------------------------------------- | ------ |
| `nums = [2, 5, 3, 7, 3, 8]` <br> `target=12`   | `1, 3` |
| `nums = [2, 5, 3, 7, 3, 8]` <br> `target=10`   | `2, 3` |
| `nums = [1, 5, 3, 1, 5, 1]` <br> `target=12`   | `None` |
| `nums = [0, 0, 0, 0]` <br> `target=0`          | `0, 1` |
| `nums = [1]` <br> `target=1`                   | `None` |
| `nums = [1, 3, 2, 42, 1]` <br> `target=42`     | `None` |
| `nums = []` <br> `target=42`                   | `None` |

"""


def two_sum(numbers: list[int], target: int) -> list[int] | None:
    """
    Find and return the indices of two elements in a list of integers that add up to a given target value.

    Parameters
    ----------
    numbers : List of int
        A list of integers to search for a pair that sums up to `target`.
    target : int
        The target value that the pair of elements should sum up to.

    Returns
    -------
    indices : List of int or None
        A list containing the indices of the two elements in the input list `numbers` that add up to the target sum.
        If no such pair exists, the function returns `None`.
    """

    seen = {}
    for i, num in enumerate(numbers):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
            # return f"{seen[diff]}, {i}" # if we want to return in the same format as the test cases
        seen[num] = i
    return None


if __name__ == "__main__":
    print(two_sum([2, 5, 3, 7, 3, 8, 2, 5, 3, 7, 3, 8], 12))
    print(two_sum([2, 5, 3, 7, 3, 8], 10))
    print(two_sum([1, 5, 3, 1, 5, 1], 12))
    print(two_sum([0, 0, 0, 0], 0))
    print(two_sum([1], 1))
    print(two_sum([1, 3, 2, 42, 1], 42))
    print(two_sum([], 42))
    print(two_sum([1, 1, 3, 5, 3, 1, 3], 10))
    print(two_sum([3, 2, 5, 2, 4], 6))
