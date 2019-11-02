class CardInfo():
    def __init__(self ,c_type, c_info):
        self.card_type = c_type #会员卡种类
        self.card_info = c_info #会员卡信息


    def get_type_info(self):
        return self.card_type,self.card_info