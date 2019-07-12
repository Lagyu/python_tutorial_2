# 1
import datetime
import locale
import sys


def show_date(date=datetime.date.today(), format_str="本日は、{0:%Y-%m-%d}です。") -> None:
    print(format_str.format(date))
    return


show_date(datetime.date(2019, 4, 16))
show_date(datetime.date(2020, 7, 24), "東京オリンピックの開会式は、{0:%Y-%m-%d}です。")

# 2

locale.setlocale(locale.LC_TIME, 'ja.utf-8')


def show_date_in_japanese(zero_fill=False) -> None:
    date = datetime.date.today()
    if zero_fill:
        print("本日は、{0:%m}月{1:%d}日です。".format(date, date))
    else:
        print("本日は、" + date.strftime("%m").lstrip("0") + "月"
              + date.strftime("%d").lstrip("0") + "日です。")


show_date_in_japanese()


# 3
def show_date_in_japanese_with_day_of_week(zero_fill=False) -> None:
    date = datetime.date.today()
    if zero_fill:
        print("本日は、{0:%m}月{0:%d}日{0:%A}です。".format(date))
    else:
        print("本日は、" + date.strftime("%B").lstrip("0")
              + date.strftime("%d").lstrip("0") + "日" + date.strftime("%A") + "です。")


show_date_in_japanese_with_day_of_week()

print(sys.stdout.encoding)

