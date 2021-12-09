from diaries.AbstractDiary import AbstractDiary

class OiwaDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "グループワークは難しい。"

    def get_author(self):
        return "Oiwa"