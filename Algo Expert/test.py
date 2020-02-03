"""
A garden is considered aesthetically pleasing when the trees are in different heights in sequential order.
Each tree should be either taller or shorter than the previous and the next tree, but not equal.


E.g. Aesthetically pleasing garden
```
7
7     6
7  5  6
7  5  6     4
7  5  6  2  4
7  5  6  2  4
7  5  6  2  4
```

Non pleasing gardens:

```
4  4
4  4  3
4  4  3  2
4  4  3  2


_____________


3  3
3  3
3  3
```

On input array with given height of each tree (e.g. [7,5,6,2,4])
compute the minimum amount of cuts needed to make the garden aesthetically pleasing.

"""
def solution(S):
    garden = ['E' for i in S]
    for i in range(0, len(S)-1):
        if S[i] > S[i+1]:
            garden[i] = 'G'
        elif S[i] < S[i+1]:
            garden[i] = 'S'
    print(garden)
    cuts = 0
    for i in range(1,len(S)-1,2):
        if garden[i] == 'G' and garden[i+1] == 'S':
            if garden[i-1] == 'S':
                pass
            else:
                cuts += 1
                print("Cutting A: "+str(i))
        elif garden[i] == 'S' and garden[i+1] == 'G':
            if garden[i-1] == 'G':
                pass
            else:
                if i + 1 == len(S):
                    pass
                else:
                    cuts += 1
                    print("Cutting B: "+str(i))
        elif i + 1 == len(S)-1:
            if garden[i] == 'G' and garden[i-1] == 'S':
                return cuts
            if garden[i] == 'S' and garden[i-1] ==' G':
                return cuts
        cuts += 1
        print("Cutting C: " + str(i))

    return cuts

print(solution([5,4,3,2,6]))
print(solution([3,7,8,3,5]))
print(solution([3,7,4,5]))
print(solution([5,5,5,5,5]))
print(solution([7,6,6,1,1,1]))

