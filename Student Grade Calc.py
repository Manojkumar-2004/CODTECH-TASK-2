class StudentGrades:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def edit_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject] = grade
        else:
            print("Subject not found")

    def delete_grade(self, subject):
        if subject in self.grades:
            del self.grades[subject]
        else:
            print("Subject not found")

    def calculate_average(self):
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        return 0

    def get_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def display_grades(self):
        if not self.grades:
            print("No grades available")
            return
        
        for subject, grade in self.grades.items():
            print(f"{subject}: {grade}")
        average = self.calculate_average()
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {self.get_letter_grade(average)}")

def main():
    tracker = StudentGrades()

    while True:
        print("\nStudent Grades Tracker")
        print("1. Add Grade")
        print("2. Edit Grade")
        print("3. Delete Grade")
        print("4. Display Grades")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            tracker.add_grade(subject, grade)
        elif choice == '2':
            subject = input("Enter subject: ")
            grade = float(input("Enter new grade: "))
            tracker.edit_grade(subject, grade)
        elif choice == '3':
            subject = input("Enter subject: ")
            tracker.delete_grade(subject)
        elif choice == '4':
            tracker.display_grades()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
