import requests


class EmployeeApi:
    def __init__(self, url):
        self.url = url
    
    def token(self, user='flora', pswrd='nature-fairy'):
        creds = {
        'username':user,
        'password':pswrd
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()['userToken']
    
    def get_employee(self, companyid):
        params_to_add = {'company' : str(companyid)}
        resp = requests.get(self.url+'/employee', params=params_to_add)
        return resp.json()
    
    def get_employee_by_id(self, empid):
        resp = requests.get(self.url+'/employee/' + str(empid))
        return resp.json()

    def create_employee(self, companyid, fname='Ann', lname='Kotikova', mname='Vladimirovna', email='nyutyan@gmail.com', url='https://t.me/KotikovaAnya', phone='+79529910101', birthdate='1988-10-17', isActive=True):
        employee = {
        "id" : 0,
        "firstName" : fname,
        "lastName" : lname,
        "companyId" : companyid,
        "isActive" : isActive,
        "middleName" : mname,
        "email" : email,
        "url" : url,
        "phone" : phone,
        "birthdate" : birthdate
        }
        my_headers = {}
        my_headers['x-client-token'] = self.token()
        resp = requests.post(self.url+'/employee', json=employee, headers=my_headers)
        return resp
    
    def edit_employee(self, empid, email='email1@google.com', url='https://url1.ru', isActive=False):
        edited = {
            "email": email,
            "url": url,
            "isActive": isActive
        }
        my_headers = {}
        my_headers['x-client-token'] = self.token()
        resp = requests.patch(self.url+'/employee/' + str(empid), json=edited, headers=my_headers)
        return resp.json()
