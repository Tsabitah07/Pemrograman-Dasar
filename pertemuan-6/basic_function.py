def min_score(score):
    lowest = score[0]
    for i in score:
        if lowest > i:
            lowest = i

    return lowest

def max_score(score):
    highest = score[0]
    for i in score:
        if highest < i:
            highest = i

    return highest

def search_score(score, search_score):
    if search_score in score:
        print(f"Score {search_score} found at index {score.index(search_score)}")
    else:
        print(f"Score {search_score} not found in the list.")

def sorted_scores(score, reverse=False):
    sort_score = []

    if reverse:
        while score:
            highest = score[0]
            for i in score:
                if i > highest:
                    highest = i
            sort_score.append(highest)
            score.remove(highest)
        return sort_score
    else:
        while score:
            lowest = score[0]
            for i in score:
                if i < lowest:
                    lowest = i
            sort_score.append(lowest)
            score.remove(lowest)
        return sort_score