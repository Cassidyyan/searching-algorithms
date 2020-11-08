# Searches through a list one item at a time, while looking for demanded item


def linear_search(arr, x):
    # iterating through the indexes of a array
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return False


# testing
arr = [1, 2, 3, 4, 5, 6, 7, 8, 11, "t"]
x = 1
result = linear_search(arr, x)

if result:
    print(f"element could be found" + "\n" + "Index: " + str(linear_search(arr,x)))

else:
    print("element is not present")



