import pytest
import requests
from jsonschema import validate, ValidationError

def pytest_yaml_run_step(item):
    step = item.current_step

    key = list(step)[0]
    value = list(step.vlaues())[0]

    match key:
        case 'request':
            item.resp = requests.request(**value)
        case 'response':
            responses_validator.validator(item.resp, **value)
