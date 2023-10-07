class Question:
    """
    Question class
    """
    def __init__(self, data):
        self.text = data["text"]
        self.answer = data["answer"]
