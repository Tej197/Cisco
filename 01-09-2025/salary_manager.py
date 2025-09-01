salaries =[]

#CRUD - Create, Read ALL, Read By ID, Update, Delete, Read by salary

def create_salary(salary):
    global salaries
    salaries.append(salary)

def read_all():
    return salaries

def read_by_salary(salary):
    for I in range(len(salaries)):
        if salaries[I] == salary:
            return I
    return -1

def update_salary(old_salary, new_salary):
    global salaries
    index = read_by_salary(old_salary)
    salaries[index] = new_salary

def delete_salary(salary):
    global salaries
    index = read_by_salary(salary)
    salaries.pop(index)


create_salary(50000)
create_salary(60000)        
create_salary(55000)


result = read_all()
for salary in result:
    print(salary)


print(read_by_salary(55000))
print(read_by_salary(70000))
print(salaries[read_by_salary(60000)])

update_salary(55000, 58000)
print(read_all())

delete_salary(60000)
print(read_all())