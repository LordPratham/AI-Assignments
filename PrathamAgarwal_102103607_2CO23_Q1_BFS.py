# Q1 BFS
# Sources GFG Youtube W3School Javatpoint
import copy
queue = []
visited = []


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


def enqueue(element):
    global queue
    queue.append(element)



def dequeue():
    global queue
    s = queue[0]
    queue.pop(0)
    return s


def search(s, g):
    global visited

    if s == g:
        print("Found")
        exit()
    while 1:
        outcome = up(s)
        if outcome == g:
            print("Found")
            exit()
        if outcome not in visited:
            enqueue(outcome)
            visited.append(outcome)

        outcome = down(s)
        if outcome == g:
            print("Found")
            exit()
        if outcome not in visited:
            enqueue(outcome)
            visited.append(outcome)

        outcome = right(s)
        if outcome == g:
            print("Found")
            exit()
        if outcome not in visited:
            enqueue(outcome)
            visited.append(outcome)

        outcome = left(s)
        if outcome == g:
            print("Found")
            exit()
        if outcome not in visited:
            enqueue(outcome)
            visited.append(outcome)

        if not queue:
            print("This case is not Possible!")
            exit()
        s = dequeue()


def main():
    start = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]
    # goal=[
    # [1,2,3],
    # [8,4,0],
    # [7,6,5]
    # ]

    goal = [
        [2, 8, 1],
        [0, 4, 3],
        [7, 6, 5]
    ]

    search(start, goal)


if __name__ == "__main__":
    main()
