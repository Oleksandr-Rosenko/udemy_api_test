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

    """Cheking value required fields"""
    @staticmethod
    def check_json_value(response: Response,field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + "\n True")









