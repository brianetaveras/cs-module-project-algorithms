'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    mutated_arr = []
    for i in arr:
        if i == 0:
            mutated_arr.append(i)
        else:
            mutated_arr.insert(0, i)

    return mutated_arr
            


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")