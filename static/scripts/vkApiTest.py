# coding: utf8
import vk

session = vk.Session()
vk_api = vk.API(session)

def vkApiTest(_id):
    getSearch = vk_api.users.get(user_id=_id)
    print(getSearch)
    return getSearch

# vkApiTest(210700286)
