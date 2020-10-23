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
        name_label_json = toga.Label(
            'Fichier JSON : ',
            style=Pack(padding=(0, 5))
        )
        self.filename_input = toga.TextInput(style=Pack(flex=1))
        self.filename_input.value = "myjson"
        name_input_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_input_box.add(name_label_json)
        name_input_box.add(self.filename_input)
        # Bouton pour convertir le JSON
        buttonLireJson = toga.Button(
            'Lire fichier JSON',
            on_press=self.lire_json,
            style=Pack(padding=5)
        )
        # Zone pour afficher le fichier JSON.

        self.texteZoneJson = toga.MultilineTextInput(
            id='view1', style=Pack(flex=1), readonly=True)
        self.texteZoneJson.MIN_HEIGHT = 200

        text_box_json = toga.Box(style=Pack(direction=ROW, padding=5))
        text_box_json.add(self.texteZoneJson)

        main_box.add(name_input_box)
        main_box.add(buttonLireJson)
        main_box.add(text_box_json)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def lire_json(self, widget):
        self.main_window.info_dialog(
            title="Fichier JSON", message="Lecture du fichier JSON")
        print('Start conversion JSON to AMC Tex file')
        question_liste = []
        fichier_json = self.filename_input.value
        AMC = Questionnaire(question_liste, fichier_json)
        AMC.importer_json()
        self.texteZoneJson.value = AMC.afficher_questionnaire()


def main():
    return AmcGenerator()
