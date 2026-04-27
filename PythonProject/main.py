

def get_student_info():
    """Collect student information including name, surname, grade, and intent"""

    print("=" * 50)
    print("STUDENT INFORMATION SYSTEM")
    print("=" * 50)


    name = input("Enter your name: ").strip()
    surname = input("Enter your surname: ").strip()


    while True:
        try:
            grade = float(input("Enter your grade (0-100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")


    print("\nSelect your intent:")
    print("1. Continue studying")
    print("2. Find a job")
    print("3. Transfer to another school")
    print("4. Graduate")
    print("5. Other")

    intent_options = {
        "1": "Continue studying",
        "2": "Find a job",
        "3": "Transfer to another school",
        "4": "Graduate",
        "5": "Other"
    }

    while True:
        choice = input("Enter your choice (1-5): ").strip()
        if choice in intent_options:
            intent = intent_options[choice]
            if choice == "5":
                custom_intent = input("Please specify your intent: ").strip()
                intent = custom_intent
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


    student_info = {
        "name": name,
        "surname": surname,
        "grade": grade,
        "intent": intent
    }

    return student_info


def display_student_info(student):
    """Display the collected student information"""

    print("\n" + "=" * 50)
    print("STUDENT INFORMATION SUMMARY")
    print("=" * 50)
    print(f"Name:     {student['name']} {student['surname']}")
    print(f"Grade:    {student['grade']:.2f}")


    if student['grade'] >= 90:
        letter_grade = "A"
    elif student['grade'] >= 80:
        letter_grade = "B"
    elif student['grade'] >= 70:
        letter_grade = "C"
    elif student['grade'] >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print(f"Letter Grade: {letter_grade}")
    print(f"Intent:   {student['intent']}")
    print("=" * 50)



if __name__ == "__main__":

    student_data = get_student_info()


    display_student_info(student_data)


    save_choice = input("\nWould you like to save this information to a file? (yes/no): ").strip().lower()
    if save_choice in ['yes', 'y']:
        filename = f"{student_data['name']}_{student_data['surname']}_info.txt"
        with open(filename, 'w') as file:
            file.write(f"Student Information\n")
            file.write(f"Name: {student_data['name']} {student_data['surname']}\n")
            file.write(f"Grade: {student_data['grade']}\n")
            file.write(f"Intent: {student_data['intent']}\n")
        print(f"Information saved to '{filename}'")
