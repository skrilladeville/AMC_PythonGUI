"""
Générateur de questionnaire à choix multiples pour le logiciel Auto-Multiple-Choice.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER, LEFT, RIGHT
from .util import Questionnaire


class AmcGenerator(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))
        # Choix du nom du fichier JSON
        name_label = toga.Label(
            'Fichier JSON : ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))
        self.name_input.value = "myjson"
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)
        # Bouton pour convertir le JSON
        buttonConvert = toga.Button(
            'Lire fichier JSON',
            on_press=self.start_convert,
            style=Pack(padding=5)
        )
        # Zone pour afficher le résultat.

        self.texteZone = toga.MultilineTextInput(
            id='view1', style=Pack(flex=1), readonly=True)

        text_box = toga.Box(style=Pack(direction=ROW, padding=5))
        text_box.add(self.texteZone)

        main_box.add(name_box)
        main_box.add(buttonConvert)
        main_box.add(text_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def start_convert(self, widget):
        self.main_window.info_dialog(
            title="Convertion", message="Conversion du JSON en AMC")
        print('Start conversion JSON to AMC Tex file')
        question_liste = []
        fichier_json = self.name_input.value
        AMC = Questionnaire(question_liste, fichier_json)
        AMC.importer_json()
        self.texteZone.value = AMC.afficher_questionnaire()


def main():
    return AmcGenerator()
