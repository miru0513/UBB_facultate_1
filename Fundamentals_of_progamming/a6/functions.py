#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#
import random
from webbrowser import Error
from winreg import error


import functools



def create_contestant(p1,p2,p3):
    """
    :param p1: grade for first solution
    :param p2: grade for second solution
    :param p3: grade for third solution
    :return: the contestant created
    """
    return [p1,p2,p3]

def getp1(contestant):
    return contestant[0]

def getp2(contestant):
    return contestant[1]

def getp3(contestant):
    return contestant[2]

def setp1(contestant,new_p1):
    contestant[0]=new_p1

def setp2(contestant,new_p2):
    contestant[1]=new_p2

def setp3(contestant,new_p3):
    contestant[2]=new_p3

def to_str(contestant):
    return "P1:"+ str(contestant[0]) + " P2:"+ str(contestant[1]) + " P3:"+ str(contestant[2])


def add_new_contestant(p1,p2,p3):
    """
        Adds a new contestant's scores to the list if they are within a valid range (0-10).

        :param p1: Score of the first contestant (should be between 0 and 10)
        :param p2: Score of the second contestant (should be between 0 and 10)
        :param p3: Score of the third contestant (should be between 0 and 10)
        :return: List containing the valid scores of the new contestant
        """
    list=[]
    if int(p1) > 10 or int(p1) < 0:
        raise error(f'Error! There should be a numbere between 0 and 10!')
    else:
        list.append(p1)
    if int(p2) > 10 or int(p2) < 0:
        raise error(f'Error! There should be a numbere between 0 and 10!')
    else:
        list.append(p2)
    if int(p3) > 10 or int(p3) < 0:
        raise error(f'Error! There should be a numbere between 0 and 10!')
    else:
        list.append(p3)
    return list


def insert_new_contestant(v, p1, p2, p3, pos):
    """
    Inserts a new contestant's scores into a list at a specified position.

    :param v: List of contestants (list of lists)
    :param p1: Score of the first contestant (should be between 0 and 10)
    :param p2: Score of the second contestant (should be between 0 and 10)
    :param p3: Score of the third contestant (should be between 0 and 10)
    :param pos: Position in the list where the new contestant should be inserted
    :return: Updated list of contestants with the new contestant inserted
    """
    new_contestant = []

    for score in [p1, p2, p3]:
        try:
            score = int(score)  # Convert score to integer
            if score < 0 or score > 10:
                raise ValueError("Score should be between 0 and 10.")
            new_contestant.append(score)
        except ValueError as e:
            print(f"Error: {e}")
            return v  # Return original list if error occurs

    try:
        pos = int(pos)  # Convert position to integer
        if pos < 0 or pos > len(v):
            raise IndexError("Index out of range.")
        v.insert(pos, new_contestant)
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

    return v


def remove_contestant(v, pos):
    """
    Removes a contestant from the list at the specified position.

    :param v: List of contestants
    :param pos: Position in the list where the contestant should be removed
    :return: Updated list of contestants after removal
    :raises IndexError: If the position is out of range
    """
    try:
        pos = int(pos)  # Ensure pos is an integer
    except ValueError:
        raise ValueError("Position is not a number.")

    # Check if position is valid
    if pos < 0 or pos >= len(v):
        raise IndexError("Position is out of range!")

    # Remove the contestant at the specified position
    v.pop(pos)
    return v  # Return the updated list after removal



def remove_contestant_range(v, start_pos, end_pos):
    """
    Removes contestants from the list in a specified range.

    :param v: List of contestants
    :param start_pos: Starting position in the list (inclusive)
    :param end_pos: Ending position in the list (inclusive)
    :return: Updated list of contestants after removal
    """
    try:
        start_pos = int(start_pos)
        end_pos = int(end_pos)
    except ValueError:
        raise ValueError("Start or end position is not a valid number.")

    # Check if start_pos and end_pos are within the valid range
    if start_pos < 0 or end_pos < 0 or start_pos >= len(v) or end_pos >= len(v):
        raise IndexError("Position out of range!")

    if start_pos > end_pos:
        return v  # No operation if start_pos > end_pos

    # Remove the contestants in the specified range
    del v[start_pos:end_pos + 1]
    return v  # Return the updated list after removal


def replace_contestant_score(contestantList, pos, position, new_score):
    """
    Replaces a specific score (P1, P2, P3) for a specific contestant at a given position in the list.

    :param contestantList: List of contestants (list of lists)
    :param pos: The position of the contestant in the list (0-indexed)
    :param position: The specific score to be replaced ('P1', 'P2', 'P3')
    :param new_score: The new score to replace with
    :return: Updated list of contestants
    :raises ValueError: If scores are invalid or the position is invalid
    :raises IndexError: If the contestant position is out of range
    """
    try:
        pos = int(pos)
        new_score = int(new_score)
    except ValueError:
        raise ValueError("Position and score must be integers.")

    if new_score < 0 or new_score > 10:
        raise error("Scores must be between 0 and 10.")

    if pos < 0 or pos >= len(contestantList):
        raise error("Contestant position is out of range.")

    # Determine the index based on the position
    if position == "P1":
        index = 0
    elif position == "P2":
        index = 1
    elif position == "P3":
        index = 2
    else:
        raise error("Position must be P1, P2, or P3.")

    contestantList[pos][index] = new_score
    return contestantList


def sort_contestants_descending(contestantList):
    """
    Sorts the contestants in descending order based on their total score, without modifying the original list.

    :param contestantList: List of contestants (list of lists with scores [P1, P2, P3])
    :return: A new list of contestants sorted in descending order of their total score
    """
    # Create a copy of the original list to avoid modifying it
    sorted_list = contestantList[:]

    # Sort the list using a basic comparison approach
    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            # Calculate total scores manually
            score_i = getp1(sorted_list[i]) + getp2(sorted_list[i]) + getp3(sorted_list[i])
            score_j = getp1(sorted_list[j]) + getp2(sorted_list[j]) + getp3(sorted_list[j])

            # Swap if needed to ensure descending order
            if score_i < score_j:
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]

    return sorted_list





def filter_contestants_by_average_score(contestantList, operator, score):
    """
    Filters the contestants based on their average score compared to a specified score.

    :param contestantList: List of contestants, where each contestant is a list of three scores [P1, P2, P3].
    :param operator: A string representing the comparison operator ('<', '=', '>').
    :param score: The score to compare the average with.
    :return: A filtered list of contestants that meet the comparison condition.
    """
    filtered_contestants = []

    try:
        # Ensure that score is a valid number
        score = float(score)

        if operator not in ['<', '=', '>']:
            raise ValueError(f"Invalid operator: '{operator}'. Must be '<', '=', or '>'.")


        for contestant in contestantList:
            # Calculate the average score
            average_score = sum(contestant) / 3

            # Perform the comparison based on the operator
            if operator == "<" and average_score < score:
                filtered_contestants.append(contestant)
            elif operator == "=" and average_score == score:
                filtered_contestants.append(contestant)
            elif operator == ">" and average_score > score:
                filtered_contestants.append(contestant)

    except ValueError as e:

        raise ValueError(f"Error: {e}")
    except Exception as e:

        raise Exception(f"An unexpected error occurred: {e}")

    return filtered_contestants


def average(item):
    return (item[0] + item[1] + item[2])/3

def compare(x,y):
    return average(y) - average(x)


import functools


def top_number(v, x):
    """
    Selects the top `x` elements from the list `v` based on a custom comparison.

    :param v: List of elements to be sorted and filtered.
    :param x: Number of top elements to return.
    :return: A list of the top `x` elements sorted by a custom comparison function.
    """
    list = []
    aux = v[:] #copy of v
    aux.sort(key=functools.cmp_to_key(compare))  # 'compare' needs to be a defined function.
    for i in range(x):
        list.append(aux[i])
    return list


def top_by_a_problem(v, x, y):
    """
    Selects the top `x` elements from the list of tuples `v`, sorted by the column determined by `y`.

    :param v: List of tuples to be sorted and filtered (e.g., [(a1, b1, c1), (a2, b2, c2), ...]).
    :param x: Number of top elements to return.
    :param y: Column key indicating which tuple element to sort by ('P1' for 0th, 'P2' for 1st, 'P3' for 2nd).
    :return: A list of the top `x` tuples sorted by the specified column.
    """
    ok = False
    if y == "P1":
        compare = 0
        ok = True
    elif y == "P2":
        compare = 1
        ok = True
    elif y == "P3":
        compare = 2
        ok = True
    if not ok:
        raise ValueError("Parameter 'y' must be either 'P1', 'P2', or 'P3'.")

    list = []
    aux = v[:]
    aux.sort(key=lambda tup: tup[compare], reverse=True)
    for i in range(x):
        list.append(aux[i])
    return list


def remove(v, x, y):
    """
    Modifies the contestant list by replacing all scores with [0, 0, 0] for contestants whose average score
    meets a specified condition.

    :param v: List of contestants, where each contestant is a list of three numerical scores [P1, P2, P3].
    :param x: Comparison operator as a string ('<', '>', or '='). Determines the condition to apply on the average score.
    :param y: Threshold value (float or int) for comparing the average score of each contestant.
    :return: A new list of contestants where scores are replaced with [0, 0, 0] if the condition specified by x and y is met.
    :raises ValueError: If the operator `x` is not one of '<', '>', or '='.
    :raises TypeError: If the input list `v` or threshold `y` is not in the expected format.

    """

    list = []
    if x == '<':
        for i in range(len(v)):
            q = (v[i][0] + v[i][1] + v[i][2]) / 3
            if q < y:
                temp = []
                temp.append(0)
                temp.append(0)
                temp.append(0)
            else:
                temp = []
                temp.append(v[i][0])
                temp.append(v[i][1])
                temp.append(v[i][2])
            list.append(temp)
    elif x == '>':
        # do smt
        for i in range(len(v)):
            q = (v[i][0] + v[i][1] + v[i][2]) / 3
            if q > y:
                temp = []
                temp.append(0)
                temp.append(0)
                temp.append(0)
            else:
                temp = []
                temp.append(v[i][0])
                temp.append(v[i][1])
                temp.append(v[i][2])
            list.append(temp)
    elif x == '=':
        # do smt
        for i in range(len(v)):
            q = (v[i][0] + v[i][1] + v[i][2]) / 3
            if q == y:
                temp = []
                temp.append(0)
                temp.append(0)
                temp.append(0)
            else:
                temp = []
                temp.append(v[i][0])
                temp.append(v[i][1])
                temp.append(v[i][2])
            list.append(temp)
    else:
        raise error("Invalid operator: '<', '=', or '>'")

    return list


def undo_calculator(contestantList, history) -> None:
    """
    Undo the last change to the contestantList by restoring the previous state from history.

    :param contestantList: The current list of contestants
    :param history: List containing previous states of contestantList
    :return: None, modifies contestantList in place
    """
    if len(history) == 1:  # Only one state (initial state), no undo possible
        return

    # Remove the last operation (current one) and revert to the previous one
    history.pop()
    previous_state = history[-1]
    contestantList[:] = previous_state









def test_insert_new_contestant():
    # Test valid input
    contestants = [[8, 9, 7], [6, 5, 8]]
    result = insert_new_contestant(contestants, 7, 6, 9, 1)
    assert result == [[8, 9, 7], [7, 6, 9], [6, 5, 8]], f"Expected [[8, 9, 7], [7, 6, 9], [6, 5, 8]] but got {result}"

    # Test invalid score (too high)
    contestants = [[8, 9, 7]]
    result = insert_new_contestant(contestants, 11, 6, 9, 0)
    assert result == [[8, 9, 7]], f"Expected [[8, 9, 7]] but got {result}"

    # Test invalid position (out of range)
    contestants = [[8, 9, 7]]
    result = insert_new_contestant(contestants, 7, 6, 9, 10)
    assert result == [[8, 9, 7]], f"Expected [[8, 9, 7]] but got {result}"

    print("All tests passed!")

test_insert_new_contestant()
print("bla")

def test_remove_contestant():
    # Test valid removal from middle of list
    contestants = [1, 2, 3, 4, 5]
    result = remove_contestant(contestants, 2)
    assert result == [1, 2, 4, 5], f"Expected [1, 2, 4, 5] but got {result}"

    # Test valid removal from beginning of list
    contestants = [1, 2, 3, 4, 5]
    result = remove_contestant(contestants, 0)
    assert result == [2, 3, 4, 5], f"Expected [2, 3, 4, 5] but got {result}"

    print("All tests passed!")

def test_remove_contestant_range():
    # Test case 1: Remove contestants from the middle
    contestants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = remove_contestant_range(contestants, 3, 6)
    assert result == [1, 2, 3, 8, 9, 10], f"Expected [1, 2, 3, 8, 9, 10] but got {result}"

    # Test case 2: Remove contestants from the start
    contestants = [1, 2, 3, 4, 5]
    result = remove_contestant_range(contestants, 0, 2)
    assert result == [4, 5], f"Expected [4, 5] but got {result}"

    # Test case 3: Remove contestants from the end
    contestants = [1, 2, 3, 4, 5]
    result = remove_contestant_range(contestants, 3, 4)
    assert result == [1, 2, 3], f"Expected [1, 2, 3] but got {result}"
    

# Run the tests
test_remove_contestant_range()
