from CompanyApi import CompanyApi
from EmployeeApi import EmployeeApi
from EmployeeTable import EmployeeTable
import allure


api1 = CompanyApi("https://x-clients-be.onrender.com")
api2 = EmployeeApi("https://x-clients-be.onrender.com")
bd = EmployeeTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")


@allure.id("LSN10-7")
@allure.epic("Создание API тестов и БД тестов")
@allure.story("Библиотеки requests и SQLAlchemy")
@allure.feature("GET")
@allure.title("Получить всех сотрудников")
@allure.description("Получить всех сотрудников конкретной компании из БД и через API и сравнить результат")
@allure.severity("blocker")
@allure.suite("requests и SQLAlchemy")
def test_get_employee():
    bd.create_company('Company to delete', 'Random descr')
    new_id = bd.get_max_comp_id()

    api_result = api2.get_employee(new_id)
    bd_result = bd.get_employees(new_id)

    bd.delete_company(new_id)

    assert len(api_result) == len(bd_result)


@allure.id("LSN10-8")
@allure.epic("Создание API тестов и БД тестов")
@allure.story("Библиотеки requests и SQLAlchemy")
@allure.feature("GET")
@allure.title("Получить сотрудника по id")
@allure.description("Получить конкретного сотрудника из БД и через API, проверить, что id совпадают")
@allure.severity("critical")
@allure.suite("requests и SQLAlchemy")
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


@allure.id("LSN10-9")
@allure.epic("Создание API тестов и БД тестов")
@allure.story("Библиотеки requests и SQLAlchemy")
@allure.feature("POST")
@allure.title("Создать сотрудника в компании")
@allure.description("Создать сотрудника через API и проверить, что в БД появилась запись о созданном сотруднике")
@allure.severity("critical")
@allure.suite("requests и SQLAlchemy")
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


@allure.id("LSN10-10")
@allure.epic("Создание API тестов и БД тестов")
@allure.story("Библиотеки requests и SQLAlchemy")
@allure.feature("PATCH")
@allure.title("Изменить запись о сотруднике в БД")
@allure.description("Изменить запись о сотруднике в БД и проверить, что данные обновились")
@allure.severity("major")
@allure.suite("requests и SQLAlchemy")
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
