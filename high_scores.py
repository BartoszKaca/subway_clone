

def new_score(score):
    scores = []
    f =open('assets/score.txt', 'r')
    for x in f.readlines():
        scores.append(x)
    f.close()
    scores.append(score)
    with open('assets/score.txt', 'w+') as f:
        for items in scores:
            f.write('%s\n' %items)
            print("Zapisano")
    f.close()
    return None
def get_high_score():
    return None