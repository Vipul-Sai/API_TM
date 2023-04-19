import unittest
from task_management_api.api_task_management import create_token
from task_management_api.api_task_management import API
import pytest


class Task_management_API_createTaskMytask(unittest.TestCase):

    @pytest.mark.api
    @pytest.mark.order(4)
    def test_api(self):
        create_token()
        t = API()
        t.create_task_mytask()