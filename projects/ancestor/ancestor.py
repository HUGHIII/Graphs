
from stack import Stack


# wherever child/starting node is found, get parent and see if that parent is a child anywhere, if so repeat. if you still have two left with no parents return lower value

# of starting node has no parents return -1




def earliest_ancestor(ancestors, starting_node):
    s = Stack()
    vis = set()
    s.push([starting_node])

    while s.size():
        path = s.pop()
        v = path[-1]
        print(path)
        print(v)
        if v not in vis:
            vis.add(v)
        
            for e in ancestors:
                if e[1] == v:
                    path.append(e[0])
                    s.push(path)
            












test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors,6))

# ```
#  10
#  /
# 1   2   4  11
#  \ /   / \ /
#   3   5   8
#    \ / \   \
#     6   7   9
# ```