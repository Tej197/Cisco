from salary_manager import create_salary, read_all, read_by_salary, update_salary, delete_salary, salaries

def menu():
    message = "Enter your choice (1-6): " \
    "\n1. Create Salary" \
    "\n2. Read All Salaries" \
    "\n3. Read Salary by Value" \
    "\n4. Update Salary" \
    "\n5. Delete Salary" \
    "\n6. Exit\n"
    
    choice = int(input(message))
    if choice == 1:
        salary = int(input("Enter salary to create: "))
        create_salary(salary)
    elif choice == 2:
        all_salaries = read_all()
        print("All Salaries:")
        for sal in all_salaries:
            print(sal)
    elif choice == 3:
        salary = int(input("Enter salary to search: "))
        index = read_by_salary(salary)
        if index != -1:
            print(f"Salary {salary} found at index {index}.")
        else:
            print(f"Salary {salary} found at {index}.")
    elif choice == 4:
        old_salary = int(input("Enter old salary to update: "))
        new_salary = int(input("Enter new salary: "))
        update_salary(old_salary, new_salary)
    elif choice == 5:
        salary = int(input("Enter salary to delete: "))
        delete_salary(salary)
    return choice

def menus():
    print("Salary Management System")
    choice = menu()
    while choice != 6:
        choice = menu()
        print("Thank you for using the Salary Management System.")
    
menus()