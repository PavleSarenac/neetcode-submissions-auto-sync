class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointToDistanceMap = dict()
        euclideanDistances = []

        for point in points:
            euclideanDistance = self.calculateEuclideanDistance(point[0], 0, point[1], 0)
            euclideanDistances.append(euclideanDistance)
            if not pointToDistanceMap.get(euclideanDistance):
                pointToDistanceMap[euclideanDistance] = [point]
            else:
                pointToDistanceMap[euclideanDistance].append(point)
        heapq.heapify(euclideanDistances)

        kClosestPoints = []
        for _ in range(k):
            kClosestPoints.append(pointToDistanceMap[heapq.heappop(euclideanDistances)].pop())
        return kClosestPoints

    def calculateEuclideanDistance(self, x1: int, x2: int, y1: int, y2: int) -> float:
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)