"""
Problem: Given a value N, and an infinite supply of
         each of the coins C={C1, C2, ..., CM}. How
         many ways can we make the change if order
         does not matter.

Input: 
    First line contains two integers N and M respectively
    Second line contains M integers representing C.
"""

from sets import Set

#Collect Input
N,M = map(int, raw_input().split())
coins = map(int, raw_input().split())
coins.insert(0,0)

def CoinChange(N, M, coins):
   # A[i] represents num of ways to make change for i
    A = [[0] * (N+1) for _ in range(M+1)]
    for i in range(N+1):
        for j in range(M+1):
            if i == 0:
                A[j][i] = 1
            elif j == 0:
                A[j][i] = 0
            elif coins[j] > i:
                A[j][i] = A[j-1][i]
            else:
                A[j][i] = A[j][i-coins[j]] + A[j-1][i]
    return A[M][N]

print CoinChange(N,M,coins)

