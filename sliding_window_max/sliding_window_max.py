'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    max_arr = []
    start = 0
    end = len(nums)
    for i in range(end):
        window = nums[start:start+k]
        if len(window) < k:
            continue
        max_arr.append(max(nums[start:start + k]))
        start += 1
  
    return max_arr
        



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1,3,-1,-3,5,3,6,7]
    # [3,3,5,5,6,7] 
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
