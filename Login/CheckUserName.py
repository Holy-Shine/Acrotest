
import json

def user_exist(username):
    try:
        f = open('./BasicInfos/user.json', encoding='utf-8')
        user_dic = json.load(f)
        for item in user_dic:
            if(username == item):
                return True
        return False
    except Exception as e:
        print(e)


def login(password,username):
    try:
        f = open('./BasicInfos/user.json', encoding='utf-8')
        user_dic = json.load(f)
        if username in user_dic:
            info = user_dic[username]
            if(info[0]['pwd']==password and info[0]['user']==username):
                return True
        return False
    except Exception as e:
        print(e)

#修改密码
def Changpwd(newpwd,oldpwd,username):
    try:
        f = open('./BasicInfos/user.json', encoding='utf-8')
        user_dic = json.load(f)
        if username in user_dic:
            info = user_dic[username]
            if (info[0]['pwd'] == oldpwd and info[0]['user'] == username):
                info[0]['pwd']=newpwd
                with open('./BasicInfos/user.json', "w") as f:
                    json.dump(user_dic, f)
                return True
        return False
    except Exception as e:
        print(e)

#修改二级密码
def ChangVerify(newve,oldve):
    try:
        f = open('./BasicInfos/Verify.json', encoding='utf-8')
        user_dic = json.load(f)
        if user_dic['Verify'][0]['pwd'] == oldve:
            user_dic['Verify'][0]['pwd'] = newve
            with open('./BasicInfos/Verify.json', "w") as f:
                json.dump(user_dic, f)
            return True
        return False
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # flag = ChangVerify('123456','123')
    flag =  login('123456','Wangliping',)
    print(flag)