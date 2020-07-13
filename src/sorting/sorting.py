# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    index_a = 0
    index_b = 0

    for i in range(len(merged_arr)):
        if index_a >= len(arrA) and index_b >= len(arrB):
            return merged_arr
        elif index_a >= len(arrA):
            merged_arr[i] = arrB[index_b]
            index_b += 1
        elif index_b >= len(arrB):
            merged_arr[i] = arrA[index_a]
            index_a += 1
        elif arrA[index_a] <= arrB[index_b]:
            merged_arr[i] = arrA[index_a]
            index_a += 1
        else:
            merged_arr[i] = arrB[index_b]
            index_b += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    #base case single int array
    if len(arr) <= 1:
        return arr

    else:
        #find the middle and split into two arrays
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        #call merge sort on both halves
        left_sort = merge_sort(left)
        right_sort = merge_sort(right)

        #call merge with both arrays
        return merge(left_sort, right_sort)



# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

