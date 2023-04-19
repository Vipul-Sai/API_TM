import unittest
from task_management_api.api_task_management import create_token
from task_management_api.api_task_management import API
import pytest


class Task_management_API_new(unittest.TestCase):

    @pytest.mark.api
    @pytest.mark.order(16)
    def test_api(self):
        create_token()
        t = API()
        t.new()