def linearsearch(arr, num):
    # iterate through elements
    for i in range(len(arr)):
        # check if element is number we're looking for
        if arr[i] == num: 

            return i
            
    return -1 

