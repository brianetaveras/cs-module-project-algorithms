'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    duplicates = []
    for i in arr:
        if i not in duplicates:
            duplicates.append(i)
        else:
            duplicates.remove(i)
    return duplicates[0]
        

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3,8, 8, 9, 0, 0, 7,7]

    print(f"The odd-number-out is {single_number(arr)}")