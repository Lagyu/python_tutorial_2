import sys
import re
from typing import List
from abc import ABCMeta, abstractmethod


class AbstractFileIO(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, path) -> None:
        pass

    @abstractmethod
    def write(self, text: str) -> None:
        pass


class WriteModeFileIO(AbstractFileIO):
    def __init__(self, path: str):
        super().__init__(path)
        self.path = path
        self.first_flag = True

    def write(self, text: str) -> None:
        if self.first_flag:
            with open(self.path, "w") as file:
                file.write(text)
                self.first_flag = False
        else:
            with open(self.path, "a") as file:
                file.write(text)


class AppendModeFileIO(AbstractFileIO):
    def __init__(self, path):
        super().__init__(path)
        self.path = path

    def write(self, text: str) -> None:
        with open(self.path, "a") as file:
            file.write(text)


class NullFileIO(AbstractFileIO):
    def __init__(self, path):
        super().__init__(path)

    def write(self, text: str) -> None:
        print(text)


class Controller:
    def __init__(self):
        self.listeners = []  # type: List[AbstractFileIO]

    def send(self, text):
        for listener in self.listeners:
            listener.write(text)

    def add_listener(self, listener: AbstractFileIO):
        self.listeners.append(listener)


def version():
    print(__version__)
    exit()

def help():
    print("tee - read from standard input and write to standard output and files")
    exit()


if __name__ == "__main__":

    __version__ = "0.1"

    args = sys.argv[1:]  # type: List[str]
    long_options = [arg for arg in args if arg.find("--") == 0]
    short_options = [arg for arg in args if (arg.find("-") == 0 and arg not in long_options)]
    out_files = [arg for arg in args if arg.find("-") == -1 or arg is "-"]

    if "--version" in long_options:
        version()

    if "--help" in long_options:
        help()

    controller = Controller()

    if len(out_files) == 0:
        if "-" in short_options:
            controller.add_listener(NullFileIO(""))
        else:
            print("No output argument detected.")
            help()

    for out_path in out_files:
        if "-a" in short_options or "--append" in long_options:
            controller.add_listener(AppendModeFileIO(out_path))
        else:
            controller.add_listener(WriteModeFileIO(out_path))

    piyo = True
    while piyo:
        try:
            in_text = input()
            print(in_text)
            controller.send(in_text)

        except KeyboardInterrupt:
            exit()

