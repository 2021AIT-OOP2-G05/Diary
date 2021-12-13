from diaries.AbstractDiary import AbstractDiary

class HayashiDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "疲れたー"

    def get_author(self):
        return "Sample"