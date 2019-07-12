import inspect


class FizzBuzz:
    def __init__(self, first=1, last=20, fizz_str="Fizz", buzz_str="Buzz"):
        if first <= last:
            self.start = first
            self.end = last + 1
        else:
            raise ValueError("end argument must be larger than start arg.")

        self.fizzbuzz_str = fizz_str + buzz_str
        self.fizz_str = fizz_str
        self.buzz_str = buzz_str

    def call_all(self):
        for i in range(self.start, self.end):
            self.call(i)

    def call(self, num: int):
        if num % 15 == 0:
            print(self.fizzbuzz_str, "(", num, ")")
        elif num % 3 == 0:
            print(self.fizz_str, "(", num, ")")
        elif num % 5 == 0:
            print(self.buzz_str, "(", num, ")")
        else:
            print(num)


if __name__ == "__main__":
    print("FizzBuzzをします。")
    keys = inspect.signature(FizzBuzz.__init__).parameters.keys()
    default_values = [param.default for param in inspect.signature(FizzBuzz.__init__).parameters.values()]
    default_values_dict = dict(zip(keys, default_values))

    def convert_num_input(input_str: str, key_name: str) -> int:
        try:
            return int(input_str)
        except ValueError:
            return default_values_dict[key_name]


    handler = FizzBuzz(
        first=convert_num_input(input("最初の数(デフォルト:" + str(default_values_dict["first"]) + ")："), "first"),
        last=convert_num_input(input("最後の数(デフォルト:" + str(default_values_dict["last"]) + ")："), "last"),
        fizz_str=input("fizzの文字列(デフォルト:" + default_values_dict["fizz_str"] + ")：") or default_values_dict["fizz_str"],
        buzz_str=input("buzzの文字列(デフォルト:" + default_values_dict["buzz_str"] + ")：") or default_values_dict["buzz_str"])
    handler.call_all()


