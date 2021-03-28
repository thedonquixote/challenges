
n = 3
cards = [8, 5, 6, 25, 6, 16]
def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a
def takeTwo(cards):
    gcff = -1
    cardone=0
    cardtwo=0
    for i in range(len(cards)):
        for j in range(len(cards)):
            print(cards[i],cards[j])
            if gcd(cards[i],cards[j]) > gcff:
                gcff = gcd(cards[i],cards[j])
                cardone = i
                cardtwo = j

    newlist = []
    for i in range(len(cards)):
        if i != cardone and i != cardtwo:
            newlist.append(cards[i])
    return newlist, gcff
newlist = cards
score = 0
for i in range(n-1):
    newlist, gcf = takeTwo(newlist)
    score += gcf 
print(score)