from typing import List
from random import shuffle


def sort_bubble(array: List[int]) -> List[int]:
    result = array.copy()
    length = len(result)

    for iteration in range(length):
        for base_idx in range(length-iteration-1):
            if result[base_idx] > result[base_idx+1]:
                result[base_idx], result[base_idx+1] = result[base_idx+1], result[base_idx]

    return result



if __name__ == "__main__":
    array = [i for i in range(100)]
    shuffle(array)
    result = sort_bubble(array)
    print(f"Original: {array}")
    print(f"Sorted: {result}")
