"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


def valid_word(word):
    if len(word) == 5:
        return word
    else:
        return "Not a valid word"


class WordleClone(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        guess_label = toga.Label(
            "Guess: ",
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        guess_box = toga.Box(style=Pack(direction=ROW, padding=5))
        guess_box.add(guess_label)
        guess_box.add(self.name_input)

        button = toga.Button(
            "Guess",
            on_press=self.guess_word,
            style=Pack(padding=5)
        )

        main_box.add(guess_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    async def guess_word(self, widget):
        self.main_window.info_dialog(
            "Your Guess",
            f"{valid_word(self.name_input.value)}",
        )
def main():
    return WordleClone()
