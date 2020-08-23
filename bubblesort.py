def bubblesort(arr):
    # store length of array
    length = len(arr) 
    # to keep track of how many elements are already sorted
    for i in range(length):
        # to iterate over the list and sort
        for j in range(length-i):

            a = arr[j]
            # check if at the end of the list
            if a != arr[-1]:
                
                b = arr[j+1]
                # compare with next element of the array
                if a > b:
                    # swap
                    arr[j], arr[j+1] = b, a 

    return arr

