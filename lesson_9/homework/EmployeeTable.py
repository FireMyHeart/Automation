from sqlalchemy import create_engine
from sqlalchemy.sql import text


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
    
    def create_company(self, name, descr=None):
        self.__db.execute(self.__scripts["insert new company"], new_name = name, description = descr)
    
    def get_max_comp_id(self):
        return self.__db.execute(self.__scripts["get max company id"]).fetchall()[0][0]

    def get_employees(self, id):
        return self.__db.execute(self.__scripts["select"], comp_id= id).fetchall()
    
    def create(self, first_name, surname, phone, id):
        self.__db.execute(self.__scripts["insert new"], f_name = first_name, l_name = surname, ph = phone, comp_id = id)

    def get_max_id(self, id):
        return self.__db.execute(self.__scripts["get max id"], comp_id = id).fetchall()[0][0]
    
    def get_employee(self, id):
        return self.__db.execute(self.__scripts["select employee by id"], emp_id= id).fetchall()
    
    def update_employee(self, id, name):
        return self.__db.execute(self.__scripts["update employee"], emp_id= id, f_name = name)

    def delete(self, id):
        self.__db.execute(self.__scripts["delete employee by id"], id_to_delete = id)
     
    def delete_company(self, id):
        self.__db.execute(self.__scripts["delete company by id"], id_to_delete = id)
