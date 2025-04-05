#jump search,selection sort and strand sort

import random
import math
def list_numbers(list,n):
    for i in range(n):
        list.append(random.randint(0,1000))
    print("Your list:",list)
def menu():
    print("This is your menu")
    print("1.Generate a random list of n numbers")
    print("2.Search using the Jump search algorithm ")
    print("3.Sort using the Selection sort algorithm")
    print("4.Sort using the Strand sort algorithm")
    print("5.Exit the program")

def search(list,x):
    step=int(math.sqrt(len(list)))
    prev=0
    ok=False
    if list[len(list)-1]<x:
        ok=False
    elif list[0]>x:
        ok=False
    else:
        while list[min(step, len(list)) - 1] < x:
            prev=step
            step=step+int(math.sqrt(len(list)))
            if step>=len(list):
                ok=False

        for i in range (prev,min(step,len(list))):
            if list[i]==x:
                ok=True

    if ok==False:
        return False
    else:
        return i

def selection_sort(list,ns): #ns=number of steps shown
    count=0
    for step in range(len(list)):
        mini= step
        for i in range(step + 1, len(list)):
            if list[i] < list[mini]:
                mini = i
        if mini != step:
            (list[step], list[mini]) = (list[mini], list[step]) #How to Swap the elements -> list[pos1],list[pos2] =list[pos2],list[pos1]
            count=count+1
            if(count%ns==0):
                print("Your list at step: ",count," is ",list)
    return list




def merge(sorted_list, strand):
    result = []
    i = j = 0

    while i < len(sorted_list) and j < len(strand):
        if sorted_list[i] <= strand[j]:
            result.append(sorted_list[i])
            i=i+1
        else:
            result.append(strand[j])
            j=j+1

    result.extend(sorted_list[i:])
    result.extend(strand[j:])
    return result

def strand_sort(list,ns):
    sorted_list = []
    count = 0
    while list:
        strand = [list.pop(0)]
        i = 0
        while i < len(list):
            if list[i] > strand[-1]:
                strand.append(list.pop(i))
            else:
                i=i+1
        sorted_list = merge(sorted_list, strand)
        count = count + 1
        if (count % ns == 0):
            print("Your list at step: ", count, " is ", sorted_list)

    return sorted_list


def start():
    sorted=False
    list_created=False
    while True:
        menu()
        command = input("Your choice: ")
        if command == "1":
            list=[]
            n=int(input("Enter how many random numbers the list will have: "))
            list_numbers(list,n)
            list_created=True
            sorted=False
        elif command == "2":
            if list_created==False:
                print("Sorry,you can't search without a list.")
            elif list_created==True and sorted==False:
                print("Sorry,you have to sort the list first,please choose 3 or 4")
            else:
                x=int(input("Enter the number you are looking for: "))

                if search(list,x)==False:
                    print("Sorry,the number",x,"is not in the list")
                else :
                    print("You have found the number",x,"in the list at",search(list,x))
        elif command == "3":
            if list_created==False:
                print("Sorry,you can't sort without a list.You have to choose the first option before this one")
            elif sorted == True:
                print("Sorry,the list has already been sorted.Please generate a new one by choosing the first option")
            else:
                ns=int(input("Choose an n.Every n steps will be shown: "))
                print("final list",selection_sort(list,ns))
                sorted=True
        elif command == "4":
            if list_created==False:
                print("Sorry,you can't sort without a list.You have to choose the first option before this one")
            elif sorted==True:
                print("Sorry,the list has already been sorted.Please generate a new one by choosing the first option")
            else:
                ns = int(input("Choose an n.Every n steps will be shown: "))
                list = strand_sort(list,ns)
                sorted=True
            print("final list",list)
        elif command == "5":
            print("You chose to exit the menu.Goodbye!")
            break
        else:
            print("Please choose a valid option")
start()