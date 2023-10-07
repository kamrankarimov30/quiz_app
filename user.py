class User:
    """
    User class
    """
    def __init__(self, name):
        self.name = name 
        self.score = 0
    
    def set_score(self, score):
        self.score = score
    
    def get_score(self):
        return self.score
    