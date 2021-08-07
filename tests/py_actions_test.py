import pytest
from .. import py_actions


class Test_Py_actions_Get_post_count:
    def test_get_post_count_1(self):
        result = py_actions.get_post_count(
            "03ea49f8-1d96-4cd0-b279-0684e3eec3a9")
        assert pytest.raises(Exception)


class Test_Py_actions_Post_to_circle:
    def test_post_to_circle_1(self):
        result = py_actions.post_to_circle(
            "7289708e-b17a-477c-8a77-9ab575c4b4d8", "01:04:03", "cool", "email@Google.com")
        assert pytest.raises(Exception)
