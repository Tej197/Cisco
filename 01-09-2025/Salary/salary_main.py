from salary_manager import create_salary, read_all, read_by_salary, update_salary, delete_salary, salaries

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