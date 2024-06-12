from EmployeeApi import EmployeeApi
from CompanyApi import CompanyApi

api1 = EmployeeApi('https://x-clients-be.onrender.com')
api2 = CompanyApi('https://x-clients-be.onrender.com')

# 1 получить всех сотрудников конкретной компании
def test_get_employee():
    rand_comp = api2.create_random_company()[0]
    new_id = rand_comp['id']
    body = api1.get_employee(new_id)
    assert len(body) == 0

# 2 получить сотрудника по id
def test_id_employee():
    rand_comp = api2.create_random_company()[0]
    new_id = rand_comp['id']
    employee = api1.create_employee(new_id)
    empid = employee.json()['id']
    body = api1.get_employee_by_id(empid)
    assert body['id'] == empid

# 3 создать сотрудника
def test_create_employee():
    rand_comp = api2.create_random_company()[0]
    new_id = rand_comp['id']
    body1 = api1.get_employee(new_id)
    employee = api1.create_employee(new_id)
    empid = employee.json()['id']
    body2 = api1.get_employee(new_id)
    assert len(body1) + 1 == len(body2)
    assert empid > 0
    assert employee.status_code == 201

# 4 изменить запись о сотруднике
def test_update_employee():
    rand_comp = api2.create_random_company()[0]
    new_id = rand_comp['id']

    employee = api1.create_employee(new_id)
    empid = employee.json()['id']

    body = api1.get_employee_by_id(empid)

    employee_edited = api1.edit_employee(empid)  # изменяем email, url, isActive
    assert employee_edited['email'] != body['email']
    assert employee_edited['url'] != body['avatar_url']
    assert employee_edited['isActive'] != body['isActive']

# 5 проверить, что имя, фамилия и email обязательны
def test_required_fields():
    rand_comp = api2.create_random_company()[0]
    new_id = rand_comp['id']
    employee = api1.create_employee(new_id, fname = '', lname = '', email = '', mname = '', url = '', phone = '', birthdate = '')
    assert employee.status_code == 400
    assert employee.json()['message'] == ["firstName should not be empty", "lastName should not be empty", "email must be an email"]

# 6 проверить, что email должен быть именно email
def test_email():
    rand_comp = api2.create_random_company()[0]
    new_id = rand_comp['id']
    employee = api1.create_employee(new_id, email='anna')
    assert employee.status_code == 400
    assert employee.json()['message'] == ["email must be an email"]
