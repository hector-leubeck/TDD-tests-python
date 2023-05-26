import requests


class People:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.data = False

    def connect_in_api(self):
        response = requests.get("https://jsonplaceholder.typicode.com/users/1")

        if response.ok:
            self.data = True
            return 'CONNECTED'
        return ("ERRO 404")
        self.data = False
