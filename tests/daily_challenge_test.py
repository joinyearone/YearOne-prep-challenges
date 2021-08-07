import pytest
from .. import daily_challenge

class Test_Daily_challenge_Format_post_body:
    def test_format_post_body_1(self):
        result = daily_challenge.format_post_body({ "title": "title", "body": "text body", "author_name": "something@example.com", \
                                                    "difficulty": True, "author_email": "user@host:300" },5)
        title, topic, author = result
        assert isinstance(title, str)
        assert isinstance(topic, str)
        assert isinstance(author, str)
        assert all(result)

    def test_format_post_body_fail(self):
        result = daily_challenge.format_post_body({},5)
        assert pytest.raises(Exception)
