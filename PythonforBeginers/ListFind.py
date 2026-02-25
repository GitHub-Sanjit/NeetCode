from typing import List  # this is used to add type hints for List type


def find_index(nums: List[int], target: int) -> int:
    ind = 0
    for n in nums:
        if n == target:
            break
        ind += 1
    return ind


# don't modify code below this line
print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5, 3], 3))
print(find_index([1, 2, 3, 4], 1))
print(find_index([1, 3, 4, 2], 2))
