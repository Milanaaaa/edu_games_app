class User:
    def __init__(self, id, login, password=None, balls=0):
        self.id = id
        self.login = login
        self.password = password
        self.balls = balls

    def get_balls(self):
        return self.balls
