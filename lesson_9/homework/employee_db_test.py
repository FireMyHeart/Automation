from CompanyApi import CompanyApi
from EmployeeApi import EmployeeApi
from EmployeeTable import EmployeeTable


api1 = CompanyApi("https://x-clients-be.onrender.com")
api2 = EmployeeApi("https://x-clients-be.onrender.com")
bd = EmployeeTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

# 1 получить всех сотрудников конкретной компании
def test_get_employee():
    bd.create_company('Company to delete', 'Random descr')
    new_id = bd.get_max_comp_id()

    api_result = api2.get_employee(new_id)
    bd_result = bd.get_employees(new_id)

    bd.delete_company(new_id)

    assert len(api_result) == len(bd_result)

# 2 получить сотрудника по id
def test_id_employee():
    bd.create_company('Company to delete', 'Random descr')
    new_id = bd.get_max_comp_id()
    name = 'Emily'
    surname = 'Kotikova'
    bd.create(name, surname, 'no_phone', new_id)
    bd_max_id = bd.get_max_id(new_id)
    api_result = api2.get_employee_by_id(bd_max_id)
    
    bd.delete(bd_max_id)
    bd.delete_company(new_id)

    assert bd_max_id == api_result['id']
    assert name == api_result['firstName']
    assert surname == api_result['lastName']
    assert new_id == api_result['companyId']

# 3 создать сотрудника
def test_create_employee():
    bd.create_company('Company to delete', 'Random descr')
    new_id = bd.get_max_comp_id()
    api_result_before = api2.get_employee(new_id)
    employee = api2.create_employee(new_id)
    empid = employee.json()['id']
    api_result_after = api2.get_employee(new_id)
    bd_result_after = bd.get_employee(empid)

    bd.delete(empid)
    bd.delete_company(new_id)

    assert len(api_result_after) - len(api_result_before) == 1
    assert len(bd_result_after) == 1
    assert employee.status_code == 201

# 4 изменить запись о сотруднике
def test_update_employee():
    bd.create_company('Company to delete', 'Random descr')
    new_id = bd.get_max_comp_id()
    name = 'Emily'
    surname = 'Kotikova'
    bd.create(name, surname, 'no_phone', new_id)
    bd_max_id = bd.get_max_id(new_id)
    new_name = 'Ophelia'
    bd.update_employee(bd_max_id, new_name)
    employee_edited = bd.get_employee(bd_max_id)

    bd.delete(bd_max_id)
    bd.delete_company(new_id)

    assert employee_edited[0][4] == new_name
