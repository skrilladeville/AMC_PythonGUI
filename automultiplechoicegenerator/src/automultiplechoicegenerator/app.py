"""
Générateur de questionnaire à choix multiples pour le logiciel Auto-Multiple-Choice.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class AmcGenerator(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            'Fichier AMC: ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)
        buttonConvert = toga.Button(
            'Convertir pour AMC!',
            on_press=self.start_convert,
            style=Pack(padding=5)
        )
        main_box.add(name_box)
        main_box.add(buttonConvert)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def start_convert(self, widget):
        print('Start conversion JSON to AMC Tex file')


def main():
    return AmcGenerator()
