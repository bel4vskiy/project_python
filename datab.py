import json


class MyDB:

    def __init__(self):
        pass

    def add_user(self, login, psw):
        data = None
        if self.check_validaty(login):
            with open("user.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                data[login] = psw
            with open("user.json", 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
            return True
        else:
            return False


    def check_validaty(self, login):
        with open("user.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
            if len(data) > 0:
                try:
                    if data[f'{login}']:
                        return False
                except BaseException:
                    return True
            else:
                return True


    def check_access(self, login, psw):
        with open("user.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
            if len(data) > 0:
                try:
                    if data[f'{login}'] == psw:
                        return True
                except BaseException:
                    return False
            else:
                return False

            



db = MyDB()
print(db.add_user('pobeda', 'yes'))

