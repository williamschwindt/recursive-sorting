# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if end >= start:
        middle = (start + end) // 2

        if arr[middle] == target:
            return middle

        if arr[middle] < target:
            return binary_search(arr, target, middle + 1, len(arr)-1)

        elif arr[middle] > target:
            return binary_search(arr, target, 0, middle-1)
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

