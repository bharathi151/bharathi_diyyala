class User:
    counter = 0
    def __init__(self, name):
        self.name = name
        type(self).counter += 1
    @staticmethod
    def get_counter():
        return User.counter
