import main
from os import path

def load_data(self):
    # load high score
    self.dir = path.dirname(__file__)
    with open(path.join(self.dir, HS_FILE), 'w') as f:
        try:
            self.highscore = int(f.read())
        except:
            self.highscore = 0


# goes in main after player has lost and score is counted
'''
if self.score > self.highscore:
    self.highscore = self.score
    self.draw_text("NEW HIGH SCORE!", 22, WHITE, WIDTH / 2, HEIGHT / 2)
    with open(path.join(self.dir, HS_FILE), 'w') as f:
        f.write(str(self.score))
else
    self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH /2, HEIGHT / 2)
'''