from diaries.AbstractDiary import AbstractDiary

class FujimotoDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "GitHubわからん"

    def get_author(self):
        return "Fujimoto"