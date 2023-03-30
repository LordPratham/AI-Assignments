# Q3 A Star Searching Algorithm
# Sources GFG Youtube 
import copy
queue = []
visited = []
d = []


def findZero(s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 0:
                return (i, j)


def up(s):
    (i, j) = findZero(s)
    # st = []
    temp = copy.deepcopy(s)
    if i > 0:
        temp[i][j] = temp[i-1][j]
        temp[i-1][j] = 0
    return temp


def down(s):
    (i, j) = findZero(s)
    temp = copy.deepcopy(s)
    if i < 2:
        temp[i][j] = temp[i+1][j]
        temp[i+1][j] = 0
    return temp


def right(s):
    (i, j) = findZero(s)
    temp = copy.deepcopy(s)
    if j < 2:
        temp[i][j] = temp[i][j+1]
        temp[i][j+1] = 0
    return temp


def left(s):
    (i, j) = findZero(s)
    temp = copy.deepcopy(s)
    if j > 0:
        temp[i][j] = temp[i][j-1]
        temp[i][j-1] = 0
    return temp


def enqueue(element, goal, pathlen):
    global d
    global queue
    queue.append(element)
    d.append(heurestic(element, goal, pathlen))


def minIndex(d):
    mini = min(d)
    ind = d.index(mini)
    return (ind)


def dequeue(d):
    global queue
    ind = minIndex(d)
    s = queue[ind]
    queue.pop(ind)
    d.pop(ind)
    return s


def heurestic(s, g, pathlen):
    dist = 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            if (s[i][j] != g[i][j]):
                dist += 1

    return dist+pathlen


def printvis():
    print("Length of visited Queue is: ", len(visited))


def search(s, g):
    global d
    global visited

    if s == g:
        print("Found")
        printvis()
        exit()
    pathlen = 1
    while 1:

        outcome = up(s)
        print(outcome)
        if outcome == g:
            print("Found")
            printvis()
            exit()
        if outcome not in visited:
            if outcome not in queue:
                enqueue(outcome, g, pathlen)
                visited.append(outcome)

        outcome = down(s)
        print(outcome)
        if outcome == g:
            print("Found")
            printvis()
            exit()
        if outcome not in visited:
            if outcome not in queue:
                enqueue(outcome, g, pathlen)
                visited.append(outcome)

        outcome = right(s)
        print(outcome)
        if outcome == g:
            print("Found")
            printvis()
            exit()
        if outcome not in visited:
            if outcome not in queue:
                enqueue(outcome, g, pathlen)
                visited.append(outcome)

        outcome = left(s)
        print(outcome)
        if outcome == g:
            print("Found")
            printvis()
            exit()
        if outcome not in visited:
            if outcome not in queue:
                enqueue(outcome, g, pathlen)
                visited.append(outcome)

        if not queue:
            print("This case is not Possible!")
            printvis()
            exit()
        s = dequeue(d)
        pathlen += 1


def main():
    start = [
        [2, 0, 3],
        [1, 8, 4],
        [7, 6, 5]
    ]

    # goal = [
    #     [1, 2, 3],
    #     [8, 0, 4],
    #     [7, 6, 5]
    # ]

    goal = [
        [1, 2, 3],
        [8, 4, 0],
        [7, 6, 5]
    ]

    search(start, goal)
    # ans=heurestic(start,start)
    # print(ans)


if __name__ == "__main__":
    main()
