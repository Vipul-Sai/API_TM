import unittest
from task_management_api.api_task_management import create_token
from task_management_api.api_task_management import API
import pytest


class Task_management_API(unittest.TestCase):

    @pytest.mark.api
    @pytest.mark.order(1)
    def test_api(self):
        create_token()
        t = API()
        t.user_info()
        # t.aggregate()
        # t.users()
        # t.create_task_mytask()
        # t.add_new_child()
        # t.create_task_teamtask()
        # t.add_existing_child()
        # t.add_existing_parent()
        # t.create_task_to_update()
        # t.update_task()
        # t.add_note()
        # t.status_update()
        # t.reference_update()
        # t.history()
        # t.overDue()
        # t.new()
        # t.inprogress()
        # t.onHold()
        # t.completed()
        # t.team_task()
        # t.team_task_owned_aggregate()
        # t.team_task_responsible_aggregate()