def  backtracking(sequence, current_subset,current_sum,index):
    # conidition for the valid subset
    if len(current_subset)>0 and current_sum % len(sequence)==0:
        print(current_subset)

    for i in range(index, len(sequence)):
        # Include the current element in the subset
        backtracking(sequence, current_subset + [sequence[i]],current_sum+sequence[i], i + 1)


def iterative(sequence):
    current_subset = []
    current_sum = 0
    index = 0

    #when current_subset is empty and there are no more elements to backtrack =stop
    while True:
        # If index is within the length of the sequence , we can add the current element to x
        if index < len(sequence):
            # Add the next element to the current subset
            current_subset.append(sequence[index])
            current_sum =current_sum+sequence[index]
            if len(current_subset)>0 and current_sum%len(sequence)==0:
                print(current_subset)

            index =index+ 1
        else:
            # If we have exceeded the sequence length
            if not current_subset:
                break  # If current subset is empty stop

            last_element = current_subset[-1]  # practiacally,it "undos" the last step it did
            current_sum =current_sum-last_element
            index = sequence.index(last_element) + 1  # Move to the next element after the current one

            # Remove the last element since we are backtracking
            current_subset= current_subset[:-1]



number_of_elements = int(input("Enter the number of elements in the sequence: "))
numbers = [int(x) for x in input(f"Enter {number_of_elements} distinct integers: ").split()[:number_of_elements]]
backtracking(numbers, [], 0,0)

print("-------")
iterative(numbers)
#Time complexity is O(2^n) because there can be a maximum of 2^n subsets