from sqlalchemy import create_engine
from sqlalchemy.sql import text
import allure


class EmployeeTable:
    __scripts = {
        "insert new company": text("insert into company(\"name\", description) values (:new_name, :description)"),
        "get max company id": text("select MAX(\"id\") from company where deleted_at is null"),
        "select": text("select * from employee where company_id =:comp_id"),
        "insert new": text("INSERT INTO employee (first_name, last_name, phone, company_id) VALUES (:f_name, :l_name, :ph, :comp_id)"),
        "get max id": text("select MAX(\"id\") from employee where company_id = :comp_id"),
        "select employee by id": text("select * from employee where \"id\" =:emp_id"),
        "update employee": text("UPDATE employee SET first_name = :f_name WHERE id = :emp_id"),
        "delete employee by id": text("delete from employee where id =:id_to_delete"),
        "delete company by id": text("delete from company where id =:id_to_delete"),
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    @allure.step("Создать команию в БД, указав имя {name} и описание {descr}")
    def create_company(self, name: str, descr=None) -> None:
        self.__db.execute(self.__scripts["insert new company"], new_name=name, description=descr)

    @allure.step("Получить из БД id последней созданной компании")
    def get_max_comp_id(self):
        return self.__db.execute(self.__scripts["get max company id"]).fetchall()[0][0]

    @allure.step("Получить из БД всех сотрудников компании с id {id}")
    def get_employees(self, id: int):
        return self.__db.execute(self.__scripts["select"], comp_id=id).fetchall()

    @allure.step("Создать в БД сотрудника в компании с id {id}, указав имя {first_name}, фамилию {surname}, телефон {phone}")
    def create(self, first_name: str, surname: str, phone: str, id: int):
        self.__db.execute(self.__scripts["insert new"], f_name=first_name, l_name=surname, ph=phone, comp_id=id)

    @allure.step("Получить из БД id {id} последнего созданного сотрудника")
    def get_max_id(self, id: int):
        return self.__db.execute(self.__scripts["get max id"], comp_id=id).fetchall()[0][0]

    @allure.step("Получить из БД информацию о сотруднике по id {id}")
    def get_employee(self, id: int):
        return self.__db.execute(self.__scripts["select employee by id"], emp_id=id).fetchall()

    @allure.step("Изменить в БД запись о сотруднике с id {id}, указав новое имя {name}")
    def update_employee(self, id: int, name: str):
        return self.__db.execute(self.__scripts["update employee"], emp_id=id, f_name=name)

    @allure.step("Удалить в БД запись о сотруднике с id {id}")
    def delete(self, id: int) -> None:
        self.__db.execute(self.__scripts["delete employee by id"], id_to_delete=id)

    @allure.step("Удалить в БД компанию с id {id}")
    def delete_company(self, id: int) -> None:
        self.__db.execute(self.__scripts["delete company by id"], id_to_delete=id)
