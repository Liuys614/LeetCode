class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [[] for _ in range(numCourses)]
        outdegree = [[] for _ in range(numCourses)]
        
        for a,b in prerequisites:
            indegree[a].append(b)
            outdegree[b].append(a)
            
        start = [i for i,v in enumerate(indegree) if not v]  #find initial nodes which no prerequistes
        res = []
        
        while start:
            s = start.pop()
            res.append(s)
            for n in outdegree[s]:
                indegree[n].remove(s)
                if not indegree[n]: #add nodes that all prerequistites are done
                    start.append(n)
                    
        return res if len(res) == numCourses else []
