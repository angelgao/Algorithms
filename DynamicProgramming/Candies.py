"""
Problem: Each child has a rating score and Alice wants
         to give at least 1 candy to each child. If two
         children sit next to each other, then the one with
         the higher rating must get more candies.
         What is the minimum number of candies Alice needs?

Input: 
    First line is integer N (number of children)
    Each following line indicates the rating of each child
"""


def MinCandies(N, ratings):
    sum = 0
    candies = [0] * N
    candies[0] = 1
    for i in range(1,N):
        if ratings[i-1] >= ratings[i]:
            if candies[i-1] == 1:
                candies[i] = 1
                j = i-1
                while ratings[j] > ratings[j+1]:
                    candies[j] = max(candies[j+1] + 1, candies[j])
                    j -= 1
            else:
                candies[i] = 1
        else:
            candies[i] = candies[i-1] + 1

    for i in range(0, len(candies)):
        sum += candies[i]

    return sum

#collect input
N = int(raw_input())
ratings = [0] * N
for i in range(N):
    ratings[i] = int(raw_input())

print MinCandies(N, ratings)
    
