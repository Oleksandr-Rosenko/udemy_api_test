from utils.http_method import http_methods

"""Metods for testing google maps API"""

base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"


class Google_maps_api():
    @staticmethod
    def create_new_place():

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Front line house",
            "phone_number": "(+91)9838933937",
            "address": "29,side layout,cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        post_resource = "/maps/api/place/add/json"
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = http_methods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post
