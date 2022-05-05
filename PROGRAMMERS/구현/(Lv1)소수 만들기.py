from itertools import combinations

def isprime(n):
    sqrt = int(n ** 0.5)
    for i in range(2, sqrt + 1):
        if not n % i:
            return 0
    return 1

def solution(nums):
    answer = 0
    comb = list(map(sum, combinations(nums, 3)))
    return sum(map(isprime, comb))
