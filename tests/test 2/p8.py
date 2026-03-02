def f(c):
    y=0
    cards=["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
    for i in range(len(cards)):
        for j in c:
            if cards[i] == j:
                cards[i]=""
    for i in range(len(cards)):
        for j in range(len(cards)):
            if cards[i]!="" and cards[i]==cards[j]:
                y=cards[j]
    return y