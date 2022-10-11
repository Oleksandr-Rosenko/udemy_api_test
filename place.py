import requests

class test_new_location ():
    """"Work with new location"""
    def test_create_new_location(self):
        """"Create new location"""
        base_url = "https://rahulshettyacademy.com"
        key = "?key = qaclick123"
        post_resource = "/maps/api/place/add/json"

        post_url = base_url + post_resource + key

        json_for_create_new_location = {

        "location":{
        "lat":-38.383494,
        "lng":33.427362
        }, "accuracy":50,
        "name":"Frontline house",
        "phone_number":"(+91)9838933937",
        "address": "29, side layout, cohen 09",
        "types":[
        "shoe park",
        "shop"
        ],
        "website":"http://google.com",
        "language":"French-IN"
        }
        result_post = requests.post(post_url, json = json_for_create_new_location)
        print(result_post.text)
        print("Status Code:" + str(result_post.status_code))
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print("Successful, New location is created !!!")
        else:
            print("Fail")
        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("Status code in  body: " + check_info_post)
        assert check_info_post == "OK"
        print("Status code is correct")
        place_id = check_post.get("place_id")
        print("Place_id : " + place_id)

        """Checking  the new location created  correct"""

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Status Code:" + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Checking  the new location created  correct: Successful ")
        else:
            print("Fail")

new_place = test_new_location()
new_place.test_create_new_location()
