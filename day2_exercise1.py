from abc import ABCMeta, abstractmethod
from datetime import date
from typing import Union

if __name__ == "__main__":

    # 1
    temp_c = 100
    temp_f = temp_c * 9 / 5 + 32

    print(temp_f)


    # 2
    def cels_to_fahr(cels: float):
        return cels * 9 / 5 + 32


    print(cels_to_fahr(0))

    # 3
    while True:
        cels_input = input("本日の気温（摂氏）を入力してください：")
        try:
            cels_input_num: float = float(cels_input)
            print("=> 華氏: {0:.1f}".format(cels_to_fahr(cels_input_num)))
            break

        except ValueError:
            print("エラー：半角整数または少数で入力してください。")
            continue


# 4
class AbstractStrToFloatConverter(metaclass=ABCMeta):
    @abstractmethod
    def convert(self, from_str: str) -> float:
        return float()


class StrToFloatConverter(AbstractStrToFloatConverter):
    def convert(self, from_str: str) -> float:
        try:
            return float(from_str)
        except ValueError:
            print("エラー：整数または小数に変換できません。")
            return None


class AbstractDisplay(metaclass=ABCMeta):
    @abstractmethod
    def display(self, num_float: float):
        pass


class AbstractFerhDisplay(AbstractDisplay):
    @abstractmethod
    def display(self, num_float: float):
        super().display(num_float)


class FerhPrettyDisplay(AbstractFerhDisplay):
    def display(self, num_float: float):
        print("=> 華氏: {0:.1f}".format(num_float))


class AbstractCelsToFerhConverter(metaclass=ABCMeta):
    def __init__(self, str_to_float_converter: AbstractStrToFloatConverter, ferh_display: AbstractDisplay):
        pass

    @abstractmethod
    def convert(self, cels_float: float) -> float:
        pass

    @abstractmethod
    def continuous_interactive_convert(self):
        pass


class CelsToFerhConverter(AbstractCelsToFerhConverter):
    def __init__(self, str_to_float_converter: AbstractStrToFloatConverter, ferh_display: AbstractDisplay):
        super().__init__(str_to_float_converter, ferh_display)
        self.str_to_float_converter = str_to_float_converter
        self.ferh_pretty_display = ferh_display

    def convert(self, cels_float: float) -> float:
        return cels_float * 9 / 5 + 32

    def continuous_interactive_convert(self):
        while True:
            cels_input_str = input("本日の気温（摂氏）を入力してください(qで終了)：")
            if cels_input_str is "q" or cels_input is "Q":
                break

            cels_float = self.str_to_float_converter.convert(cels_input_str)
            if cels_float:
                ferh_float = self.convert(cels_float)
                self.ferh_pretty_display.display(ferh_float)
            continue


if __name__ == "__main__":
    converter = CelsToFerhConverter(StrToFloatConverter(), FerhPrettyDisplay())
    converter.continuous_interactive_convert()


class AbstractTempMode(metaclass=ABCMeta):
    @abstractmethod
    def calc(self, original_value: float) -> float:
        pass

    @abstractmethod
    def restore_calc(self, value: float) -> float:
        pass

    @abstractmethod
    def unit_english(self) -> str:
        pass

    @abstractmethod
    def unit_japanese(self) -> str:
        pass


class CelsiusMode(AbstractTempMode):
    def calc(self, original_value: float) -> float:
        return original_value

    def restore_calc(self, value: float) -> float:
        return value

    def unit_english(self) -> str:
        return "C"

    def unit_japanese(self) -> str:
        return "摂氏"


class FahrenheitMode(AbstractTempMode):
    def calc(self, original_value: float) -> float:
        return original_value * 9 / 5 + 32

    def restore_calc(self, value: float) -> float:
        return (value - 32) * 5 / 9

    def unit_english(self) -> str:
        return "F"

    def unit_japanese(self) -> str:
        return "華氏"


class AbstractDayTempData(metaclass=ABCMeta):
    def __init__(self, date_data: date, high_temp: float, low_temp: float, mode: AbstractTempMode):
        self.date = date_data
        self.high_temp = high_temp
        self.low_temp = low_temp
        self.mode = mode

    def __repr__(self):
        return repr((self.date, self.high_temp, self.low_temp))

    def __lt__(self, other):
        return self.date < other.date

    @abstractmethod
    def get_date(self) -> date:
        pass

    @abstractmethod
    def get_high(self) -> float:
        pass

    @abstractmethod
    def get_low(self) -> float:
        pass

    @abstractmethod
    def get_list(self) -> list:
        pass

    @abstractmethod
    def change_mode(self, new_mode: AbstractTempMode):
        pass


class DayTempData(AbstractDayTempData):
    def __init__(self, date_data: date, high_temp: float, low_temp: float, mode: AbstractTempMode):
        super().__init__(date_data, high_temp, low_temp, mode)

    def get_date(self):
        return self.date

    def get_high(self):
        return self.high_temp

    def get_low(self):
        return self.high_temp

    def get_list(self):
        return [self.date, self.high_temp, self.low_temp]

    def change_mode(self, new_mode: AbstractTempMode):
        self.high_temp = new_mode.calc(self.mode.restore_calc(self.high_temp))
        self.low_temp = new_mode.calc(self.mode.restore_calc(self.low_temp))


class AbstractOverwriteAskAgent(metaclass=ABCMeta):
    def ask(self, old: AbstractDayTempData, new: AbstractDayTempData) -> bool:
        pass


class DuplicateOverwriteAskAgent(AbstractOverwriteAskAgent):
    def ask(self, old: AbstractDayTempData, new: AbstractDayTempData) -> bool:
        print("")
        print("old: ", old)
        print("new: ", new)
        answer = input("重複データがあります。更新しますか？(y/N)")

        if answer == "y" or answer == "Y":
            print("上書きしました。")
            return True
        else:
            return False


class DataStore:
    def __init__(self, overwrite_ask_agent: AbstractOverwriteAskAgent, day_temp_data_list=None):
        if day_temp_data_list:
            self.day_temp_data_list = day_temp_data_list
        else:
            self.day_temp_data_list = []
        self.overwrite_ask_agent = overwrite_ask_agent

    def __repr__(self):
        return str(self.day_temp_data_list)

    def change_mode(self, mode: AbstractTempMode):
        for data in self.day_temp_data_list:
            data.change_mode(mode)
        return self

    def add(self, new_data_obj: AbstractDayTempData):
        is_new = True
        for data in self.day_temp_data_list:
            if data.get_date == new_data_obj:
                is_new = False
                old_data = data
                overwrite_flag = self.overwrite_ask_agent.ask(old_data, new_data_obj)

                if overwrite_flag:
                    self.day_temp_data_list.remove(old_data)
                    self.day_temp_data_list.append(new_data_obj)
                    self.day_temp_data_list.sort()

        if is_new:
            self.day_temp_data_list.append(new_data_obj)
            self.day_temp_data_list.sort()

    def get_single_data(self, target_date: date):
        result = None
        for data_obj in self.day_temp_data_list:
            if data_obj.get_date is target_date:
                return result

        return result

    def get_period_date(self, from_date: date, to_date: date):
        result = []
        for data_obj in self.day_temp_data_list:
            if from_date <= data_obj.get_date <= to_date:
                result.append(data_obj)

        return self.__class__(self.overwrite_ask_agent, result)


if __name__ == "__main__":
    store = DataStore(DuplicateOverwriteAskAgent())
    data_set = [[35.1, 24.8], [37.3, 26.7], [35.4, 27.3], [34.1, 26.1],
                [34.7, 27.2], [34, 27], [24.3, 20.9], [25.1, 21.4], [32.1, 23.8], [34.5, 27], [33.6, 26],
                [31.1, 25.6], [34.1, 26.1], [34.1, 23.9], [33.1, 27.2], [32.3, 27.3], [30, 24.7], [27.2, 18.3]]
    for i in range(1, 19):
        new_data = DayTempData(date(2018, 8, i), data_set[i-1][0], data_set[i-1][1], CelsiusMode())
        store.add(new_data)
    store.change_mode(FahrenheitMode())
    print(store)

