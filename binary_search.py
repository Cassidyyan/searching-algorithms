# It returns index of x in given arry if present
# Divide and conquer searching algorithm
# else returns false


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        # finding midpoint
        mid = (high + low) // 2

        # check if x is bigger than the mid number
        if arr[mid] < x:
            low = mid + 1

        # check if x is smaller than the mid number
        elif arr[mid] > x:
            high = mid - 1

        # if the number is mid, return that number
        else:
            return mid

    # If function returns false then the number was not in the list
    return False


# testing
arr = [1, 2, 3, 4, 5, 6, 7, 8]
x = 8

# Function call
result = binary_search(arr, x)

if result:
    print("Element could be found")

else:
    print("Element cannot be found")
