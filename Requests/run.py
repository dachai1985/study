import os
import pytest

pytest.main()
os.system('allure generate -o report temps')