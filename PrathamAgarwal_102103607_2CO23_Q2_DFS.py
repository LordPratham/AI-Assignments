# Q2 DFS
# Sources StackOverflow Youtube Javatpoint W3School
import copy
queue = []
visited = []
cap4 = 4
cap3 = 3


def fill4(s):
    temp = copy.deepcopy(s)
    temp[0] = cap4
    return temp


def fill3(s):
    temp = copy.deepcopy(s)
    temp[1] = cap3
    return temp


def pourTo4(s):
    temp = copy.deepcopy(s)
    toReduce = cap4-temp[0]
    temp[0] = temp[0]+temp[1] if (temp[0]+temp[1]) < cap4 else cap4
    temp[1] = temp[1]-toReduce if (temp[1]-toReduce) > 0 else 0
    return temp


def pourTo3(s):
    temp = copy.deepcopy(s)
    toReduce = cap3-temp[1]
    temp[1] = temp[0]+temp[1] if (temp[0]+temp[1]) < cap3 else cap3
    temp[0] = temp[0]-toReduce if (temp[0]-toReduce) > 0 else 0
    return temp


def empty4(s):
    temp = copy.deepcopy(s)
    if s[0] != 0:
        temp[0] = 0
    return temp


def empty3(s):
    temp = copy.deepcopy(s)
    if s[1] != 0:
        temp[1] = 0
    return temp


def enqueue(element):
    global queue
    queue.append(element)


def dequeue():
    global queue
    s = queue[-1]
    queue.pop()
    return s


def search(s, g):
    global visited

    if s == g:
        print("Found")
        exit()
    while 1:
        outcome = fill4(s)
        if outcome[0] == g[0]:
            print("Found")
            exit()
        if outcome not in visited:
            enqueue(outcome)
            visited.append(outcome)

        outcome = fill3(s)
        if outcome[0] == g[0]:
            print("Found")
            exit()
        if outcome not in visited:
            enqueue(outcome)
            visited.append(outcome)

        outcome = pourTo4(s)
        if outcome[0] == g[0]:
            print("Found")
            exit()
        if outcome not in visited:
            enqueue(outcome)
            visited.append(outcome)

        outcome = pourTo3(s)
        if outcome[0] == g[0]:
            print("Found")
            exit()
        if outcome not in visited:
            enqueue(outcome)
            visited.append(outcome)

        outcome = empty4(s)
        if outcome[0] == g[0]:
            print("Found")
            exit()
        if outcome not in visited:
            enqueue(outcome)
            visited.append(outcome)

        outcome = empty3(s)
        if outcome[0] == g[0]:
            print("Found")
            exit()
        if outcome not in visited:
            enqueue(outcome)
            visited.append(outcome)

        if not queue:
            print("This case is not Possible!")
            exit()
        s = dequeue()
        print(queue)


def main():
    start = [
        0, 0
    ]
    # goal=[
    # [1,2,3],
    # [8,4,0],
    # [7,6,5]
    # ]

    goal = [
        2, 0
    ]

    search(start, goal)


if __name__ == "__main__":
    main()
