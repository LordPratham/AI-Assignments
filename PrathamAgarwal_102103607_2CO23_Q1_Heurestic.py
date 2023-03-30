# Q1 Heurestic
# Sources GFG Youtube W3School Javatpoint
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


def enqueue(element, goal):
    global d
    global queue
    queue.append(element)
    d.append(heurestic(element, goal))


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


def heurestic(s, g):
    dist = 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            if (s[i][j] != g[i][j]):
                dist += 1

    return dist


def search(s, g):
    global d
    global visited

    if s == g:
        print("Found")
        exit()
    while 1:
        print(len(visited))
        outcome = up(s)
        if outcome == g:
            print("Found")
            exit()
        if outcome not in visited:
            enqueue(outcome, g)
            visited.append(outcome)

        outcome = down(s)
        if outcome == g:
            print("Found")
            exit()
        if outcome not in visited:
            enqueue(outcome, g)
            visited.append(outcome)

        outcome = right(s)
        if outcome == g:
            print("Found")
            exit()
        if outcome not in visited:
            enqueue(outcome, g)
            visited.append(outcome)

        outcome = left(s)
        if outcome == g:
            print("Found")
            exit()
        if outcome not in visited:
            enqueue(outcome, g)
            visited.append(outcome)

        if not queue:
            print("This case is not Possible!")
            exit()
        s = dequeue(d)


def main():
    start = [
        [2, 0, 3],
        [1, 8, 4],
        [7, 6, 5]
    ]

    goal = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]

    # goal=[
    # [1,2,3],
    # [8,4,0],
    # [7,6,5]
    # ]

    search(start, goal)
    # ans=heurestic(start,start)
    # print(ans)


if __name__ == "__main__":
    main()
