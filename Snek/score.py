import shelve

def main():
    d = shelve.open('score.txt')
    d['score'] = score
    d.close