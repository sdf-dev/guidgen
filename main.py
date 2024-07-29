import uuid

def get_users():
    try:
        f = open("users.csv", "r")
        user_list = []
        for i in f:
            string = i.lower()
            string.replace(",", "")             
            user_list.append(string)
        guid_gen(user_list)
    except IOError:
        print("Error occured when trying to read from file..")

def guid_gen(user_list):
    updated_users = {}
    for i in range(len(user_list) -1 ):
        updated_users[user_list[i]] = str(uuid.uuid4())
    return updated_users

if __name__ == "__main__":
    get_users()


