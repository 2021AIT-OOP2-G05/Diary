from diaries.AbstractDiary import AbstractDiary

class FukushimaDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-12"

    def get_summary(self):
        return "多分Github、おもしろい。多分。"

    def get_author(self):
        return "Fukushima"