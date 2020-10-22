import json


class Questionnaire:

    questionnaire = []  # Questionnaire en cours
    fichier_json = ''  # Nom du fichier json contenant les questions

    def __init__(self,  questions_listes=[], questions_fichier='myjson'):
        self.questionnaire = questions_listes
        self.fichier_json = questions_fichier

    def importer_json(self):
        """
        Importe le fichier JSON contenant les questions dans la variable questionnaire.
        """
        with open(self.fichier_json, "r") as mj:
            self.questionnaire = json.load(mj)

    def afficher_questionnaire(self):
        """
        Affiche le questionnaire en mémoire
        """
        print(self.questionnaire)


if __name__ == "__main__":
    AMC = Questionnaire()
    AMC.importer_json()
    AMC.afficher_questionnaire()
