students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}

while True:
    print("---STUDENT MARKS MANAGER---")
    print("1. Add students")
    print("2. View all")
    print("3. Show topper")
    print("4. Exit")

    choice = input('Enter your choice: ')

    if choice == "1":
        name = input("Enter student name: ").strip()

        if name in students:
            print("Student already exits.")

        else:
            marks = []

            for i in range(1 ,4):
                while True:
                    
                     
                    mark = float(input(f"Enter mark {i} (0-100): "))

                    if 0 <= mark <= 100:
                        marks.append(mark) 
                        break
                    else:
                        print("Invalid mark, try again.")

            students[name] = marks
            print("Student added successfully.")

    elif choice == "2":
        print("---All Students---")

        for name, marks in students.items():
            average = round(sum(marks) / len(marks), 2)

            if average >= 85:
                grade = "A"

            elif average >= 70:
                grade = "B"

            elif average >= 50:
                grade = "C"

            else:
                grade = "F"


            print(name, average, grade)

    elif choice == "3":

        topper = None

        highest_average = -1

        for name, marks in students.items():
            average = sum(marks) / len(marks)

            if average > highest_average:
                highest_average = average

                topper = name

        if topper is not None:
            print("Topper: ", topper)
            print("Average: ", round(highest_average, 2))


    elif choice == "4":
        print("Goodbye!")

    else:
        print("Invalid choice. Try again.")