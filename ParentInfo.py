class ParentInfo():
    def __init__(self ,p_name, p_phone,p_idcard,p_address):
        self.parent_name = p_name #家长姓名
        self.parent_phone = p_phone #家长电话
        self.parent_idcard = p_idcard #家长身份证号码
        self.parent_address = p_address #家庭住址

    def get_name(self):
        return self.parent_name

    def get_phone(self):
        return self.parent_phone

    def get_idcard(self):
        return self.parent_idcard

    def get_address(self):
        return self.parent_address
