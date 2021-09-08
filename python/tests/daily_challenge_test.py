import pytest

try:
    import python.daily_challenge
except ImportError:
    pytest.skip("Skipping module import", allow_module_level=True)


class Test_Daily_challenge_Format_post_body:
    def test_format_post_body_fail(self):
        result = python.daily_challenge.format_post_body({}, 5)
        assert pytest.raises(Exception)
