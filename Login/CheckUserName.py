

def user_exist(username):
    try:
        with open('./BasicInfos/users.log','r',encoding='utf-8') as f:
            for line in f:
                line=line.strip()
                line_list=line.strip("$")
                if username==line_list[0]:
                    return True
        return False
    except Exception as e:
        print(e)

def login(password,username):
    try:
        with open('./BasicInfos/users.log', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                line_list = line.split("$")

                if not line_list=='':
                    if username==line_list[0] and password==line_list[1]:
                        return True
        return False
    except Exception as e:
        print(e)