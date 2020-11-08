import math


def jump_search(arr, x, n):
    # finding optimal steps
    step = math.sqrt(n)

    # finding the block that the element is in
    # if the block is found the loop breaks and goes into linear search
    prev = 0
    while arr[int(min(step, n) - 1)] < x:
        # skipping through the array with steps
        prev = step
        step += math.sqrt(n)
        # prev is bigger than n break the loop
        if prev >= n:
            return False

    # performing linear search on the previous block
    while arr[int(prev)] < x:
        prev += 1

        # if reached next block of the array
        # assume the element is not there
        if prev == min(step, n):
            return False

    # if the the wanted value is found then return the index
    if arr[int(prev)] == x:
        return int(prev)

    # if the element is not found at then end, it isnt here
    return False


arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
       34, 55, 89, 144, 233, 377, 610]
x = 55
n = len(arr)

# Find the index of 'x' using Jump Search
index = jump_search(arr, x, n)
print(f"Number: {x}, is at Index: {index}")
