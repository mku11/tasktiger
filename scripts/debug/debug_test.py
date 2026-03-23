# use with debugpy to debug a test case remotely
import pytest

# pytest.main(["-s","-vv", "./tests/test_base.py"])
pytest.main(["-s", "-vv", "../../tests/test_base.py::TestCase::test_locked_task"])
