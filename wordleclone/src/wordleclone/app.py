"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER


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
        self.word_input = toga.TextInput(style=Pack(flex=1))

        guess_box = toga.Box(style=Pack(direction=ROW, padding=5))
        guess_box.add(guess_label)
        guess_box.add(self.word_input)

        guess_button = toga.Button(
            "Guess",
            on_press=self.guess_word,
            style=Pack(padding=5)
        )

        alphabet_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        alphabet_label = toga.Label(
            "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z",
            style=Pack(text_align=CENTER)
        )
        alphabet_box.add(alphabet_label)

        main_box.add(guess_box)
        main_box.add(guess_button)
        main_box.add(alphabet_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    async def guess_word(self, widget):
        self.main_window.info_dialog(
            "Your Guess",
            f"{valid_word(self.word_input.value)}",
        )
def main():
    return WordleClone()
