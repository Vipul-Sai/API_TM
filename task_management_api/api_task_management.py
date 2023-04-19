import unittest
import requests
import json
from utilities.configReader import readConfig

auth = None

def create_token():
    body = {
        'username': 'vipuladmin',
        'password': 'test',
        'client_id': 'camunda-identity-service',
        'grant_type': 'password',
        'client_secret': '7c4599a1-d425-4af1-8daf-3ce1948213b7'
    }
    url = readConfig('Token_API', 'token')
    response = requests.post(url, data=body)
    print(response.status_code)
    # print(response.json)
    json_data = response.json()
    # print(json_data)
    a_token = json_data['access_token']
    global auth
    auth = a_token


task_id_one = None
task_id_two = None
childtask = None
task_to_update = None
owner_id = 1092745609490669568

class API(unittest.TestCase):

    def user_info(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/user-info"
        url = readConfig('url', 'weburl') + endpoint
        response = requests.get(url, headers= headers)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False

    def aggregate(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/my-tasks/aggregate"
        url = readConfig('url', 'weburl') + endpoint
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False

    def users(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/users"
        url = readConfig('url', 'weburl') + endpoint
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False

    def filter_after_login(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "https://api-cm-uat.techsophy.com/api/task-management/v1/tasks/filters?page=1&size=25&orFilters=assignee:"+str(owner_id)+",owner:"+str(owner_id)+"&andFilters="
        url = readConfig('url', 'weburl') + endpoint
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False


    def create_task_mytask(self):
        headers = {
            'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/tasks"
        url = readConfig('url', 'weburl') + endpoint
        file = open('Data/createTask.json', 'r')
        json_file = json.loads(file.read())
        response = requests.post(url, headers=headers, json=json_file)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False
        json_data = response.json()
        t1 = json_data['data']['id']
        # print(t1)
        global task_id_one
        task_id_one = t1
        print(task_id_one)
        print("Task created")


    def add_new_child(self):
        print(task_id_one)

        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/tasks"
        url = readConfig('url', 'weburl') + endpoint
        file = open('Data/add_new_child.json', 'r')
        json_file = json.loads(file.read())
        json_file['parentTaskId'] = task_id_one
        response = requests.post(url, headers=headers, json=json_file)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False
        json_data = response.json()
        ct = json_data['data']['id']
        global childtask
        childtask = ct
        print(childtask)

    def create_task_teamtask(self):
        headers = {
            'Authorization': 'Bearer' + ' ' + str(auth)
        }
        endpoint = "task-management/v1/tasks"
        url = readConfig('url', 'weburl') + endpoint
        file = open('Data/createTask_Team.json', 'r')
        json_file = json.loads(file.read())
        response = requests.post(url, headers=headers, json=json_file)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False
        json_data = response.json()
        task_id2 = json_data['data']['id']
        # print(task_id2)
        global task_id_two
        task_id_two = task_id2
        print(task_id_two)


    def add_existing_child(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = 'task-management/v1/tasks/'+str(childtask)
        url = readConfig('url','weburl')+endpoint
        file = open('Data/add_existing_child.json','r')
        json_file = json.loads(file.read())
        json_file['parentTaskId'] = task_id_two
        response = requests.patch(url, headers=headers, json=json_file)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False

    def add_existing_parent(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = 'task-management/v1/tasks/'+str(task_id_one)
        url = readConfig('url','weburl')+endpoint
        file = open('Data/add_existing_child.json','r')
        json_file = json.loads(file.read())
        json_file['parentTaskId'] = task_id_two
        response = requests.patch(url, headers=headers, json=json_file)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False

    def create_task_to_update(self):
            headers = {
                'Authorization': 'Bearer' + ' ' + str(auth)}
            endpoint = "task-management/v1/tasks"
            url = readConfig('url', 'weburl') + endpoint
            file = open('Data/createTasktoupdate.json', 'r')
            json_file = json.loads(file.read())
            response = requests.post(url, headers=headers, json=json_file)
            print(response.status_code)
            if response.status_code == 200:
                assert True
            else:
                assert False
            json_data = response.json()
            t1 = json_data['data']['id']
            # print(t1)
            global task_to_update
            task_to_update = t1
            print(task_to_update)

    def update_task(self):
        headers = {
            'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/tasks/"+str(task_to_update)
        url = readConfig('url', 'weburl') + endpoint
        file = open('Data/updateTask.json', 'r')
        json_file = json.loads(file.read())
        response = requests.patch(url, headers=headers, json=json_file)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False


    def add_note(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/notes"
        url = readConfig('url', 'weburl') + endpoint
        file = open('Data/notes.json', 'r')
        json_file = json.loads(file.read())
        json_file['taskId'] = task_to_update
        response = requests.post(url, headers=headers, json=json_file)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False

        json_data = response.json()
        print(json_data)

    def status_update(self):
        headers = {
            'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/tasks/"+str(task_to_update)
        url = readConfig('url', 'weburl') + endpoint
        file = open('Data/status_update.json', 'r')
        json_file = json.loads(file.read())
        response = requests.patch(url, headers=headers, json=json_file)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False

    def reference_update(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/tasks/"+str(task_to_update)
        url = readConfig('url', 'weburl') + endpoint
        file = open('Data/reference.json', 'r')
        json_file = json.loads(file.read())
        response = requests.patch(url, headers=headers, json=json_file)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False

    def history(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/tasks/audit/"+str(task_to_update)
        url = readConfig('url', 'weburl') + endpoint

        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False

    def overDue(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/tasks/due?page=1&size=25&owner="+str(owner_id)+"&tasks-category=myTasks"
        url = readConfig('url', 'weburl') + endpoint

        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False

    def new(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/tasks/filters?page=1&size=25&orFilters=assignee:"+str(owner_id)+",owner:"+str(owner_id)+"&andFilters=status:New,"
        url = readConfig('url', 'weburl') + endpoint

        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False

    def onHold(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/tasks/filters?page=1&size=25&orFilters=assignee:"+str(owner_id)+",owner:"+str(owner_id)+"&andFilters=status:OnHold,"
        url = readConfig('url', 'weburl') + endpoint

        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False

    def inprogress(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/tasks/filters?page=1&size=25&orFilters=assignee:"+str(owner_id)+",owner:"+str(owner_id)+"&andFilters=status:InProgress,"
        url = readConfig('url', 'weburl') + endpoint

        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False

    def completed(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/tasks/filters?page=1&size=25&orFilters=assignee:"+str(owner_id)+",owner:"+str(owner_id)+"&andFilters=status:Completed,"
        url = readConfig('url', 'weburl') + endpoint

        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False





    def team_task(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/team-tasks"
        url = readConfig('url', 'weburl') + endpoint

        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False

    def team_task_owned_aggregate(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/team-tasks/aggregate?tasks-category=ownedTasks"
        url = readConfig('url', 'weburl') + endpoint

        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False

    def team_task_responsible_aggregate(self):
        headers = {'Authorization': 'Bearer' + ' ' + str(auth)}
        endpoint = "task-management/v1/team-tasks/aggregate?tasks-category=responsibleTasks"
        url = readConfig('url', 'weburl') + endpoint

        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False















