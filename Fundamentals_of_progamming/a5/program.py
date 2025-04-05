#
# Write the implementation for A5 in this file
#

# 
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

from math import sqrt
import random
"""
def create(real,imaginary):
    return [real, imaginary]

def get_real(complex):
    return complex[0]

def get_imaginary(complex):
    return complex[1]

def set_real(complex, new_real):
    complex[0] = new_real

def set_imaginary(complex, new_imaginary):
    complex[1] = new_imaginary

def to_string(complex):
    if get_imaginary(complex) >= 0:
        return f"{get_real(complex)}+{get_imaginary(complex)}i"
    else:
        return f"{get_real(complex)}-{abs(get_imaginary(complex))}i"
        """

#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

def create(real,imaginary):
    return {'real': real, 'imaginary': imaginary}

def get_real(complex):
    return complex['real']

def get_imaginary(complex):
    return complex['imaginary']

def set_real(complex, new_real):
    complex['real'] = new_real

def set_imaginary(complex, new_imaginary):
    complex['imaginary'] = new_imaginary

def to_string(complex):
    if get_imaginary(complex) >= 0:
        return f"{get_real(complex)}+{get_imaginary(complex)}i"
    else:
        return f"{get_real(complex)}-{abs(get_imaginary(complex))}i"


#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def longest_subarray_of_distinct_numbers(lst):
    longest_subarray = []  #  the longest subarray found distinct numbers
    current_subarray = []  #  current subarray of distinct numbers

    for num in lst:
        # If num is already in the current subarray, remove elements until it’s unique
        while num in current_subarray:
            current_subarray.pop(0)  # Remove from the start to eliminate duplicates

        # Add the current number to the current subarray
        current_subarray.append(num)

        # Update longest_subarray if current_subarray is longer
        if len(current_subarray) > len(longest_subarray):
            longest_subarray = current_subarray[:]

    # Return the longest subarray and its length
    return longest_subarray, len(longest_subarray)

def modulus(complex):
    a = get_real(complex)
    b = get_imaginary(complex)
    modul = round(sqrt(a * a + b * b),2)
    return modul

def modules_list(list):
    n = len(list)
    modules = []
    for i in range(0, n):
        modules.append(modulus(list[i]))
    return modules


def longest_increasing_subsequence(arr):
    if not arr:
        return []

    subsequences = [[] for _ in range(len(arr))] #a list fo lists
    subsequences[0] = [to_string(arr[0])]


    for i in range(1, len(arr)):
        for j in range(i):
            # Check if the modulus of arr[j] is less than that of arr[i] and if adding arr[i] extends the longest subsequence ending at j
            if modulus(arr[j]) < modulus(arr[i]) and len(subsequences[j]) > len(subsequences[i]):
                subsequences[i] = subsequences[j].copy()
        subsequences[i].append(to_string(arr[i]))  # Append the current element to build the subsequence

    # Find the longest subsequence by comparing lengths
    longest_subsequence = max(subsequences, key=len)

    return longest_subsequence


#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
           
def print_list(list):
    if not list:
        print("The list is empty.")
    else:
        print("Complex numbers list:")
        for num in list:
            print(to_string(num))

def menu():
    print("Here is you menu.Please choose your option")
    print("1.Read a list of COMPLEX numbers")
    print("2.Show the list")
    print("3.Display the list with a property")
    print("4.Exit")
def start():
    """
    list = [[2, 3], [2, 3], [2, 0], [0, 1], [7, 2], [2, 3], [1, -1], [0, -5], [0, 0], [-5, -5]]
    """
    list = [{'real': 2, 'imaginary': 3}, {'real': 5, 'imaginary': 3}, {'real': 1, 'imaginary': 0}, {'real': 0, 'imaginary': 3},
               {'real': 2, 'imaginary': 3}, {'real': 2, 'imaginary': 3}, {'real': 2, 'imaginary': 3}, {'real': 2, 'imaginary': 3},
               {'real': 2, 'imaginary': 3}, {'real': 2, 'imaginary': 3}]

    """
    list=[]
    print("Generating 10 random complex numbers.")
    for i in range(10):
        real = random.randint(-100, 100)
        imaginary = random.randint(-100, 100)
        complexnr = create(real, imaginary)
        list.append(complexnr)
    """
    while True:
        menu()
        command=input("Enter your choice: ")
        if command =='1':
            print("1")
            n=int(input("Enter how many complex numbers: "))
            for _ in range(n):
                real = int(input("Enter the real part: "))
                imaginary = int(input("Enter the imaginary part: "))
                complexnr = create(real,imaginary)
                list.append(complexnr)

        elif command =='2':
                print_list(list)

        elif command =='3':
            command2=input("Enter propoerty 1 or 2: ")
            if command2=='1':
                print("Option 3.1: Display the longest subarray of distinct complex numbers.")
                longest_subarray, length = longest_subarray_of_distinct_numbers(list)
                print("The longest subarray of distinct complex numbers:")
                for complex_num in longest_subarray:
                    print(to_string(complex_num))

                print(f"Length: {length}")
            elif command2=='2':

                print(modules_list(list))
                result = longest_increasing_subsequence(list)
                print(f"The length of the longest increasing subsequence is {len(result)} ", "\n")
                print(f"The longest increasing subsequence is : ")
                for complex_num in result:
                    print(complex_num)

            else:
                print("Please choose a valid option")
        elif command =='4':
            print("You chose to exit the menu.Goodbye!")
            break
        else:
            print("Please choose a valid option")


start()




