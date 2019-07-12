import re
import tkinter

class Title:
    def __init__(self, raw_text="", title="", subtitle=""):
        if raw_text:
            self.raw_text = raw_text
            self.title = re.search(pattern=r"^[\w\s]+", string=raw_text).group(0).lstrip().upper()  # type: str
            self.subtitle = re.search(pattern=r"[\w\s]+$", string=raw_text).group(0).lstrip().title()  # type: str

    def get_title(self) -> str:
        return self.title

    def get_subtitle(self) -> str:
        return self.subtitle


starwars = Title("star wars: the empire strikes back")
print(starwars.get_title().center(60))
print(starwars.get_subtitle().center(60))


class NewWindow(tkinter.Frame):
    def __init__(self, **kw):
        super().__init__(**kw)


test1 = tkinter.Tk()
test1.geometry("500x500")
title_text = tkinter.Text(test1)
title_text.insert("1.0", starwars.title)
test1.mainloop()



