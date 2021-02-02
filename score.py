score = []
while True:
    inscore = int(input('分數'))
    if inscore == '':
        break
    else:
        score.append(inscore)
        score2 = sorted(score,reverse=True)
#        score.sort()
#        score.reverse()
    print(score2)
