from GameParameters import *

def new_score(score):
    dates = []
    scores = []
    f =open('assets/score.txt', 'r')
    for x in f.readlines():
        if x !="\n" and x!=" ":
            scores.append(int(x))
    f.close()
    scores.append(score)
    with open('assets/score.txt', 'w+') as f:
        for items in scores:
            f.write('\n%s' %items)
    f.close()
    return None
def get_high_score():
    scores = []
    f = open('assets/score.txt', 'r')
    for x in f.readlines():
        if x != "\n" and x!=" ":
            scores.append(int(x))
    f.close()
    scores = insertion_sort(scores)
    x = scores[-1]
    return x
def get_score_list():
    scores = []
    f = open('assets/score.txt', 'r')
    for x in f.readlines():
        if x != "\n" and x!=" ":
            scores.append(int(x))
    f.close()
    scores = insertion_sort(scores)
    effect = ""
    if len(scores)>4:
        for i in range(1,6):
            effect += "\n"+str(i)+". "+str(scores[i*-1])
    else:
        for i in range(1,len(scores)):
            effect += "\n"+str(i)+". "+str(scores[i*-1])
    return effect
def erase_high_scores():
    with open('assets/score.txt', 'w+') as f:
        f.write(" ")
    f.close()