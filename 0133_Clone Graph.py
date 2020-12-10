# DFS with queue
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        newRoot = Node(node.val)
        helper = {node:newRoot} # nodeIndex:nodeptr
        queue = deque([node]) 
        
        while queue:
            node = queue.popleft()
            for n in node.neighbors:
                if n in helper:
                    helper[node].neighbors.append(helper[n])
                else:
                    newNb = Node(n.val,[]) 
                    helper[n] = newNb
                    helper[node].neighbors.append(helper[n])
                    queue.append(n)
            
        return newRoot 


# DFS with queue iteratively
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        newRoot = Node(node.val)
        helper = {node:newRoot} # nodeIndex:nodeptr
        stack = [node]
        
        while stack:
            node = stack.pop()
            for n in node.neighbors:
                if n in helper:
                    helper[node].neighbors.append(helper[n])
                else:
                    newNb = Node(n.val,[]) 
                    helper[n] = newNb
                    helper[node].neighbors.append(helper[n])
                    stack.append(n)
            
        return newRoot 

#DFS with recursivly
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self, node:'Node', helper:dict) :
        for n in node.neighbors:
            if n in helper:
                helper[node].neighbors.append(helper[n])
            else:
                newNb = Node(n.val,[]) 
                helper[n] = newNb
                helper[node].neighbors.append(helper[n])
                self.dfs(n, helper)
                
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        newRoot = Node(node.val)
        helper = {node:newRoot} # old:new
        self.dfs(node, helper)
            
        return newRoot 
