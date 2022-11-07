from requests import Response
from utils.api import Google_maps_api


"""Creating,edidting,deleteing location"""
class test_create_place():

    def test_create_new_place(self):

        print("POST method")
        result_post: Response = Google_maps_api.create_new_place()
