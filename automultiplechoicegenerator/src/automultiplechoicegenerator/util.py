
# coding: utf-8
import json
import os.path
import sys


class Questionnaire:

    questionnaire = []  # Questionnaire en cours
    fichier_json = ''  # Nom du fichier json contenant les questions
    chemin = ''

    def __init__(self,  questions_listes=[], questions_fichier='myjson'):
        pathname = os.path.dirname(sys.argv[0])
        self.questionnaire = questions_listes
        self.fichier_json = os.path.join(pathname, questions_fichier)
        self.chemin = pathname

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
            # On récupère le nombre de points, 1 par défaut
            points = str(question.get('points', 1))
            # On récupère la pénalité en cas d'erreur, 0 par défaut,
            penalite = str(question.get('penalite', 0))
            # Si la question est simple, multiple
            if question.get('type') == 'simple' or question.get('type') == 'multiple':
                question_type = 'question'
                # e Réponse incohérente = 0 pt / v Aucune réponse = 0 pt / b  bonne réponse rapporte = points / m mauvaise reponse = penalite / Max Total de points de la question
                insere_bareme = "\\bareme{e=0,v=0,b=" + \
                    points+",m="+penalite+",MAX="+points+"}"
                if question.get('type') == 'multiple':
                    question_type = 'questionmult'
                    # e Réponse incohérente = 0 pt / v Aucune réponse = 0 pt / b  bonne réponse rapporte = points / m mauvaise reponse = points ÷ Nbre de propositions / Max Total de points de la question / p = plancher / d= élève par de 1 point
                    insere_bareme = "\\bareme{e=0,v=0,d="+points + \
                        ",p=0,b=0,m=-"+points+"/NB,MAX="+points+"}"
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
