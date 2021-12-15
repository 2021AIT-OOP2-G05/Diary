from diaries.AbstractDiary import AbstractDiary

class TsunoDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-15"

    def get_summary(self):
        return "今締め切り十三分前"

    def get_author(self):
        return "Tsuno"