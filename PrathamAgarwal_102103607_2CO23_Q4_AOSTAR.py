# Q4 AO STAR
# Sources GeekForGeeksYoutube W3School Javatpoint


def Cost(Heurestic, condition, wt=1):
    cost = {}
    if 'AND' in condition:
        AND_nodes = condition['AND']
        Path_A = ' AND '.join(AND_nodes)
        PathA = sum(Heurestic[node]+wt for node in AND_nodes)
        cost[Path_A] = PathA

    if 'OR' in condition:
        OR_nodes = condition['OR']
        Path_B = ' OR '.join(OR_nodes)
        PathB = min(Heurestic[node]+wt for node in OR_nodes)
        cost[Path_B] = PathB
    return cost


def shortest_path(Start, update, Heurestic):
    Path = Start
    if Start in update.keys():
        Min_cost = min(update[Start].values())
        key = list(update[Start].keys())
        values = list(update[Start].values())
        Index = values.index(Min_cost)

        Next = key[Index].split()

        if len(Next) == 1:

            Start = Next[0]
            Path += '<--|' + shortest_path(Start, update, Heurestic)

        else:
            Path += '<--|('+key[Index]+') '

            Start = Next[0]
            Path += '[' + shortest_path(Start, update, Heurestic) + ' + '

            Start = Next[-1]
            Path += shortest_path(Start, update, Heurestic) + ']'

    return Path


def update_cost(Heurestic, cond, wt=1):
    MainNodes = list(cond.keys())
    MainNodes.reverse()
    leastCost = {}
    for key in MainNodes:
        condition = cond[key]
        print(key, ':', cond[key], '>>>', Cost(Heurestic, condition, wt))
        c = Cost(Heurestic, condition, wt)
        Heurestic[key] = min(c.values())
        leastCost[key] = Cost(Heurestic, condition, wt)
    return leastCost


Heurestic = {'A': -1, 'B': 6, 'C': 12, 'D': 10, 'E': 4, 'F': 4, 'G': 5, 'H': 7}

cond = {
    'A': {'OR': ['D'], 'AND': ['B', 'C']},
    'B': {'OR': ['G', 'H']},
    'D': {'AND': ['E', 'F']}
}

wt = 1

print('Updated Cost :')
update = update_cost(Heurestic, cond, wt=1)
print('--------------------------------------------------------------------------')
print('Shortest Path :\n', shortest_path('A', update, Heurestic))
