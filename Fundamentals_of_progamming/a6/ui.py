"""
A
add   #done
insert #done
B
remove #done
remove a to b #done
replace #done
C
display all participants and their score #done
display participants with an average score >5 #done
display participants sorted in decreasing order of total score #done
D
top ...
top... base on problem ...
set the scores of participants having an average score <70 to 0
E
undo #done
"""

#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
import random
import functions
from texttable import Texttable


def display_contestants(contestantList):
    """
    Displays all contestants and their scores in a table format using texttable.

    :param contestantList: List of contestants, where each contestant is represented as a list of scores [P1, P2, P3].
    """
    table = Texttable()
    # Set header
    table.header(['Contestant #', 'P1', 'P2', 'P3'])

    # Add rows for each contestant
    for idx, scores in enumerate(contestantList):
        table.add_row([idx + 1, scores[0], scores[1], scores[2]])

    # Print the table
    print(table.draw())


def generate_initial_contestants(p):
    for _ in range(10):
        p1 = random.randint(0, 10)
        p2 = random.randint(0, 10)
        p3 = random.randint(0, 10)
        p.append(functions.add_new_contestant(p1, p2, p3))

def menu():
    print("Here is you menu")
    print("Category A.Add the result of a new participant")
    print("Category B.Modify scores")
    print("Category C.Display participants whose score has different properties")
    print("Category D.Establish the podium")
    print("Category E.Undo")

def start():
    contestantList=[]
    history=[]
    generate_initial_contestants(contestantList)
    print(contestantList)
    history.append([x[:] for x in contestantList])
    while True:
        menu()
        command=input("Enter category: ")
        if command == "A":
            print("add <P1 score> <P2 score> <P3 score> ")
            print("insert <P1 score> <P2 score> <P3 score> at <position> ")
            text=input("Introduce your choice ")
            x=text.split(' ')
            if x[0]=="add":
                if len(x)==4:
                    try:
                        contestantList.append(functions.add_new_contestant(x[1], x[2], x[3]))
                        history.append([x[:] for x in contestantList])
                    except Exception as e:
                            print(e)
                else:
                    print("add contestant failed")
            elif x[0]=="insert":
                if len(x)==6 and x[4]=="at":
                    try:
                        contestantList= functions.insert_new_contestant(contestantList, x[1], x[2], x[3], x[5])
                    except Exception as e:
                        print(e)
                        history.append([x[:] for x in contestantList])
                else:
                    print("insert contestant failed")
            else:
                print("not recognized")
        elif command == "B":
            print("remove <position>")
            print("remove <start position> to <end position>")
            print("replace <contestant pos> <P1 | P2 | P3> with <new score>")
            text = input("Introduce your choice: ").strip()
            x = text.split(' ')
            if x[0] == "remove" and len(x) == 2:
                try:
                    contestantList = functions.remove_contestant(contestantList, x[1])
                    history.append([x[:] for x in contestantList])
                except Exception as e:
                    print(e)
            elif x[0] == "remove" and len(x) == 4 and x[2] == "to":
                try:

                    contestantList = functions.remove_contestant_range(contestantList, x[1], x[3])
                    history.append([x[:] for x in contestantList])
                except Exception as e:

                    print(e)
            elif  x[0] == "replace" and len(x) == 5 and x[3] == "with":
                try:
                    contestantList = functions.replace_contestant_score(contestantList, x[1], x[2], x[4])
                    history.append([x[:] for x in contestantList])  # Save state for undo
                except Exception as e:
                    print(e)
            else:
                print("Remove contestant failed. Check the input format.")
        elif command=="C":
            print("list")
            print("sorted list")
            print("list [ < | = | > ] <score>")
            text = input("Introduce your choice: ").strip()
            x = text.split(' ')
            if x[0] == "list" and len(x) == 1:
                display_contestants(contestantList)
            elif x[0] == "sorted" and len(x) == 2 and x[1] == "list":
                sorted_contestants = functions.sort_contestants_descending(contestantList)
                display_contestants(sorted_contestants)
            elif  x[0] == "list" and len(x) == 3:
                try:
                    operator = x[1]
                    score = float(x[2])
                    filtered_contestants = functions.filter_contestants_by_average_score(contestantList, operator, score)
                    display_contestants(filtered_contestants)
                except ValueError as e:
                    print(e)  # Display error message for invalid input
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
        elif command=="D":
            print("top <number>")
            print("top <number> to <number>")
            print("remove [ < | = | > ] <score>")
            text = input("Introduce your choice: ").strip()
            x = text.split(' ')
            if x[0] == "top" and len(x) == 2:
                try:
                    showList = functions.top_number(contestantList, int(x[1]))
                    print(showList)
                except Exception as e:
                    print(e)
            elif  x[0] == "top" and len(x) == 3:
                try:
                    showList = functions.top_by_a_problem(contestantList, int(x[1]), x[2])
                    print(showList)
                except Exception as e:
                    print(e)
            elif x[0] == "remove" and len(x) == 3:
                try:
                    contestantList = functions.remove(contestantList, x[1], int(x[2]))
                    history.append([x[:] for x in contestantList])
                    print(contestantList)
                except Exception as e:
                    print(e)
            else:
                print("Program failed. Check the input format.")
        elif command == "E":
            if len(history) == 1:  # Check if no more undos are available
                print("No more undos available.")
            else:
                functions.undo_calculator(contestantList, history)  # Call the undo function
                print("Undo successful! Reverted to previous state.")
        else:
            print("Invalid command")
        print(contestantList)





