from diaries.AbstractDiary import AbstractDiary

class DiarySample(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "今日初のグループワークが始まりその難易度の高さに絶望しているところだ。"

    def get_author(self):
        return "Onishi"