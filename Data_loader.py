# VK API is used to load the data (для работы использовался VK API)
# URL: https://vk.com/dev/methods

%pip install vk_api
import json
import vk_api
def main():

  # authorization (авторизация)

  vk_session = vk_api.VkApi('login', 'password')
  vk_session.auth()

  # initializing VK tools (инициализация VK tools)

  tools = vk_api.VkTools(vk_session)

  # initializing wall.get method (инициализация метода wall.get)

  wall = tools.get_all('wall.get', 100, {'domain': '---'})

  # saving the JSON object with the data (сохранение JSON-объекта с полученными данными)

  with open('output.json', 'w') as fw:json.dump(wall, fw, ensure_ascii=False)

  return wall

if __name__ == '__main__':
    main()
