#problem 3
#capstone

class Employee:
    def __init__(self, employee_id, name, organization):
        self.employee_id = employee_id
        self.name = name
        self.organization = organization
        self.attendance = []  
    
    def mark_attendance(self, present):
        """Mark attendance for the employee: True for present, False for absent."""
        self.attendance.append(present)
    
    def calculate_attendance_percentage(self):
        """Calculate attendance percentage based on the attendance list."""
        total_days = len(self.attendance)
        present_days = self.attendance.count(True)
        if total_days > 0:
            return (present_days / total_days) * 100
        return 0.0
    
    def display(self):
        """Display the employee's attendance details."""
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Organization: {self.organization}")
        print(f"Attendance: {self.attendance}")
        print(f"Attendance Percentage: {self.calculate_attendance_percentage():.2f}%\n")


class AttendanceTracker:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee_id, name, organization):
        """Add a new employee to the system."""
        new_employee = Employee(employee_id, name, organization)
        self.employees.append(new_employee)
        print(f"Employee {name} added successfully.\n")
    
    def mark_attendance(self, employee_id, present):
        """Mark attendance for a specific employee."""
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.mark_attendance(present)
                print(f"Attendance marked for employee {employee_id}.\n")
                return
        print(f"Employee with ID {employee_id} not found.\n")
    
    def display_all_attendance(self):
        """Display attendance records for all employees."""
        if not self.employees:
            print("No employees available.\n")
            return
        for employee in self.employees:
            employee.display()
    
    def display_attendance_percentage(self):
        """Display the attendance percentage for all employees."""
        if not self.employees:
            print("No employees available.\n")
            return
        for employee in self.employees:
            print(f"Employee: {employee.name} | Attendance Percentage: {employee.calculate_attendance_percentage():.2f}%")
        print()


def main():
    tracker = AttendanceTracker()
    
    while True:
        print("Employee Attendance Tracker Program")
        print("1. Add Employee id")
        print("2. Mark Attendance")
        print("3. Display All Attendance Records")
        print("4. Display Attendance Percentage")
        print("5. Exit program")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            employee_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            organization = input("Enter organization name: ")
            tracker.add_employee(employee_id, name, organization)
        
        elif choice == '2':
            employee_id = input("Enter employee ID to mark attendance: ")
            attendance = input("Enter attendance (P for Present, A for Absent): ").strip().lower()
            if attendance == 'p':
                tracker.mark_attendance(employee_id, True)
            elif attendance == 'a':
                tracker.mark_attendance(employee_id, False)
            else:
                print("Invalid input. Please enter 'P' for Present or 'A' for Absent.\n")
        
        elif choice == '3':
            tracker.display_all_attendance()
        
        elif choice == '4':
            tracker.display_attendance_percentage()
        
        elif choice == '5':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid option. Please try again by choosing 1-5.")

if __name__ == "__main__":
    main()
