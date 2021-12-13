from diaries.DiarySample import DiarySample
from diaries.FukushimaDiary import FukushimaDiary
from diaries.HayashiDiary import HayashiDiary
from diaries.OiwaDiary import OiwaDiary
from diaries.OnishiDiary import OnishiDiary
from diaries.DiarySample import DiarySample
from diaries.FujimotoDiary import FujimotoDiary
from diaries.FukushimaDiary import FukushimaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  DiarySample(),
  HayashiDiary(),
  OnishiDiary(),
  FujimotoDiary(),
  OiwaDiary(),
  FukushimaDiary(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()