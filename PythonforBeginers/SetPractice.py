from typing import List

def contains_duplicate(words: List[str]) -> bool:
    length_list = len(words)
    new_set = set(words)
    length_set = len(new_set)
    if length_list == length_set:
        return False
    else:
        return True

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
