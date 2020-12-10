class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {i:[] for i in range(numCourses)}
        for x in prerequisites:
            dic[x[0]].append(x[1])

        def check(c:int) -> bool:
            if c in course:
                return True
            if not dic[c]:
                course.add(c)
                return True
            if c in visited:
                return False
            visited.add(c)
            for r in dic[c]:
                if not check(r): 
                    visited.remove(c)    
                    return False
            visited.remove(c)    # important
            course.add(c)
            return True 
        
        course = set() 
        for a in dic:
            visited= set()
            if not check(a):
                print(course)
                return False

        return True 
