import requests

class ToDoList:
    def __init__(self, url):
        self.url = url
    
    def get_tasks(self):
        resp = requests.get(self.url)
        return resp.json()
    
    def create_task(self, title):
        task = {'title' : title}
        resp = requests.post(self.url, json=task)
        return resp
    
    def get_task_by_id(self, taskid):
        resp = requests.get(self.url + '/' + str(taskid))
        return resp.json()
    
    def update_task(self, taskid, title):
        body = {"title": title}
        resp = requests.patch(self.url + '/' + str(taskid), json = body)
        return resp.json()
    
    def completed_true(self, taskid):
        body = {"completed": True}
        resp = requests.patch(self.url + '/' + str(taskid), json = body)
        return resp.json()
    
    def completed_false(self, taskid):
        body = {"completed": False}
        resp = requests.patch(self.url + '/' + str(taskid), json = body)
        return resp.json()

    def delete_task(self, taskid):
        resp = requests.delete(self.url + '/' + str(taskid))
        return resp
