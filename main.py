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

    def convertion_amc(self, element_def='element'):
        question_amc = []
        erreur = False
        for question in self.questionnaire:
            element = question.get('element', 'item')
            # Création d'un élément de question
            question_amc.append("\\element{"+element+"}{\n")
            # Si la question est simple, multiple
            if question.get('type') == 'simple' or question.get('type') == 'multiple':
                question_type = 'question'
                if question.get('type') == 'multiple':
                    question_type = 'questionmult'
                question_amc.append("\t\\begin{"+question_type+"}")
                # Ajoute l'identifiant de la question
                question_amc.append("{"+question['id']+"}\n")
                # Insère le bareme
                question_amc.append('\t\t'+insere_bareme+"\n")
                # Insère l'intitulé de la question
                question_amc.append(
                    '\t\t'+self.echappement(question.get('question'))+'\n')
                # Insère le multicolonnage si demandé
                if question.get('colonne', None) is not None:
                    if question.get('colonne') > 1:
                        question_amc.append(
                            '\t\t\\begin{multicols}{'+question.get('colonne')+'}\n')
                # Insère les propositions de réponses
                question_amc.append("\t\t\t\\begin{reponses}\n")
                if question.get('reponses', None) is not None:
                    for reponse in question.get('reponses'):
                        if reponse[1] == 0:
                            question_amc.append(
                                '\t\t\t\t\\mauvaise{'+self.echappement(reponse[0])+'}\n')
                        elif reponse[1] == 1:
                            question_amc.append(
                                '\t\t\t\t\\bonne{'+self.echappement(reponse[0])+'}\n')
                        # else: erreur = True
                # Fin des propositions de réponses
                question_amc.append('\t\t\t\\end{reponses}\n')
                # Fin du multicolonnage
                if question.get('colonne', None) is not None:
                    if question.get('colonne') > 1:
                        question_amc.append('\t\t\\end{multicols}\n')
                # FIn de la question
                question_amc.append('\t\\end{'+question_type+'}\n')
            # Fin de l'élément de question
            question_amc.append('}\n')
        question_r = ''.join(question_amc)
        with open('questionnaire_amc.tex', 'w+') as fichier:
            fichier.write(question_r)

    def echappement(self, chaine):
        return chaine  # chaine.replace('\\', '\\\\')


if __name__ == "__main__":
    AMC = Questionnaire()
    AMC.importer_json()
    AMC.afficher_questionnaire()
    AMC.convertion_amc()
