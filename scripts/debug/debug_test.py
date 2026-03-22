# use with debugpy to debug a test case remotely
import pytest

# pytest.main(["-s","-vv", "./tests/test_base.py"])
pytest.main(["-s","-vv", "../../tests/test_periodic.py::TestPeriodicTasks::test_successful_execution_clears_executions_from_retries"])
