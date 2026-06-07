import time
import statistics

starline = "****************************************************"
tildeline = "~~~"
grade_list = [0]*7

def print_main_menu():
    print(tildeline+"Main menu"+tildeline)
    time.sleep(0.25)
    print("0. EXIT")
    print("1. Display highest mark")
    print("2. Display lowest mark")
    print("3. Display average (mean) mark")
    print("4. Display mode mark")
    print("5. Sort marks")
    print("6. Display marks")
    return int(input())

def add_grades():
   for i in range(len(grade_list)):
    while True:
        print("Input grade number " + str(i + 1) + ": ")
        grade = int(input())
        if grade >= 1 and grade <= 100:
            grade_list[i] = grade
            break
        else:
            print("The number must be between 1 and 100") 

def highest_mark():
    print("The student's highest grade is " + str(max(grade_list)))
    print(starline)
    time.sleep(0.5)

def lowest_mark():
    print("The student's lowest grade is " + str(min(grade_list)))
    print(starline)
    time.sleep(0.5)

def average_mark():
    print("The student's grade average is " + str(round(sum(grade_list)/len(grade_list), 2)))
    print(starline)
    time.sleep(0.5)

def mode_mark():
    print("The student's mode grade is " + str(statistics.mode(grade_list)))
    print(starline)
    time.sleep(0.5)

def sort_marks():
    grade_list.sort()
    print("Sorted list: " + str(grade_list))
    time.sleep(0.5)


add_grades()
print("Marks entered: " + str(grade_list))
while True:
    choice = print_main_menu()
    if choice == 0:
        break
    if choice == 1:
        highest_mark()
    elif choice == 2:
        lowest_mark()
    elif choice == 3:
        average_mark()
    elif choice == 4:
        mode_mark()
    elif choice == 5:
        sort_marks()
    elif choice == 6:
        print("Marks: " + str(grade_list))
        print(starline)
        time.sleep(0.5)
    else:
        print("Not a valid option")
        time.sleep(0.5)