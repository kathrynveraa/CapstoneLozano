#problem 2
#capstone

class Student:
    def __init__(self, student_id, name, course, grade1, grade2, grade3, grade4):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.grades = [grade1, grade2, grade3, grade4]
    
    def update_grade(self, grade_index, new_grade):
    
        if 0 <= grade_index < len(self.grades):
            self.grades[grade_index] = new_grade
        else:
            print("Invalid grade index.")
    
    def calculate_average(self):
        return sum(self.grades) / len(self.grades)
    
    def display(self):
    
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.calculate_average():.2f}\n")


class StudentGradeManagement:
    def __init__(self):
        self.students = []
    
    def add_student(self, student_id, name, course, grade1, grade2, grade3, grade4):
        new_student = Student(student_id, name, course, grade1, grade2, grade3, grade4)
        self.students.append(new_student)
        print(f"Student {name} added successfully.\n")
    
    def update_student_grade(self, student_id, grade_index, new_grade):
        for student in self.students:
            if student.student_id == student_id:
                student.update_grade(grade_index, new_grade)
                print(f"Grade updated for student {student_id}.\n")
                return
        print("Student not found.\n")
    
    def display_all_students(self):
        if not self.students:
            print("No students available.\n")
            return
        for student in self.students:
            student.display()
    
    def calculate_class_average(self):
        if not self.students:
            print("No students available.\n")
            return
        total_sum = sum(student.calculate_average() for student in self.students)
        class_average = total_sum / len(self.students)
        print(f"Class Average Grade: {class_average:.2f}\n")


def main():
    system = StudentGradeManagement()
    
    while True:
        print("Student Grade Management System (for teachers)")
        print("1. Add Student id ")
        print("2. Update Student Grade")
        print("3. Display All Students")
        print("4. Total Class Grade Average")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            course = input("Enter course: ")
            grade1 = float(input("Enter grade 1: "))
            grade2 = float(input("Enter grade 2: "))
            grade3 = float(input("Enter grade 3: "))
            grade4 = float(input("Enter grade 4: "))
            system.add_student(student_id, name, course, grade1, grade2, grade3, grade4)
        
        elif choice == '2':
            student_id = input("Enter student ID to update: ")
            grade_index = int(input("Enter grade index to update (0-3): "))
            new_grade = float(input("Enter new grade: "))
            system.update_student_grade(student_id, grade_index, new_grade)
        
        elif choice == '3':
            system.display_all_students()
        
        elif choice == '4':
            system.calculate_class_average()
        
        elif choice == '5':
            print("Exiting the system.")
            print("Have a nice dayw")
            break
        
        else:
            print("Invalid option. Please try again by choosing 1-5.")

if __name__ == "__main__":
    main()
