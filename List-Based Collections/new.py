
# Python 3 program to remove a given  
# element from an array 
  
# This function removes an element x  
# from arr[] and returns new size after  
# removal (size is reduced only when x  
# is present in arr[] 
def deleteElement(arr, n, x): 
      
    # Search x in array 
    for i in range(n): 
        if (arr[i] == x): 
            break
  
    # If x found in array 
    if (i < n): 
          
        # reduce size of array and move  
        # all elements on space ahead 
        n = n - 1; 
        for j in range(i, n, 1): 
            arr[j] = arr[j + 1] 
  
    return n 
  
# Driver Code 
if __name__ == '__main__': 
    arr = [11, 15, 6, 8, 9, 10] 
    n = len(arr) 
    x = 6
  
    # Delete x from arr[] 
    n = deleteElement(arr, n, x) 
  
    print("Modified array is") 
    for i in range(n): 
        print(arr[i], end = " ") 
    print('\narr final:', arr)
          
# This code is contributed by 
# Shashank_Sharma 