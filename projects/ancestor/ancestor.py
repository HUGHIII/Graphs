
from stackAndQ import Stack, Queue


# wherever child/starting node is found, get parent and see if that parent is a child anywhere, if so repeat. if you still have two left with no parents return lower value

# of starting node has no parents return -1




def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    vis = set()
    q.enqueue([starting_node])
    allPaths = []
    # for e in ancestors:
    #    
    #     if e[1] != starting_node:
    #         return -1
    cache = {}
    for ancestor in ancestors: 
        parent = ancestor[0]
        child = ancestor[1]
        if child not in  cache:
            cache[child] = parent
    if starting_node not in cache:
        return -1 
              
    while q.size():
        path = q.dequeue()
        v = path[-1]
        print(path)
        print(v)
        if v not in vis:
            vis.add(v)
        
            for e in ancestors:
                if e[1] == v:
                    newList = list(path)
                    newList.append(e[0])
                    q.enqueue(newList)
                    allPaths.append(newList)
           
  
    if len(allPaths[-1]) == len(allPaths[-2]):
        twoOldest = []
        for i in range(len(allPaths) -2, len(allPaths)):
            twoOldest.append(allPaths[i][-1])
            twoOldest.sort()
            return twoOldest[0]
    if len(allPaths[-1]) > len(allPaths[-2]):
        return allPaths[-1][-1]














test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors,1))

# ```
#  10
#  /
# 1   2   4  11
#  \ /   / \ /
#   3   5   8
#    \ / \   \
#     6   7   9
# ```