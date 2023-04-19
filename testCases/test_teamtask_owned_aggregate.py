import unittest
from task_management_api.api_task_management import create_token
from task_management_api.api_task_management import API
import pytest


class Task_management_API_teamtask_owned_aggregate(unittest.TestCase):

    @pytest.mark.api
    @pytest.mark.order(21)
    def test_api(self):
        create_token()
        t = API()
        t.team_task_owned_aggregate()