class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if x == y:
                continue
            heapq.heappush(stones, y - x)
        return 0 if len(stones) == 0 else -heapq.heappop(stones)