from diaries.AbstractDiary import AbstractDiary

class NoharaDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-13"

    def get_summary(self):
        return """よくわからないけど作業中"""

    def get_author(self):
        return "Nohara"