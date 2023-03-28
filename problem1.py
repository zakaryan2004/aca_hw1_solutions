"""

## Problem 1 ~ Find the Duplicates
Given an unsorted list of numbers (integers) `n`, find and print all the duplicates in the list.

### Test Cases
| Input                    | Output |
| ------------------------ | ------ |
| `n = [5, 1, 2, 1, 4,]`   | `1`    |
| `n = [4, 1, 2]`          | `None` |
| `n = []`                 | `None` |
| `n = [6, 2, 5, 2, 6, 2]` | `2 6` |
| `n = [42, 42, 42, 42]`   | `42`   |

Think of the data structures used and try to implement an optimal solution for the problem.

_Additionally:_ Add comments on the complexity analysis of the implementation (Big-O).


Complexity Analysis:
--------------------
Time Complexity: O(n)
The time complexity of this algorithm is O(n) because we are iterating through the list once,
and all of the operations we are doing are constant time operations.
element in set is O(1) in sets
set.add(num) is amortized O(1)
Space Complexity: O(n)

"""


def duplicate(numbers: list[int]) -> set[int] | None:
    """
    Find and return all the duplicate elements in a list of integers.

    Parameters
    ----------
    numbers : list of int
        A list of integers to check for duplicates.

    Returns
    -------
    duplicates : set of int or None
        A set of duplicate elements in the input list `numbers`. If there are no duplicates, the function returns `None`.

    """
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return duplicates or None


if __name__ == "__main__":
    print(duplicate([5, 1, 2, 1, 4]))
    print(duplicate([4, 1, 2]))
    print(duplicate([]))
    print(duplicate([6, 2, 5, 2, 6, 2]))
    print(duplicate([42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]))
