def acmTeam(topic):
    scores = []
    topics = []

    for x in topic:
        topics.append([int(y) for y in list(x)])
    

    for x in combinations(topics,2):
        score = [x+y for x,y in zip(x[0],x[1])]
        scores.append(len([x for x in score if x>=1]))
    print(scores)
    max_num = max(scores)
    count = scores.count(max_num)
    
    return [max_num,count]
