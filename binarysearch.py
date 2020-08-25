def binarysearch(arr, num):
    # set pointers
    low = 0 
    
    high = len(arr) - 1
    # make sure whole list hasn't been checked
    while low <= high:
        # get the middle number
        mid = (low + high) // 2

        if arr[mid] == num:

            return mid
        # reset pointer
        elif arr[mid] > num:

            high = mid - 1 
        # reset pointer
        else:

            low = mid + 1

    return -1 