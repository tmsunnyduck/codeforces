'''
A. I Wanna Be the Guy
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

There is a game called "I Wanna Be the Guy", consisting of n levels. Little X and his friend Little Y are addicted to the game. Each of them wants to pass the whole game.

Little X can pass only p levels of the game. And Little Y can pass only q levels of the game. You are given the indices of levels Little X can pass and the indices of levels Little Y can pass. Will Little X and Little Y pass the whole game, if they cooperate each other?
Input

The first line contains a single integer n (1 ≤  n ≤ 100).

The next line contains an integer p (0 ≤ p ≤ n) at first, then follows p distinct integers a1, a2, ..., ap (1 ≤ ai ≤ n). These integers denote the indices of levels Little X can pass. The next line contains the levels Little Y can pass in the same format. It's assumed that levels are numbered from 1 to n.
Output

If they can pass all the levels, print "I become the guy.". If it's impossible, print "Oh, my keyboard!" (without the quotes).
'''
n = int(input())

little_X = [int(x) for x in input().split()]
little_Y = [int(x) for x in input().split()]
little_X.pop(0)
little_Y.pop(0)
#list_n = [x for x in range(n)]

little_X.extend(little_Y)

combined_answers = list(set(little_X))


if len(combined_answers) == n :
    print("I become the guy.")
else :
    print("Oh, my keyboard!")