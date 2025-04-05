# Solve the problem from the third set here
# Function to determine if a given year is a leap year
def leap_year(year):
    ok=0
    #A year is a leap year if it's divisible by 4 but not by 100, or if it's divisible by 400
    #for example 1800 is divisible by 4 and 100 ,but not by 400 so it's not a leap year
    if year%4==0 and year%100!=0 or year%400==0:
        ok=1
    return ok

# Function to calculate the number of days between two years (without the current and birth years)
def all_years(y1,y2):
    count=0
    for i in range(y2+1,y1):
        if leap_year(i)==1:
            count=count+366
        else:
            count=count+365
    return count

# Function to calculate the number of days from the start of the current year to the current date
def current_year(y1,m1,d1):
    count=0
    l=[31,28,31,30,31,30,31,31,30,31,30,31]
    count=count+d1
    for i in range(0,m1-1):
        count=count+l[i]
    if leap_year(y1)==1:
        count=count+1
    return count

#Function to calculate the number of days from the birth date to the end of the birth year
def birth_year(y2,m2,d2):
    count = 0
    l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = count + d2
    for i in range(0, m2 - 1):
        count = count + l[i]
    if leap_year(y2) == 1:
        count=count+1
    if leap_year(y2)==1:
        return 366-count
    else:
        return 365-count



d1=int(input("Please introduce current day "))
m1=int(input("Please introduce current month "))
y1=int(input("Please introduce current year "))
d2=int(input("Please introduce the day of your birth " ))
m2=int(input("Please introduce the month of your birth "))
y2=int(input("Please introduce year of your birth "))
print(all_years(y1,y2)+current_year(y1,m1,d1)+birth_year(y2,m2,d2)+1)
# added 1 so we take into account the present day