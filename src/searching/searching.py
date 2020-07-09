def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr) - 1
    mid = 0
  
    while start <= end:   
        mid = (start+end) // 2
  
        if arr[mid] < target: 
            start = mid + 1
        elif arr[mid] > target: 
            end = mid - 1
        else: 
            return mid 
  
    # If we reach here, then the element was not present 
    return -1