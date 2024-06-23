# Binary search example
def binary_search(arr, target):
    # Setup 2 pointers on left and right of the dataset, then moving from left to right, element by element
    left, right = 0, len(arr) - 1

    while left <= right:
        # Take the remaining div as the new pointer
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example usage:
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 7

result = binary_search(my_list, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
