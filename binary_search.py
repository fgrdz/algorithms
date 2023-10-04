def binary_search (arr, element):
  # initialization of variables
  # right is set to the length of the list minus 1 (the end of the list)
  left, right = 0, len(arr) -1 

  # a while loop that continues as long as left is less than or equal to right.
  while left <= right:
    mid = (left + right) // 2

    # calculation of the middle 
    if arr[mid] == element:
      return mid
    
    # discard half of the list
    elif arr[mid]> element:
      right = mid -1
    # discard the other half of the list  
    else:
      left = mid +1
    
  return -1

list_ord = [1,2,3,4,5,6,7,8,9,10,11]
element = 9

print(f'the element {element} founded in position: {binary_search(list_ord, element)}')
      
  