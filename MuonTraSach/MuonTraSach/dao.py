import json, os



def auth_user(username, password):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "data", "user.json")
    with open(file_path, encoding="utf8") as f:
        users = json.load(f)
        for u in users:
            if u["username"] == username and u["password"] == password:
                return True


    return False




if __name__ == '__main__':
    print(auth_user("user1", 2))