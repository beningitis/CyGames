from os import path

HS_FILE = "highscore.txt"


def load_hs(self):
    # load high score
    self.dir = path.dirname(__file__)
    with open(path.join(self.dir, HS_FILE), 'r') as f:
        try:
            self.high_score = int(f.read())
        except:
            self.high_score = 0


def update_hs(self):
    with open(path.join(self.dir, HS_FILE), 'w') as f:
        f.write(str(self.score))

