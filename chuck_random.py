import requests
"""Create new joke"""
class  tes_new_joke ():
  def __init__(self):
      pass

  # def test_create_new_random_joke(self):
  #   """Create new random joke"""
  #   url = "https://api.chucknorris.io/jokes/random"
  #   print(url)
  #   result = requests.get(url)
  #   print("Status Code:" + str(result.status_code))
  #   assert 200 == result.status_code
  #   if  result.status_code == 200:
  #       print("Successful new joke is created !!!")
  #   else:
  #       print("Fail")
  #   result.encoding = 'utf-8'
  #   print(result.text)
  #   check = result.json()
  #   # check_info = check.get("categories")
  #   # print(check_info)
  #   # assert  check_info ==[]
  #   # print("Categories is  true")
  #   check_info_value = check.get("value")
  #   print(check_info_value)
  #   name = "Chuck"
  #   if name in check_info_value:
  #       print("Chuck name indeed present in joke")
  #   else:
  #       print("Chuck name  not present in  joke ")
  def test_create_new_categories_joke(self):
    """Create new from any  categories  joke"""
    categories = "sport"
    url = "https://api.chucknorris.io/jokes/random?category="+ categories
    print(url)
    result = requests.get(url)
    print("Status Code:" + str(result.status_code))
    assert 200 == result.status_code
    if  result.status_code == 200:
        print("Successful new joke is created !!!")
    else:
        print("Fail")
    result.encoding = 'utf-8'
    print(result.text)
    check = result.json()
    check_info = check.get("categories")
    print(check_info)
    assert  check_info ==["sport"]
    print("Categories is  true")
    # check_info_value = check.get("value")
    # print(check_info_value)
    # name = "Chuck"
    # if name in check_info_value:
    #     print("Chuck name indeed present in joke")
    # else:
    #     print("Chuck name  not present in  joke ")

# random_joke = tes_new_joke()
# random_joke.test_create_new_random_joke()
sport_joke = tes_new_joke()
sport_joke.test_create_new_categories_joke()


