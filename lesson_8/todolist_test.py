from ToDoList import ToDoList

api = ToDoList('https://todo-app-sky.herokuapp.com')

# получить список задач
def test_get_tasks():
    api.create_task('Task1')
    tasks_list = api.get_tasks()
    assert len(tasks_list) > 0

# создать задачу
def test_create_task():
    new_task = api.create_task('Выполнить домашнюю работу №9 по питону')
    assert new_task.json()['id']
    assert new_task.status_code == 201

# поиск конкретной задачи
def test_find_task():
    new_task = api.create_task('Task to be find')
    taskid = new_task.json()['id']
    result = api.get_task_by_id(taskid)
    assert result['id'] == taskid

# изменение названия задачи
def test_edit_title():
    new_task = api.create_task('Task to be edited')
    taskid = new_task.json()['id']
    result = api.update_task(taskid, 'Edited task')
    assert result['title'] != new_task.json()['title']
    assert result['completed'] == new_task.json()['completed']

# изменение статуса на выполнено
def test_edit_status_true():
    new_task = api.create_task('Task to be completed')
    taskid = new_task.json()['id']
    result = api.completed_true(taskid)
    assert result['completed'] == True

# изменение статуса на не выполнено
def test_edit_status_false():
    new_task = api.create_task('Task not to be completed')
    taskid = new_task.json()['id']
    api.completed_true(taskid)
    res2 = api.completed_false(taskid)
    assert res2['completed'] == False

# удаление задачи
def test_delete_task():
    new_task = api.create_task('Task to be deleted')
    taskid = new_task.json()['id']
    list_of_tasks1 = api.get_tasks()
    result = api.delete_task(taskid)
    list_of_tasks2 = api.get_tasks()
    assert result.status_code == 204
    assert len(list_of_tasks2) == len(list_of_tasks1) - 1
