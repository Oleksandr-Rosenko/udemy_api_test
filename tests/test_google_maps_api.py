import json
from requests import Response
from utils.api import Google_maps_api
from utils.checking import Checking
"""Creating,edite,delete location"""
class Test_create_place():

    def test_create_new_place(self):

        print("Method POST")
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # token = json.loads(result_post.text)
        # print(list(token))
        Checking.check_json_value(result_post, 'status', 'OK')


        print("Method GET POST")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        # token = json.loads(result_get.text)
        # print(list(token))
        # "address": "29, side layout, cohen 09
        Checking.check_json_value(result_get, 'address', '29,side layout,cohen 09')

        print("Method PUT")
        result_put: Response = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')


        print("Method GET PUT")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("Testing is succsesfully  done !!!")





