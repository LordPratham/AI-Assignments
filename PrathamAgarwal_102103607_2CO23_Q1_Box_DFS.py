# Q1 Box World DFS
# Sources GFG YouTube W3School 
import copy

visited=[]
queue=[]

def generateStates(s):
    global queue
    temp=copy.deepcopy(s)
    for i in range(len(s)):
        if(len(s[i])!=0):
            topElem=temp[i][-1]
            for j in range(len(s)):
                temp1=copy.deepcopy(temp)
                if j!=i:
                    temp1[j]+=topElem
                    del temp1[i][-1]
                    # print(temp1)
                    temp1.sort()
                    if temp1 not in visited and temp1 not in queue:
                        
                        queue.append(temp1)
    return queue[-1]

def dequeue():
    global queue
    outcome=queue[-1]
    queue.pop()
    return outcome
                    
def search(s,g):
    global queue
    global visited
    if s==g:
        print("Found!")
        exit()
    else:
        while 1:
            # for i in queue:
            #     print(i)
            print(len(visited))
                
            outcome=generateStates(s)
            visited.append(outcome)
            if outcome==g:
                print("Found!")
                exit()
            
            s =dequeue()

            if not queue:
                print("State not found!")
                exit()
            
def main():
    start=[["A"],["B", "C"],[]]
    # goal=[[], ['A', 'C'], ['B']]
    goal=[["A", "B", "C"],[],[]]
    start.sort()
    goal.sort()
    # print(start)
    # print(goal)
    # generateStates(start)
    # for i in queue:
    #     print(i)
    
    search(start,goal)

if __name__=="__main__":
    main()