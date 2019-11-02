

class MemberInfomation():
    def __init__(self,m_id,m_name,m_sex, m_parent, m_phone, m_face1, m_face2, m_face3, m_type,m_cishu, m_timelimit):
        self.member_id = m_id   #学员id
        self.member_name = m_name   #学员姓名
        self.member_sex = m_sex  #学员性别
        self.member_parent = m_parent #学员家长姓名
        self.member_phone = m_phone #学员电话号码
        self.member_faceid1 = m_face1 #人脸识别码1
        self.member_faceid2 = m_face2  #人脸识别码2
        self.member_faceid3 = m_face3  #人脸识别码3
        self.member_type = m_type   #办卡次数
        self.member_cishu = m_cishu #剩余次数
        self.member_timelimit = m_timelimit  # 剩余次数


    def get_name(self):
        return self.member_name

    def get_parent(self):
        return self.member_parent

    def get_phone(self):
        return self.member_phone

    def get_cishu(self):
        return self.member_cishu