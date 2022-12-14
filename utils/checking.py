"""Method for checking"""
import json

from requests import Response
class Checking():
    @staticmethod
    def check_status_code (response: Response,status_code ):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Succsesfully!!! Status  Code = " + str(response.status_code))
        else:
            print("Failed!!! Status  Code = " + str(response.status_code))

    """Method for checking required fields"""
    @staticmethod
    def check_json_token(response: Response,expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print(" All fields is present")







