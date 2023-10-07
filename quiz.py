import random
import json
from question import Question

class Quiz:
    """
    Quiz class
    """
    def __init__(self, questionsFile='questions.json'):
        self.questions = self.load_questions(questionsFile)
        self.currScore = 0
    
    def load_questions(self, questionsFile):
        with open(questionsFile, 'r') as file:
            data = json.load(file)
            return [Question(item) for item in data]

    def ask_questions(self, num):
        """
        function for asking user questions
        """
        self.current_score = 0
        questions_asked = random.sample(self.questions, num)

        for question in questions_asked:
            user_answer = input(question.text + "\nYour answer: ")
            if user_answer == question.answer:
                self.current_score += 1

    
    def get_score(self):
        """
        Returns the current score
        """
        return self.currScore

            