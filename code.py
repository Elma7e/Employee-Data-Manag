import csv

# Employee blueprint. Each employee's attributes.
class Employee:
    def __init__(self, emp_id, name, position, salary, email):
        self.__emp_id = emp_id
        self.__name = name
        self.__position = position
        self.__salary = salary
        self.__email = email

    def update_details(self, name=None, position=None, salary=None, email=None):
        # Update only the fields provided, leave others as they are.
        if name:
            self.__name = name
        if position:
            self.__position = position
        if salary:
            self.__salary = salary
        if email:
            self.__email = email

    def display(self):
        # Just to make printing the employee details easy.
        return f"ID: {self.__emp_id}, Name: {self.__name}, Position: {self.__position}, Salary: {self.__salary}, Email: {self.__email}"

    def get_id(self):
        return self.__emp_id

# This class manages everything - adding, updating, deleting, etc.
class EmployeeManager:
    def __init__(self, filename):
        self.__filename = filename
        self.__employees = []
        self.load_data()

    def load_data(self):
        # Trying to load employee data from the CSV file.
        try:
            with open(self.__filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Creating Employee objects and adding them to the list.
                    emp = Employee(row['ID'], row['Name'], row['Position'], row['Salary'], row['Email'])
                    self.__employees.append(emp)
        except FileNotFoundError:
            # If the file doesn't exist, it's fine. We'll create it later.
            pass

    def save_data(self):
        # Saving all employees back into the CSV file.
        with open(self.__filename, mode='w', newline='') as file:
            fieldnames = ['ID', 'Name', 'Position', 'Salary', 'Email']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for emp in self.__employees:
                writer.writerow({
                    'ID': emp.get_id(),
                    'Name': emp._Employee__name,
                    'Position': emp._Employee__position,
                    'Salary': emp._Employee__salary,
                    'Email': emp._Employee__email
                })

    def add_employee(self, emp_id, name, position, salary, email):
        # Adding a new employee to the list.
        emp = Employee(emp_id, name, position, salary, email)
        self.__employees.append(emp)
        self.save_data()

    def update_employee(self, emp_id, name=None, position=None, salary=None, email=None):
        # Finding the employee and updating their details.
        for emp in self.__employees:
            if emp.get_id() == emp_id:
                emp.update_details(name, position, salary, email)
                self.save_data()
                return True
        return False  # Employee not found.

    def delete_employee(self, emp_id):
        # Removing an employee from the list.
        for emp in self.__employees:
            if emp.get_id() == emp_id:
                self.__employees.remove(emp)
                self.save_data()
                return True
        return False  # Employee not found.

    def search_employee(self, emp_id):
        # Looking for an employee by their ID.
        for emp in self.__employees:
            if emp.get_id() == emp_id:
                return emp
        return None

    def list_employees(self):
        # Returning the list of all employees.
        return self.__employees

# This function acts as the main menu without using the __name__ check.
def start_program():
    manager = EmployeeManager('employees.csv')

    while True:
        print("\nEmployee Data Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Search Employee")
        print("5. List All Employees")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Adding a new employee.
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            email = input("Enter Email: ")
            manager.add_employee(emp_id, name, position, salary, email)
            print("Employee added successfully!")

        elif choice == '2':
            # Updating employee details.
            emp_id = input("Enter Employee ID to update: ")
            name = input("Enter New Name (leave blank to skip): ")
            position = input("Enter New Position (leave blank to skip): ")
            salary = input("Enter New Salary (leave blank to skip): ")
            email = input("Enter New Email (leave blank to skip): ")
            if manager.update_employee(emp_id, name, position, salary, email):
                print("Employee updated successfully!")
            else:
                print("Employee not found!")

        elif choice == '3':
            # Deleting an employee.
            emp_id = input("Enter Employee ID to delete: ")
            if manager.delete_employee(emp_id):
                print("Employee deleted successfully!")
            else:
                print("Employee not found!")

        elif choice == '4':
            # Searching for an employee.
            emp_id = input("Enter Employee ID to search: ")
            emp = manager.search_employee(emp_id)
            if emp:
                print("Employee found:")
                print(emp.display())
            else:
                print("Employee not found!")

        elif choice == '5':
            # Listing all employees.
            employees = manager.list_employees()
            if employees:
                print("\nList of Employees:")
                for emp in employees:
                    print(emp.display())
            else:
                print("No employees found!")

        elif choice == '6':
            # Exiting the program.
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

# Start the program
start_program()
