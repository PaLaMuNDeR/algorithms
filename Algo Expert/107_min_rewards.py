"""
Min Rewards
Imagine that you're a teacher who's just graded the final exam in a class. You have a list of student scores on the
final exam in a particular order (not necessarily sorted), and you want to reward your students. You decide to do so
fairly by giving them arbitrary rewards following two rules: first, all students must receive at least one reward;
second, any given student must receive strictly more rewards than an adjacent student (a student immediately to the
left or to the right) with a lower score and must receive strictly fewer rewards than an adjacent student with a higher
score. Assume that all students have different scores; in other words, the scores are all unique. Write a function that
takes in a list of scores and returns the minimum number of rewards that you must give out to students, all the while
satisfying the two rules.
Sample input: [8, 4, 2, 1, 3, 6, 7, 9, 5] Sample output: 25 ([4, 3, 2, 1, 2, 3, 4, 5, 1])

"""

# Find local mins and assign 1 - then expand to left and right
def minRewards(score):
    local_mins = []
    answer = [1]*len(score)
    if len(answer) == 1:
        return 1
    for i in range(len(score)):
        if i==0:
            if score[i] < score[i+1]:
                local_mins.append(i)
        elif i==len(score)-1:
            if score[i-1] > score[i]:
                    local_mins.append(i)
        else:
            if score[i-1] > score[i] < score[i+1]:
                local_mins.append(i)
    print(local_mins)

    for currentIndex in local_mins:
        leftIndex = currentIndex -1
        while leftIndex >= 0 and score[leftIndex] > score[leftIndex+1]:
            answer[leftIndex] = max(answer[leftIndex], answer[leftIndex+1]+1)
            leftIndex -= 1

        rightIndex = currentIndex + 1
        while rightIndex < len(score) and score[rightIndex] > score[rightIndex-1]:
            answer[rightIndex] = max(answer[rightIndex], answer[rightIndex-1]+1)
            rightIndex += 1


    print(answer)
    return sum(answer)


print(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))
print(minRewards([1]))
print(minRewards([800,400,20,10,30,61,70,90,17,21,22,13,12,11,8,4,2,1,3,6,7,9,0,68,55,67,57,60,51,661,50,65,53]))