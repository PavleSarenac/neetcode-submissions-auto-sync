class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencyList = dict()

        for targetCourse, prerequisite in prerequisites:
            if targetCourse not in adjacencyList:
                adjacencyList[targetCourse] = set()
            adjacencyList[targetCourse].add(prerequisite)

            transitivePrerequisites = deque()
            transitivePrerequisites.append(adjacencyList[targetCourse])
            visitedTargets = set()
            visitedTargets.add(targetCourse)
            while transitivePrerequisites:
                currentTransitivePrerequisites = transitivePrerequisites.popleft()
                for currentTransitivePrerequisite in currentTransitivePrerequisites:
                    if currentTransitivePrerequisite == targetCourse:
                        return False
                    if currentTransitivePrerequisite in adjacencyList and currentTransitivePrerequisite not in visitedTargets:
                        transitivePrerequisites.append(adjacencyList[currentTransitivePrerequisite])
                        visitedTargets.add(currentTransitivePrerequisite)
        return True