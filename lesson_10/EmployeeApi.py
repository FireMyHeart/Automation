import requests
import allure


class EmployeeApi:
    def __init__(self, url):
        self.url = url

    @allure.step("Отправить через API логин {user} и пароль {pswrd} и получить токен")
    def token(self, user: str = 'flora', pswrd: str = 'nature-fairy') -> str:
        creds = {
            'username': user,
            'password': pswrd
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()['userToken']

    @allure.step("Получить через API всех сотрудников компании {companyid}")
    def get_employee(self, companyid: int) -> dict:
        params_to_add = {'company': str(companyid)}
        resp = requests.get(self.url+'/employee', params=params_to_add)
        return resp.json()

    @allure.step("Получить через API сотрудника {empid}")
    def get_employee_by_id(self, empid: int) -> dict:
        resp = requests.get(self.url+'/employee/' + str(empid))
        return resp.json()

    @allure.step("Создать через API сотрудника в компании с id {companyid}, передав имя {fname}, фамилию {lname}, отчество {mname}, email {email}, url {url}, телефон {phone}, дату рождения {birthdate}, флаг активен {isActive}")
    def create_employee(self, companyid: int, fname: str = 'Ann', lname: str = 'Kotikova', mname: str = 'Vladimirovna', email: str = 'nyutyan@gmail.com', url: str = 'https://t.me/KotikovaAnya', phone: str = '+79529910101', birthdate: str = '1988-10-17', isActive: bool = True) -> object:
        employee = {
            "id": 0,
            "firstName": fname,
            "lastName": lname,
            "companyId": companyid,
            "isActive": isActive,
            "middleName": mname,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate
        }
        my_headers = {}
        my_headers['x-client-token'] = self.token()
        resp = requests.post(self.url+'/employee', json=employee, headers=my_headers)
        return resp

    @allure.step("Изменить через API запись о сотруднике с id {empid}, передав новый email {email}, url {url}, флаг активен {isActive}")
    def edit_employee(self, empid: int, email: str = 'email1@google.com', url: str = 'https://url1.ru', isActive: bool = False) -> dict:
        edited = {
            "email": email,
            "url": url,
            "isActive": isActive
        }
        my_headers = {}
        my_headers['x-client-token'] = self.token()
        resp = requests.patch(self.url+'/employee/' + str(empid), json=edited, headers=my_headers)
        return resp.json()
