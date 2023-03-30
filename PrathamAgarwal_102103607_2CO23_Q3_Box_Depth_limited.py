# Q3 Box World Depth Limited
# Sources GFG YouTube W3School
import copy

visited = []
queue = []

def generateStates(s):
    global queue
    temp = copy.deepcopy(s[0])
    for i in range(len(temp)):
        if (len(temp[i]) != 0):
            topElem = temp[i][-1]
            for j in range(len(s)):
                temp1 = copy.deepcopy(temp)
                if j != i:
                    temp1[j] += topElem
                    del temp1[i][-1]
                    # print(temp1)
                    temp1.sort()
                    if temp1 not in visited and temp1 not in queue:

                        queue.append([temp1, s[1]+1])
    return queue[-1][0]


def dequeue():
    global queue
    outcome = queue[-1]
    queue.pop()
    return outcome


def search(s, g, depth):

    global queue
    global visited
    found = 0
    if s[0] == g:
        print("Found!")
        exit()
    else:
        while s[1] <= depth:
            # for i in queue:
            #     print(i)
            print(len(visited))
            # print(s[1])

            outcome = generateStates(s)
            visited.append(outcome)
            if outcome == g:
                print("Found!")
                found = 1
                exit()

            s = dequeue()

            if not queue:
                print("State not found!")
                exit()

        if not found:
            print("State not found!")
            exit()


def main():
    start = [[["B"], ["A", "C"], []], 0]
    # goal=[[], ['A', 'C'], ['B']]
    goal = [["A", "B", "C"], [], []]
    depth = 1
    start[0].sort()
    goal.sort()
    # print(start)
    # print(goal)
    # generateStates(start)
    # for i in queue:
    #     print(i)

    search(start, goal, depth)


if __name__ == "__main__":
    main()
