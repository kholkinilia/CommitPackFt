def move_one_ball(arr):
    """
    This function moves the smallest value to the end of the array.
    """
    if len(arr)==0:
      return True
    sorted_array=sorted(arr)
    my_arr=[]
    
    min_value=min(arr)
    min_index=sorted_array.index(min_value)
    my_arr=arr[min_index:]+arr[0:min_index]
    for i in range(len(arr)):
      if my_arr[i]!=sorted_array[i]:
        return False
    return True