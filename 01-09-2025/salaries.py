salaries = []
salaries.append(50000)
salaries.append(60000)
salaries.append(55000)
print(salaries)

search = 55000
index = -1
I = 0
for salary in salaries:
    if salary == search:
        index = I
        break
    I += 1
print(index)

search_salary = 60000
if search_salary in salaries:
    print(f"Salary {search_salary} found in the list.")